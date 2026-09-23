---
tags: [python, boas-praticas, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Boas Práticas e Próximos Passos

## Você terminou o essencial de Python. E agora?

As 15 notas anteriores cobrem o que praticamente todo programa Python usa: variáveis, decisões, repetição, estruturas de dados, funções, módulos, erros, arquivos e objetos. Isso já é suficiente para escrever programas reais e pequenos utilitários. Esta nota fecha com hábitos de qualidade e para onde ir depois — veja também [[../Programacao-Geral/00-Indice]] para conhecimento de programação que vale para qualquer linguagem, não só Python.

## PEP 8: o guia de estilo oficial

Python tem um documento chamado **PEP 8** que define convenções de estilo aceitas pela comunidade inteira. Isso importa porque código consistente é mais fácil de ler — inclusive por você mesmo, seis meses depois. Os pontos mais usados no dia a dia:

- Indentação: 4 espaços (nunca misturar com tabs).
- Nomes de variáveis e funções: `snake_case` (`minha_variavel`).
- Nomes de classes: `PascalCase` (`MinhaClasse`), como em [[15-Programacao-Orientada-a-Objetos]].
- Constantes: `MAIUSCULO_COM_UNDERSCORE`.
- Uma linha em branco entre blocos lógicos, duas entre funções/classes no nível principal do arquivo.
- Linhas com no máximo ~79-99 caracteres (evita rolagem horizontal).

## Ferramentas que aplicam isso automaticamente

Você não precisa decorar as regras — ferramentas fazem isso por você:

- **Formatadores** (ex.: `black`): reescrevem seu código no estilo padrão automaticamente.
- **Linters** (ex.: `ruff`, `flake8`): apontam problemas de estilo e possíveis bugs antes de você rodar o código.

```bash
pip install black
black meu_arquivo.py
```

## Nomes importam mais do que parece

```python
# ruim: não diz nada sobre o que representa
x = 18

# bom: se explica sozinho
idade_minima = 18
```

Um código com bons nomes precisa de menos comentários, porque ele já se explica. Comentários devem responder **"por quê"**, não **"o quê"** — o "o quê" já está no próprio código, se ele for bem escrito.

## DRY: Don't Repeat Yourself

Se você percebe que copiou e colou o mesmo trecho de lógica em dois lugares, é sinal de extrair isso para uma função (visto em [[11-Funcoes]]). Duplicação significa que, ao corrigir um bug, você precisa lembrar de corrigir em todos os lugares — e é fácil esquecer um.

## Testando seu próprio código

Até agora, você testou seus programas rodando e olhando a saída manualmente. Conforme um programa cresce, isso fica inviável. A ideia central de **testes automatizados** é escrever código que verifica automaticamente se outro código está correto:

```python
def somar(a, b):
    return a + b

# Um teste simples, sem nenhuma biblioteca:
assert somar(2, 3) == 5
assert somar(-1, 1) == 0
print("Todos os testes passaram!")
```

`assert` verifica se uma condição é verdadeira; se for falsa, o programa para com um erro `AssertionError`. Bibliotecas como `pytest` formalizam e organizam isso em projetos maiores — veja [[../Programacao-Geral/12-Debugging-e-Testes]].

## Ambientes virtuais (`venv`)

Quando você instala pacotes de terceiros com `pip` (visto em [[12-Modulos-e-Pacotes]]), eles ficam disponíveis globalmente no seu computador por padrão. Isso vira um problema quando projetos diferentes precisam de versões diferentes do mesmo pacote. A solução é um **ambiente virtual**: uma "caixa" isolada de pacotes por projeto.

```bash
python -m venv venv          # cria o ambiente virtual na pasta "venv"
venv\Scripts\activate         # ativa (Windows)
pip install requests          # instala só dentro deste ambiente
```

Todo projeto Python "sério" usa um ambiente virtual próprio — vale criar esse hábito desde já.

## Organizando um projeto maior

Um script único (`.py`) é ótimo para aprender, mas projetos crescem. Um padrão comum:

```
meu_projeto/
├── main.py            # ponto de entrada do programa
├── utilidades.py       # funções auxiliares (ver módulos, [[12-Modulos-e-Pacotes]])
├── testes.py            # testes automatizados
└── requisitos.txt      # lista de pacotes de terceiros usados (pip freeze > requisitos.txt)
```

## Erros como parte do processo

Ler um traceback e não entender de primeira é absolutamente normal, mesmo para quem programa há anos. A diferença entre iniciante e experiente não é "nunca ter erro", é ter mais prática em ler a mensagem, isolar a linha do problema e testar hipóteses pequenas.

## Para onde ir a partir daqui

- Pratique construindo pequenos projetos completos (uma lista de tarefas com arquivo, um jogo de adivinhação, um conversor de unidades) em vez de só exercícios soltos — isso força a combinar tudo que você aprendeu.
- Aprenda `git`, a ferramenta padrão da indústria para guardar o histórico do seu código — veja [[../Programacao-Geral/03-Git-e-Controle-de-Versao]].
- Explore o que existe além de Python puro: como a web funciona, bancos de dados, outras linguagens — a trilha completa está em [[../Programacao-Geral/00-Indice]].
- Aprenda uma segunda linguagem para comparar: o [[../JavaScript/00-Indice|curso de JavaScript do Zero]] segue exatamente o mesmo formato desta trilha, comparando a sintaxe com Python nota a nota.

## Perguntas de revisão

O que é a PEP 8? :: O guia oficial de estilo do Python, com convenções como 4 espaços de indentação e snake_case para variáveis e funções.

Qual a convenção de nome de classes em Python? :: PascalCase, como MinhaClasse.

Qual a diferença entre formatador e linter? :: O formatador (como black) reescreve o código no estilo padrão; o linter (como ruff ou flake8) aponta problemas de estilo e possíveis bugs.

O que significa DRY? :: Don't Repeat Yourself: não duplicar lógica, extraindo trechos repetidos para funções.

Para que serve um ambiente virtual (venv)? :: Isolar os pacotes de cada projeto, evitando conflito de versões entre projetos.

O que faz assert em Python? :: Verifica uma condição e, se for falsa, interrompe com AssertionError; é a base de testes simples.

O que um comentário deve explicar? :: O porquê do código; o quê já deve ficar claro pelos bons nomes.

---
Fim da trilha de Python. Volte ao [[00-Indice|índice do curso de Python]] a qualquer momento, ou siga para o [[../Programacao-Geral/00-Indice|conhecimento geral de programação]].
