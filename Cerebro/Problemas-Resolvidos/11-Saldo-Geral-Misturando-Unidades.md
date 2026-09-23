---
tags: [problema-resolvido, dados, regra-de-negocio, interface, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Saldo geral somando litros com unidades

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · card **Saldo Geral** do painel.

## Sintoma e impacto

O painel mostrava um número único de saldo somando **tudo**. Como observou o usuário:

> não faz sentido aparecer saldo geral pois tem itens em litros e outros em unidades

Esse número não significava nada. Somar 2,5 litros de tinta com 5 toners dá 7,5 — de quê? O card exibia um total com aparência de informação e conteúdo nulo.

## Causa-raiz

O modelo guardava `quantidade` como um número sem carregar a **unidade** junto. A soma era possível no SQL, então aconteceu — e ninguém perguntou se fazia sentido.

O erro não é de código: é de **modelagem**. Quantidade sem unidade não é uma grandeza, é um número solto.

## Correção aplicada

Separar por unidade em toda apresentação agregada:

- **Painel:** dois indicadores em vez de um — total em litros (tinta) e total em unidades (toner e cartucho);
- **Estoque e Relatórios:** resumo no formato `X L de tinta | Y un em toner/cartucho`;
- **CSV exportado:** ganhou uma coluna **Unidade**, com números em formato brasileiro.

## Prevenção

> [!dados] Regra de modelagem
> **Quantidade sem unidade não é dado, é armadilha.** Sempre que houver mais de uma unidade no mesmo campo, qualquer soma, média ou total precisa agrupar por unidade — ou não existir.
>
> Sinal de alerta: um card de total que some itens de tipos diferentes.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Prática: [[../Praticas/08-Unidades-de-Medida|Unidades de medida como regra de negócio]]
- Mapa: [[../Mapas/02-Mapa-Dados|Mapa de Dados]]

## Perguntas de revisão

Por que um saldo geral somando litros e unidades não faz sentido? :: Porque quantidade sem unidade não é grandeza; somar 2,5 litros com 5 toners não significa nada.

Qual a regra de modelagem sobre unidades? :: Com mais de uma unidade no mesmo campo, toda soma ou média precisa agrupar por unidade, ou não existir.

O erro de somar unidades diferentes é de código ou de modelagem? :: De modelagem: o dado foi guardado sem a unidade junto.
