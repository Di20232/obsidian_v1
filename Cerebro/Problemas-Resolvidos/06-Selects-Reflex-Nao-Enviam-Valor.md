---
tags: [problema-resolvido, reflex, python, interface, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Selects não enviam o valor escolhido no formulário

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · Reflex · componente compartilhado `app_reflex/componentes/selects.py`.

## Sintoma e impacto

Dois sintomas que pareciam separados, mas eram o mesmo defeito:

- **Registrar entrada** não gravava a entrada do produto;
- **Registrar despacho** não aparecia no histórico nem atualizava o estoque.

Os selects de **filial**, **departamento** e **item** mostravam as opções normalmente — mas o valor escolhido nunca chegava ao servidor.

## Causa-raiz

O componente montava o valor de cada opção assim:

```python
value=str(i[campo_valor])     # ERRADO
```

O `i[campo_valor]` é um **Var do Reflex** — uma referência que só vira valor real no navegador, em tempo de execução. Chamar `str()` nele não converte o dado: converte **a referência** em texto. Cada opção passou a carregar literalmente a string:

```
i_rx_state_?.["id"]
```

Todo select enviava esse texto em vez do ID. O formulário chegava ao servidor com um valor sem sentido, e a gravação falhava silenciosamente.

## Correção aplicada

```python
value=i[campo_valor]          # passa o Var direto
```

Como o componente era compartilhado, **uma linha** consertou entrada e despacho de uma vez.

## Prevenção

> [!problema] Regra do Reflex
> **Nunca chame `str()`, `int()` ou f-string em um Var.** Funções nativas do Python operam sobre a referência, não sobre o dado. Entregue o Var direto ao componente e deixe o Reflex resolver no navegador.

Ver a família completa dessa armadilha em [[07-Operadores-Python-em-Var-do-Reflex|operadores Python em Var]].

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Tecnologia: [[../Tecnologias/01-Reflex|Reflex]]
- Relacionado: [[10-Selects-Cinza-com-Texto-Invisivel|O outro problema dos mesmos selects]]

## Perguntas de revisão

Por que chamar str() num Var do Reflex quebra o valor? :: Porque converte a referência em texto, e não o dado, que só existe no navegador.

Qual a correção para selects do Reflex que não enviam o valor? :: Passar o Var direto no value, sem str().

Qual a regra geral para Vars do Reflex? :: Nunca usar str(), int() ou f-string num Var; entregá-lo direto ao componente.
