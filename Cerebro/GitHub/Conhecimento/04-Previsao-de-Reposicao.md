---
tags: [github, conceito, estoque, dados]
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

