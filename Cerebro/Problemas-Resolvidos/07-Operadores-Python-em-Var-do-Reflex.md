---
tags: [problema-resolvido, reflex, python, interface, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Operadores do Python quebram dentro de um Var do Reflex

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · Reflex · tela de **Estoque**, ao marcar em vermelho os itens abaixo do mínimo.

## Sintoma e impacto

A página de estoque **não compilava**. O erro apontava para a condição que decide se um item está com saldo baixo.

## Causa-raiz

O código tentava, dentro de um `rx.foreach`, escrever lógica Python normal:

```python
baixo = item["minimo"] > 0 and item["saldo"] <= item["minimo"]   # QUEBRA
```

No Reflex, os valores dentro de `foreach` são **Var** — referências que viram JavaScript. E aí valem outras regras:

| Construção | Funciona em Var? | Por quê |
|---|---|---|
| `>` `<` `>=` `<=` | ✅ | O Reflex sobrecarrega e gera comparação em JS |
| `and` `or` `not` | ❌ | São palavras-chave do Python; **não podem** ser sobrecarregadas |
| `&` e o pipe | ✅ | Operadores bitwise, esses o Reflex consegue interceptar |
| `if / else` comum | ❌ | Avalia na hora de montar a página, não no navegador |
| `rx.cond(...)` | ✅ | É a forma correta de condicional reativa |

## Duas correções possíveis

**Opção A — operadores que o Reflex entende:**

```python
baixo = (item["minimo"] > 0) & (item["saldo"] <= item["minimo"])
```

**Opção B — calcular em Python de verdade (a escolhida):**

Em vez de espremer lógica no template, o campo passou a ser calculado no *event handler*, onde os dados ainda são dicionários Python comuns:

```python
def carregar(self):
    itens = db.estoque_atual()
    for it in itens:
        it["baixo"] = it["minimo"] > 0 and it["saldo"] <= it["minimo"]
    self.itens = itens
```

A opção B venceu porque mantinha `db.py` intocado e deixou o template só apresentando — sem regra de negócio dentro dele.

## Prevenção

> [!problema] A regra que resolve a família inteira
> **Calcule no estado, apresente no template.** Se você precisa de `and`, `or`, `if` ou `str()` sobre um valor da tela, é sinal de que o cálculo está no lugar errado — mova-o para o event handler, onde você tem Python de verdade.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Tecnologia: [[../Tecnologias/01-Reflex|Reflex]]
- Relacionado: [[06-Selects-Reflex-Nao-Enviam-Valor|str() em Var]]

## Perguntas de revisão

Por que and, or e not não funcionam em Vars do Reflex? :: Porque são palavras-chave do Python e não podem ser sobrecarregadas para virar JavaScript.

Quais operadores funcionam em Vars do Reflex? :: Comparações como > e <=, e os operadores & e | no lugar de and e or.

Como fazer uma condicional reativa no Reflex? :: Com rx.cond, não com if/else comum.

Qual a regra que resolve a família de problemas com Vars? :: Calcular no estado (event handler) e só apresentar no template.
