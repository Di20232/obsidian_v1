---
tags: [github, conceito, estoque, dados, flashcards]
cssclasses: [cerebro-nota, cerebro-dados]
verificado_em: 2026-09-15
---
# Previsão simples de reposição

O [[Cerebro/GitHub/contro-vend-public/Fontes/src/forecast.js.md|forecast.js]] estima consumo médio diário e dias até o estoque acabar:

```text
média diária = quantidade vendida na janela / dias da janela
dias restantes = estoque atual / média diária
```

Se a média for zero, o código devolve ausência de previsão. Isso não significa estoque infinito; significa que a janela observada não oferece consumo para fazer essa divisão.

## Exemplo

Venda de 60 unidades em 30 dias → média de 2 por dia. Com 10 unidades disponíveis, a projeção simples é de 5 dias. Se o fornecedor demora 7 dias, esse alerta já merece atenção.

## O que a fórmula não sabe sozinha

- Promoções e sazonalidade alteram a demanda.
- Falta de estoque pode reduzir vendas observadas, escondendo procura real.
- Cancelamentos e devoluções precisam de uma regra consistente na série.
- Produtos novos podem ter poucos dias efetivos de histórico.
- Prazo de entrega e estoque de segurança entram na decisão de compra, mesmo que não estejam na fórmula.

## Como evoluir

Compare a previsão com o consumo real após uma semana. Registre erro e contexto, ajuste a janela por categoria se fizer sentido e apresente a estimativa com sua data. Uma fórmula explicável é um bom início para o pequeno comércio.

[[Cerebro/GitHub/contro-vend-public/01-Arquitetura-e-Aprendizados|Contro Vend]] · [[Cerebro/GitHub/00-Indice|GitHub]]

## Perguntas de revisão

Como calcular os dias até o estoque acabar? :: Estoque atual dividido pela média diária de vendas.

Vendendo 60 unidades em 30 dias com 10 em estoque, em quantos dias acaba? :: Em cerca de 5 dias, com média de 2 por dia.

O que a fórmula simples de reposição não considera sozinha? :: Promoções, sazonalidade, ruptura que esconde demanda, devoluções, produtos novos, prazo do fornecedor e estoque de segurança.

Como melhorar uma previsão simples com o tempo? :: Comparar com o consumo real, registrar o erro e ajustar a janela por categoria.
