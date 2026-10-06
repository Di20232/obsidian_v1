"""GAN de texto treinada nas notas do cofre (WGAN-GP por caracteres).

Experimento didático: a GAN aprende a imitar trechos de 32 caracteres
das notas. O objetivo não é gerar notas úteis (para isso, RAG e
fine-tuning funcionam muito melhor), e sim ver na prática por que texto
é difícil para GANs e o que elas conseguem aprender assim mesmo.

A arquitetura segue o modelo de linguagem do artigo do WGAN-GP
(Gulrajani et al., 2017): o gerador devolve, para cada posição, uma
distribuição de probabilidade sobre os caracteres, e o crítico compara
essas distribuições com o texto real codificado em one-hot.

Uso:
    python gan_das_notas.py --dados               # só mostra o que foi lido das notas
    python gan_das_notas.py --treinar             # treina; retoma do último ponto salvo
    python gan_das_notas.py --treinar --iteracoes 20000
    python gan_das_notas.py --gerar 20            # gera 20 trechos com o modelo salvo

Explicação e resultados: GANs/10-Experimento-GAN-com-as-Notas.md
"""

import argparse
import random
import re
import sys
import time
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore", message="Failed to initialize NumPy")
import torch
from torch import nn
from torch.nn import functional as F

RAIZ_DO_COFRE = Path(__file__).resolve().parents[2]
PASTA_SAIDA = Path(__file__).parent / "saida"
ARQUIVO_MODELO = PASTA_SAIDA / "gan_das_notas.pt"
ARQUIVO_HISTORICO = PASTA_SAIDA / "historico.csv"

# Mesma política da exportação para IA: nada pessoal, nada de código de terceiros.
PASTAS_EXCLUIDAS = {"Templates", "Diario", "Inbox", "Fontes", "exportacao", "exemplos"}
CARACTERES = "abcdefghijklmnopqrstuvwxyzáàâãéêíóôõúüç0123456789 .,;:!?()-%/\"'"
PALAVRA = re.compile(r"[a-záàâãéêíóôõúüç]{3,}")  # 3+ letras: "a", "o" e "e" valeriam até por acaso


# ---------------------------------------------------------------- dados

def arquivos_de_notas(raiz: Path):
    for caminho in sorted(raiz.rglob("*.md")):
        pastas = caminho.relative_to(raiz).parts[:-1]
        if any(p.startswith(".") for p in pastas) or PASTAS_EXCLUIDAS & set(pastas):
            continue
        yield caminho


def _link_interno(m: re.Match) -> str:
    alvo, _, apelido = m.group(1).partition("|")
    return apelido or alvo.split("/")[-1].replace("-", " ")


def limpar(texto: str) -> str:
    """Tira do Markdown tudo que não é prosa: frontmatter, código, links, tabelas, marcações."""
    texto = re.sub(r"\A---\n.*?\n---\n", " ", texto, flags=re.S)
    texto = re.sub(r"```.*?```", " ", texto, flags=re.S)
    texto = re.sub(r"`[^`\n]*`", " ", texto)
    texto = re.sub(r"!\[\[[^\]]*\]\]", " ", texto)
    texto = re.sub(r"\[\[([^\]]*)\]\]", _link_interno, texto)
    texto = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", texto)
    texto = re.sub(r"https?://\S+", " ", texto)
    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = re.sub(r"\[![\w-]+\][+-]?", " ", texto)
    texto = texto.replace("::", ".").replace("\\|", " ").lower()
    texto = re.sub(r"-{2,}", " ", texto)
    texto = "".join(c if c in CARACTERES else " " for c in texto)
    return re.sub(r"\s+", " ", texto).strip()


def carregar_corpus(raiz: Path) -> tuple[str, int]:
    textos = [limpar(c.read_text(encoding="utf-8", errors="replace")) for c in arquivos_de_notas(raiz)]
    textos = [t for t in textos if len(t) > 100]
    return " ".join(textos), len(textos)


class Trechos:
    """Sorteia janelas de texto começando no início de uma palavra e as codifica como índices."""

    def __init__(self, corpus: str, comprimento: int):
        self.corpus, self.comprimento = corpus, comprimento
        self.vocab = list(CARACTERES)  # fixo: o modelo salvo continua valendo quando as notas mudam
        self.indice = {c: i for i, c in enumerate(self.vocab)}
        self.inicios = [i + 1 for i, c in enumerate(corpus[:-comprimento - 1]) if c == " "]
        self.palavras = set(PALAVRA.findall(corpus))

    def sortear(self, n: int) -> torch.Tensor:
        textos = [self.corpus[i:i + self.comprimento] for i in random.choices(self.inicios, k=n)]
        return torch.tensor([[self.indice[c] for c in t] for t in textos])

    def decodificar(self, indices: torch.Tensor) -> list[str]:
        return ["".join(self.vocab[i] for i in linha) for linha in indices.tolist()]

    def palavras_validas(self, textos: list[str]) -> float:
        """Fração das palavras de 3+ letras que existem nas notas. A primeira e a última
        palavra de cada trecho ficam de fora, porque podem ter sido cortadas no meio."""
        palavras = [p for t in textos for pedaco in t.split()[1:-1] for p in PALAVRA.findall(pedaco)]
        return sum(p in self.palavras for p in palavras) / max(len(palavras), 1)

    @staticmethod
    def variedade(textos: list[str], n: int = 4) -> float:
        """Fração de sequências de 4 caracteres diferentes entre todas as geradas (a métrica distinct-4).
        Repetição ("oooo oooo") derruba o valor: é assim que o colapso de modos aparece no texto."""
        sequencias = [t[i:i + n] for t in textos for i in range(len(t) - n + 1)]
        return len(set(sequencias)) / max(len(sequencias), 1)

    def copiados(self, textos: list[str]) -> float:
        """Fração dos trechos gerados que aparecem idênticos nas notas: sinal de que a rede decorou."""
        return sum(t in self.corpus for t in textos) / max(len(textos), 1)

    def texto_aleatorio(self, n: int) -> list[str]:
        """Linha de base: caracteres sorteados só pela frequência de cada letra, sem nenhuma estrutura."""
        freq = Counter(self.corpus)
        letras, pesos = zip(*freq.items())
        return ["".join(random.choices(letras, pesos, k=self.comprimento)) for _ in range(n)]


# ---------------------------------------------------------------- modelos

class BlocoResidual(nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.camadas = nn.Sequential(
            nn.ReLU(), nn.Conv1d(dim, dim, 5, padding=2),
            nn.ReLU(), nn.Conv1d(dim, dim, 5, padding=2),
        )

    def forward(self, x):
        return x + 0.3 * self.camadas(x)


class Gerador(nn.Module):
    """Ruído -> para cada uma das posições, uma distribuição sobre o vocabulário."""

    def __init__(self, vocab: int, dim: int, comprimento: int, blocos: int, ruido: int):
        super().__init__()
        self.dim, self.comprimento = dim, comprimento
        self.entrada = nn.Linear(ruido, dim * comprimento)
        self.blocos = nn.Sequential(*[BlocoResidual(dim) for _ in range(blocos)])
        self.saida = nn.Conv1d(dim, vocab, 1)

    def forward(self, z):
        x = self.entrada(z).view(-1, self.dim, self.comprimento)
        return F.softmax(self.saida(self.blocos(x)), dim=1)  # (lote, vocab, posições)


class Critico(nn.Module):
    """Texto (one-hot ou distribuição) -> uma nota: quanto maior, mais parecido com as notas reais."""

    def __init__(self, vocab: int, dim: int, comprimento: int, blocos: int):
        super().__init__()
        self.entrada = nn.Conv1d(vocab, dim, 1)
        self.blocos = nn.Sequential(*[BlocoResidual(dim) for _ in range(blocos)])
        self.saida = nn.Linear(dim * comprimento, 1)

    def forward(self, x):
        return self.saida(self.blocos(self.entrada(x)).flatten(1))


def penalidade_de_gradiente(critico, reais, falsos):
    alfa = torch.rand(reais.size(0), 1, 1)
    meio = (alfa * reais + (1 - alfa) * falsos).requires_grad_(True)
    gradiente, = torch.autograd.grad(critico(meio).sum(), meio, create_graph=True)
    return ((gradiente.flatten(1).norm(dim=1) - 1) ** 2).mean()


# ---------------------------------------------------------------- treino

def montar(args, vocab: int):
    gerador = Gerador(vocab, args.dim, args.comprimento, args.blocos, args.ruido)
    critico = Critico(vocab, args.dim, args.comprimento, args.blocos)
    opt_g = torch.optim.Adam(gerador.parameters(), lr=1e-4, betas=(0.5, 0.9))
    opt_c = torch.optim.Adam(critico.parameters(), lr=1e-4, betas=(0.5, 0.9))
    return gerador, critico, opt_g, opt_c


def configuracao(args, dados: Trechos) -> dict:
    return {"dim": args.dim, "blocos": args.blocos, "ruido": args.ruido,
            "comprimento": args.comprimento, "vocab": "".join(dados.vocab)}


def carregar(args, dados: Trechos):
    gerador, critico, opt_g, opt_c = montar(args, len(dados.vocab))
    iteracao = 0
    if ARQUIVO_MODELO.exists() and not args.do_zero:
        salvo = torch.load(ARQUIVO_MODELO)
        if salvo["config"] != configuracao(args, dados):
            sys.exit("O modelo salvo foi treinado com outra configuração (--dim, --blocos, --ruido ou "
                     "--comprimento). Use os mesmos valores, ou --do-zero para recomeçar (o arquivo salvo será substituído).")
        gerador.load_state_dict(salvo["gerador"])
        critico.load_state_dict(salvo["critico"])
        opt_g.load_state_dict(salvo["opt_g"])
        opt_c.load_state_dict(salvo["opt_c"])
        iteracao = salvo["iteracao"]
    return gerador, critico, opt_g, opt_c, iteracao


def gerar_textos(gerador, dados: Trechos, z: torch.Tensor) -> list[str]:
    """Para cada posição, fica o caractere mais provável da distribuição gerada."""
    with torch.no_grad():
        return dados.decodificar(gerador(z).argmax(dim=1))


def treinar(args, dados: Trechos) -> None:
    gerador, critico, opt_g, opt_c, inicio = carregar(args, dados)
    vocab = len(dados.vocab)
    PASTA_SAIDA.mkdir(exist_ok=True)
    if inicio == 0:
        ARQUIVO_HISTORICO.write_text("iteracao,distancia_w,palavras_validas,variedade,copiados,segundos\n",
                                     encoding="utf-8")
    else:
        print(f"Retomando da iteração {inicio}.")
    relogio = time.time()
    # Ruído fixo para avaliar: as mesmas entradas a cada relatório, sem mexer nos sorteios do treino.
    ruido_fixo = torch.randn(200, args.ruido, generator=torch.Generator().manual_seed(1234))

    for iteracao in range(inicio + 1, inicio + args.iteracoes + 1):
        # 1) Crítico: várias rodadas por iteração, para a nota dele ser uma boa estimativa da distância.
        for _ in range(args.passos_critico):
            reais = F.one_hot(dados.sortear(args.lote), vocab).float().transpose(1, 2)
            with torch.no_grad():
                falsos = gerador(torch.randn(args.lote, args.ruido))
            distancia_w = critico(reais).mean() - critico(falsos).mean()
            perda_c = -distancia_w + 10 * penalidade_de_gradiente(critico, reais, falsos)
            opt_c.zero_grad()
            perda_c.backward()
            opt_c.step()

        # 2) Gerador: subir a nota que o crítico dá ao texto inventado.
        perda_g = -critico(gerador(torch.randn(args.lote, args.ruido))).mean()
        opt_g.zero_grad()
        perda_g.backward()
        opt_g.step()

        if iteracao % args.mostrar_a_cada == 0 or iteracao == inicio + args.iteracoes:
            textos = gerar_textos(gerador, dados, ruido_fixo)
            validas, variedade = dados.palavras_validas(textos), dados.variedade(textos)
            copiados, segundos = dados.copiados(textos), time.time() - relogio
            print(f"\niteração {iteracao} | distância W {distancia_w.item():6.3f} | palavras que existem "
                  f"{validas:5.1%} | variedade {variedade:5.1%} | copiados {copiados:4.1%} | {segundos / 60:5.1f} min")
            for t in textos[:4]:
                print(f"   «{t}»")
            with ARQUIVO_HISTORICO.open("a", encoding="utf-8") as f:
                f.write(f"{iteracao},{distancia_w.item():.4f},{validas:.4f},{variedade:.4f},"
                        f"{copiados:.4f},{segundos:.0f}\n")

        if iteracao % args.salvar_a_cada == 0 or iteracao == inicio + args.iteracoes:
            torch.save({"gerador": gerador.state_dict(), "critico": critico.state_dict(),
                        "opt_g": opt_g.state_dict(), "opt_c": opt_c.state_dict(),
                        "iteracao": iteracao, "config": configuracao(args, dados)}, ARQUIVO_MODELO)


def mostrar_dados(dados: Trechos, notas: int) -> None:
    print(f"Notas lidas: {notas}")
    print(f"Caracteres no corpus: {len(dados.corpus):,}".replace(",", "."))
    print(f"Palavras diferentes: {len(dados.palavras):,}".replace(",", "."))
    print(f"Vocabulário ({len(dados.vocab)} caracteres): {''.join(dados.vocab)!r}")
    print("\nTrechos reais sorteados:")
    reais = dados.decodificar(dados.sortear(200))
    for t in reais[:5]:
        print(f"   «{t}»")
    aleatorios = dados.texto_aleatorio(200)
    print("\nLinha de base, letras sorteadas pela frequência:")
    for t in aleatorios[:3]:
        print(f"   «{t}»")
    print("\nReferências para ler o treino (200 trechos de cada):")
    for nome, textos in (("reais", reais), ("aleatórios", aleatorios), ('"o o o..."', ["o o " * 8] * 200)):
        print(f"   {nome:11} palavras que existem {dados.palavras_validas(textos):6.1%} | "
              f"variedade {dados.variedade(textos):6.1%}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    acao = parser.add_mutually_exclusive_group(required=True)
    acao.add_argument("--dados", action="store_true", help="mostra o corpus lido das notas e sai")
    acao.add_argument("--treinar", action="store_true")
    acao.add_argument("--gerar", type=int, metavar="N", help="gera N trechos com o modelo salvo")
    # Os padrões são uma versão reduzida para caber numa CPU (cerca de 0,3 s por iteração em 6 núcleos).
    # O código original do artigo usa dim 512, 5 blocos, 10 passos do crítico e 200.000 iterações, em GPU.
    parser.add_argument("--iteracoes", type=int, default=6000)
    parser.add_argument("--do-zero", action="store_true", help="ignora o modelo salvo e recomeça")
    parser.add_argument("--comprimento", type=int, default=32, help="caracteres por trecho")
    parser.add_argument("--dim", type=int, default=64, help="canais das camadas convolucionais")
    parser.add_argument("--blocos", type=int, default=3, help="blocos residuais em cada rede")
    parser.add_argument("--ruido", type=int, default=128, help="tamanho do vetor de ruído z")
    parser.add_argument("--lote", type=int, default=64)
    parser.add_argument("--passos-critico", type=int, default=5)
    parser.add_argument("--mostrar-a-cada", type=int, default=250)
    parser.add_argument("--salvar-a-cada", type=int, default=500)
    parser.add_argument("--semente", type=int, default=0)
    parser.add_argument("--cofre", type=Path, default=RAIZ_DO_COFRE, help="pasta raiz do cofre")
    args = parser.parse_args()

    random.seed(args.semente)
    torch.manual_seed(args.semente)
    corpus, notas = carregar_corpus(args.cofre)
    dados = Trechos(corpus, args.comprimento)

    if args.dados:
        mostrar_dados(dados, notas)
    elif args.treinar:
        print(f"Corpus: {notas} notas, {len(corpus):_} caracteres.".replace("_", "."))
        treinar(args, dados)
    else:
        if not ARQUIVO_MODELO.exists():
            sys.exit("Nenhum modelo salvo ainda. Rode primeiro com --treinar.")
        gerador, *_ = carregar(args, dados)
        gerador.eval()
        for t in gerar_textos(gerador, dados, torch.randn(args.gerar, args.ruido)):
            print(f"«{t}»")
