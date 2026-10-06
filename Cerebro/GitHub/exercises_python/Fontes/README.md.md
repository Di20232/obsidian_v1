---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-python]
source: https://github.com/Di20232/exercises_python/blob/7ff4a840eb4ac382de7e47166414facee981b6f3/README.md
source_commit: 7ff4a840eb4ac382de7e47166414facee981b6f3
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# README.md

Origem: [Di20232/exercises_python](https://github.com/Di20232/exercises_python/blob/7ff4a840eb4ac382de7e47166414facee981b6f3/README.md). Versao consultada: 7ff4a840eb4a.

[[Cerebro/GitHub/exercises_python/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--exercises_python--7ff4a840eb4a.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

# Exercícios da AP1 — duas variações de cada

Refazimento dos 5 exercícios de
[`diego2600612/AP1-python`](https://github.com/diego2600612/AP1-python),
cada um em **duas versões escritas de formas diferentes que imprimem
exatamente a mesma coisa**.

```
.
├── combo_a/              ← estilo orientado a dados
│   ├── ex01.py … ex05.py
├── combo_b/              ← estilo orientado a objetos
│   ├── ex01.py … ex05.py
└── comparar_saidas.py    ← prova que os dois combos dão a mesma saída
```

## Como rodar

Qualquer exercício roda sozinho, sem instalar nada:

```bash
python combo_a/ex03.py
python combo_b/ex03.py
```

Para conferir que as duas versões realmente batem:

```bash
python comparar_saidas.py
```

O script alimenta os dois programas com as mesmas teclas (21 casos, incluindo
entradas inválidas) e mostra um `diff` se alguma linha divergir. Hoje ele
termina com:

```
Todos os 21 casos produziram saidas identicas.
```

## Qual é a diferença entre os combos

Os dois resolvem o mesmo problema; o que muda é **onde a decisão mora**.

| | `combo_a` — orientado a dados | `combo_b` — orientado a objetos |
|---|---|---|
| Estilo | funções + tabelas (tuplas, dicionários) | classes, `dataclass`, `Enum` |
| Regras de decisão | listas de `(condição, resultado)` percorridas em ordem | métodos com `if`/`return` dentro do objeto |
| Saída de texto | lista de linhas montada e impressa de uma vez | métodos que imprimem passo a passo |
| Para mudar uma regra | edita a tabela no topo do arquivo | edita o método da classe |

### Exercício a exercício

| # | Assunto | `combo_a` | `combo_b` |
|---|---|---|---|
| 01 | variáveis, precedência de operadores, f-string | linhas numa tupla, unidas com `join` | classe `Demonstracao` com `@property` |
| 02 | carrinho de compras com valores fixos | dicionário + template com `format_map` | `@dataclass CarrinhoDeCompras` com `__str__` |
| 03 | sistema de compras com recibo | `calcular_compra` devolve dicionário; recibo é lista de linhas | `Compra` calcula em `@property`; `Recibo` só desenha |
| 04 | liberação de entrada por idade e ingresso | tabela `REGRAS` de `(lambda, resultado)` | `Enum Acesso` + `Visitante.classificar()` |
| 05 | sistema escolar (menus e seleção) | tabelas `CLASSIFICACOES`/`SITUACOES` + `executar_menu` genérica | `Aluno`, `Avaliacao`, `Boletim`, `Turma` + classe `Menu` |

No exercício 05 os dois combos mantêm as três versões do original: menu
interativo (1), menu avançado (2) e teste rápido (3).

## O que mudou em relação ao original

As duas variações imprimem **exatamente** o mesmo que os arquivos originais
em `ex01`, `ex02`, `ex04` e `ex05` — conferido linha a linha. Três ajustes:

**1. `ex03` imprimia `R$` duas vezes.** No original, `formatar_real()` já
devolvia o texto com `R$` na frente, e os `print` colocavam outro:

```
Preco unitario:   R$ R$ 35,00      ← original
Preco unitario:   R$ 35,00         ← aqui
```

Aqui `formatar_real()` devolve só o número no padrão brasileiro
(`1.234,50`) e quem imprime coloca o `R$`. Essa é a única diferença de saída
em relação ao original.

**2. `ex03` não depende mais de `locale`.** O original tentava
`locale.setlocale(...)` com `pt_BR.UTF-8` e caía num formato manual quando o
sistema não tinha esse idioma instalado — ou seja, o mesmo programa podia
imprimir diferente em máquinas diferentes. Além disso, o parâmetro `symbol`
de `locale.currency` espera `True`/`False`, não o texto `"R$ "`. A formatação
agora é feita direto no código e dá o mesmo resultado em qualquer máquina.

**3. Todos os arquivos usam `if __name__ == "__main__":`.** Os originais
`ex01`–`ex04` chamavam a função principal assim que o arquivo era lido, o que
impede importar o código de fora. Com a guarda, dá para importar as funções
num teste sem disparar as perguntas de teclado — é assim que o
`comparar_saidas.py` funciona.

O restante do comportamento foi mantido de propósito, inclusive o que dá para
melhorar: `ex03` ainda quebra se você digitar letra no lugar do preço (a
validação em laço existe só no `ex04` e no `ex05`, como no original).
