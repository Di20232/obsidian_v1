---
tags: [github, python, exercicios, testes, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
source: https://github.com/Di20232/exercises_python
source_commit: 7ff4a840eb4ac382de7e47166414facee981b6f3
verificado_em: 2026-09-15
---
# Exercícios Python — duas formas de resolver o mesmo problema

O repositório contém cinco exercícios em duas versões: `combo_a`, com funções e tabelas de decisão, e `combo_b`, com classes, propriedades, dataclasses e enums. O objetivo documentado é manter saídas equivalentes.

## Ordem de estudo

| Exercício | Tema | Compare |
|---|---|---|
| 01 | Variáveis, operadores e formatação | [[Cerebro/GitHub/exercises_python/Fontes/combo_a/ex01.py.md|Funções/dados]] · [[Cerebro/GitHub/exercises_python/Fontes/combo_b/ex01.py.md|Objetos]] |
| 02 | Carrinho de compras | [[Cerebro/GitHub/exercises_python/Fontes/combo_a/ex02.py.md|Dicionário]] · [[Cerebro/GitHub/exercises_python/Fontes/combo_b/ex02.py.md|Dataclass]] |
| 03 | Compra e recibo | [[Cerebro/GitHub/exercises_python/Fontes/combo_a/ex03.py.md|Cálculo/linhas]] · [[Cerebro/GitHub/exercises_python/Fontes/combo_b/ex03.py.md|Compra/Recibo]] |
| 04 | Regras de acesso | [[Cerebro/GitHub/exercises_python/Fontes/combo_a/ex04.py.md|Tabela de regras]] · [[Cerebro/GitHub/exercises_python/Fontes/combo_b/ex04.py.md|Enum e método]] |
| 05 | Sistema escolar e menus | [[Cerebro/GitHub/exercises_python/Fontes/combo_a/ex05.py.md|Menus por dados]] · [[Cerebro/GitHub/exercises_python/Fontes/combo_b/ex05.py.md|Classes escolares]] |

## Três aprendizados registrados pelo autor

1. **Responsabilidade de formatação:** o problema de `R$ R$` foi tratado fazendo a função devolver apenas o número e deixando o recibo acrescentar a moeda.
2. **Portabilidade:** formatação explícita evita depender da disponibilidade do locale brasileiro na máquina.
3. **Código importável:** `if __name__ == "__main__":` impede que perguntas de teclado executem ao importar funções em um teste.

## Prática proposta

Escolha um exercício e explique onde fica a decisão em cada versão. Adicione um caso de teste que expresse uma regra de negócio. Mantenha os dois programas equivalentes para esse caso.

O [[Cerebro/GitHub/exercises_python/Fontes/comparar_saidas.py.md|comparador]] contém cenários de entrada e compara resultados. O README registra 21 casos iguais; essa é uma declaração do repositório, não uma execução feita nesta importação.

Limitação declarada: o exercício 03 ainda aceita conversões numéricas que podem falhar quando a entrada é texto. É um bom próximo exercício de validação.

[[Cerebro/GitHub/exercises_python/Fontes/README.md.md|README e atribuição ao projeto original]] · [[Python/00-Indice|Trilha de Python]] · [[Cerebro/GitHub/00-Indice|GitHub]]

> [!problema] Não confundir com os exercícios do professor
> O cofre também documenta [[Cerebro/Projetos/08-Exercicios-IMP|Exercícios IMP]] — outro conjunto de exercícios em Python, clonado de `profedsonvieira/AlgoritmosExercicios`, com push ainda bloqueado por conta Git errada. É um projeto diferente: exercícios diferentes, sem relação de commit ou branch com este repositório.

## Perguntas de revisão

Como o repositório exercises_python resolve cada exercício? :: Duas vezes: combo_a com funções e tabelas de decisão, combo_b com classes, dataclasses e enums, mantendo saídas equivalentes.

Como foi resolvido o problema de aparecer R$ R$ no recibo? :: A função passou a devolver só o número, e o recibo acrescenta a moeda.

Para que serve if __name__ == "__main__": em Python? :: Impede que o código principal, como perguntas de teclado, rode quando o arquivo é importado, por exemplo num teste.

Por que formatar números explicitamente em vez de usar o locale? :: Para não depender da disponibilidade do locale brasileiro na máquina.
