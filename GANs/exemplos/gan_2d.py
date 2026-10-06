"""GAN mínima em 2D: aprende a desenhar 8 grupos de pontos num círculo.

É o "olá, mundo" das GANs: pequena o bastante para treinar em um minuto
na CPU, e visual o bastante para enxergar os problemas do treino
(colapso de modos, oscilação) e o efeito do WGAN-GP.

Uso:
    python gan_2d.py                      # GAN original (perda não saturante)
    python gan_2d.py --perda wgan-gp      # mesma rede, treinada como WGAN-GP
    python gan_2d.py --passos 5000 --semente 3

Explicação passo a passo: GANs/08-GAN-em-PyTorch.md
"""

import argparse
import math
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", message="Failed to initialize NumPy")
import torch
from torch import nn

PASTA_SAIDA = Path(__file__).parent / "saida"

RAIO = 2.0
DESVIO = 0.05
CENTROS = torch.tensor(
    [[RAIO * math.cos(2 * math.pi * k / 8), RAIO * math.sin(2 * math.pi * k / 8)] for k in range(8)]
)


def amostras_reais(n: int) -> torch.Tensor:
    """Sorteia n pontos: escolhe um dos 8 centros e soma um ruído pequeno."""
    escolhidos = CENTROS[torch.randint(0, 8, (n,))]
    return escolhidos + DESVIO * torch.randn(n, 2)


def mlp(entrada: int, saida: int, largura: int = 128) -> nn.Sequential:
    return nn.Sequential(
        nn.Linear(entrada, largura), nn.ReLU(),
        nn.Linear(largura, largura), nn.ReLU(),
        nn.Linear(largura, saida),
    )


def penalidade_de_gradiente(critico: nn.Module, reais: torch.Tensor, falsas: torch.Tensor) -> torch.Tensor:
    """WGAN-GP: a norma do gradiente do crítico, em pontos entre real e falso, deve ficar perto de 1."""
    alfa = torch.rand(reais.size(0), 1)
    meio = (alfa * reais + (1 - alfa) * falsas).requires_grad_(True)
    gradiente, = torch.autograd.grad(critico(meio).sum(), meio, create_graph=True)
    return ((gradiente.norm(dim=1) - 1) ** 2).mean()


def avaliar_modos(pontos: torch.Tensor) -> tuple[int, float]:
    """Quantos dos 8 grupos o gerador cobre, e que fração dos pontos cai perto de algum grupo."""
    distancias = torch.cdist(pontos, CENTROS)
    menor, grupo = distancias.min(dim=1)
    bons = menor < 4 * DESVIO
    contagem = torch.bincount(grupo[bons], minlength=8)
    cobertos = int((contagem >= 0.02 * len(pontos)).sum())
    return cobertos, float(bons.float().mean())


def desenho_ascii(pontos: torch.Tensor, largura: int = 41, altura: int = 21) -> str:
    """Mapa de densidade no terminal: quanto mais pontos na célula, mais 'escuro' o caractere."""
    tons = " .:-=+*#%@"
    limite = RAIO + 0.6
    grade = torch.zeros(altura, largura)
    col = ((pontos[:, 0] + limite) / (2 * limite) * (largura - 1)).round().long()
    lin = ((limite - pontos[:, 1]) / (2 * limite) * (altura - 1)).round().long()
    dentro = (col >= 0) & (col < largura) & (lin >= 0) & (lin < altura)
    for l, c in zip(lin[dentro].tolist(), col[dentro].tolist()):
        grade[l, c] += 1
    # raiz quadrada: sem ela, a célula mais cheia apaga todas as outras
    grade = (grade.sqrt() / grade.max().clamp(min=1).sqrt() * (len(tons) - 1)).ceil().long()
    return "\n".join("".join(tons[v] for v in linha.tolist()) for linha in grade)


def salvar_svg(reais: torch.Tensor, falsas: torch.Tensor, caminho: Path, titulo: str) -> None:
    """Desenha reais (cinza) e geradas (cor) num SVG, sem depender de matplotlib."""
    tamanho, limite = 360, RAIO + 0.6

    def xy(p):
        return ((p[0] + limite) / (2 * limite) * tamanho, (limite - p[1]) / (2 * limite) * tamanho)

    linhas = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {tamanho} {tamanho + 28}" width="{tamanho}">',
        f'<rect width="{tamanho}" height="{tamanho + 28}" fill="#ffffff"/>',
        f'<text x="8" y="{tamanho + 19}" font-family="sans-serif" font-size="13" fill="#333">{titulo}</text>',
    ]
    for p in reais.tolist():
        x, y = xy(p)
        linhas.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="#9ca3af" fill-opacity="0.5"/>')
    for p in falsas.tolist():
        x, y = xy(p)
        linhas.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="#d946ef" fill-opacity="0.6"/>')
    linhas.append("</svg>")
    caminho.write_text("\n".join(linhas), encoding="utf-8")


def treinar(args) -> None:
    torch.manual_seed(args.semente)
    gerador = mlp(args.ruido, 2)
    discriminador = mlp(2, 1)  # devolve um número: "logit" na GAN original, nota do crítico no WGAN

    if args.perda == "gan":
        betas, passos_d = (0.5, 0.999), 1
    else:
        betas, passos_d = (0.5, 0.9), 5  # o crítico treina mais vezes que o gerador
    opt_g = torch.optim.Adam(gerador.parameters(), lr=args.taxa, betas=betas)
    opt_d = torch.optim.Adam(discriminador.parameters(), lr=args.taxa, betas=betas)
    bce = nn.BCEWithLogitsLoss()
    um, zero = torch.ones(args.lote, 1), torch.zeros(args.lote, 1)
    # Ruído fixo para avaliar: as mesmas entradas a cada relatório, sem mexer nos sorteios do treino.
    ruido_fixo = torch.randn(2000, args.ruido, generator=torch.Generator().manual_seed(1234))

    for passo in range(1, args.passos + 1):
        # 1) Discriminador: aprender a separar real de falso. O gerador fica parado (detach).
        for _ in range(passos_d):
            reais = amostras_reais(args.lote)
            falsas = gerador(torch.randn(args.lote, args.ruido)).detach()
            if args.perda == "gan":
                perda_d = bce(discriminador(reais), um) + bce(discriminador(falsas), zero)
            else:
                perda_d = (discriminador(falsas).mean() - discriminador(reais).mean()
                           + 10 * penalidade_de_gradiente(discriminador, reais, falsas))
            opt_d.zero_grad()
            perda_d.backward()
            opt_d.step()

        # 2) Gerador: produzir pontos que o discriminador classifique como reais.
        falsas = gerador(torch.randn(args.lote, args.ruido))
        if args.perda == "gan":
            perda_g = bce(discriminador(falsas), um)  # versão "não saturante": maximiza log D(G(z))
        else:
            perda_g = -discriminador(falsas).mean()
        opt_g.zero_grad()
        perda_g.backward()
        opt_g.step()

        if passo % args.mostrar_a_cada == 0 or passo == args.passos:
            with torch.no_grad():
                amostra = gerador(ruido_fixo)
            cobertos, precisao = avaliar_modos(amostra)
            print(f"passo {passo:5d} | perda D {perda_d.item():7.3f} | perda G {perda_g.item():7.3f} "
                  f"| grupos cobertos {cobertos}/8 | pontos no alvo {precisao:5.1%}")

    print("\nResultado final (geradas):")
    print(desenho_ascii(amostra))
    PASTA_SAIDA.mkdir(exist_ok=True)
    nome = f"gan_2d_{args.perda}_semente{args.semente}.svg"
    titulo = f"{args.perda.upper()} · {args.passos} passos · {cobertos}/8 grupos · {precisao:.0%} no alvo"
    salvar_svg(amostras_reais(1000), amostra[:1000], PASTA_SAIDA / nome, titulo)
    print(f"\nDesenho salvo em {PASTA_SAIDA / nome}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--perda", choices=["gan", "wgan-gp"], default="gan")
    parser.add_argument("--passos", type=int, default=3000)
    parser.add_argument("--taxa", type=float, default=1e-3, help="taxa de aprendizado do Adam")
    parser.add_argument("--lote", type=int, default=256)
    parser.add_argument("--ruido", type=int, default=8, help="tamanho do vetor de ruído z")
    parser.add_argument("--semente", type=int, default=0)
    parser.add_argument("--mostrar-a-cada", type=int, default=500)
    treinar(parser.parse_args())
