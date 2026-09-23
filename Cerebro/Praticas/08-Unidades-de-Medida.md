---
tags: [pratica, dados, regra-de-negocio]
cssclasses: [cerebro-nota, cerebro-dados]
---

# Unidade de medida é regra de negócio, não formatação

A lição mais cara do [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] — e a que mais se repete em qualquer sistema de estoque.

## O problema em uma frase

**Quantidade sem unidade não é dado, é armadilha.**

O sistema guardava `quantidade` como um número solto. Como o SQL consegue somar qualquer coluna numérica, o painel somou litros de tinta com unidades de toner e exibiu um total que não significava nada. → [[../Problemas-Resolvidos/11-Saldo-Geral-Misturando-Unidades|caso real]]

## As regras que emergiram

Nenhuma delas estava no pedido original. Todas apareceram conforme o usuário usou o sistema:

| Regra | Detalhe |
|---|---|
| **Unidade decorre do tipo** | Tinta → litros (L), aceita fracionado. Toner e Cartucho → unidades (un), só inteiro |
| **Entrada e saída podem usar unidades diferentes** | Entrada de tinta em **litros**; despacho em **mililitros** |
| **Conversão acontece na borda** | O despacho recebe ml e divide por 1000 **antes de gravar** — o banco guarda sempre litros |
| **Embalagem tem tamanho** | Garrafinha código 544 = 65 ml · código 534 = 120 ml. Escolher a garrafinha debita o equivalente |
| **Alerta por unidade** | Tinta: menos de 1 L. Toner: menos de 5 un |
| **Agregação sempre separada** | Nunca somar unidades diferentes em um mesmo total |

## O padrão que fez isso funcionar

**Um único módulo concentra a regra.** No CTL-TINTA-FL é o `util_unidade.py`, com `unidade_do_tipo`, `numero_br`, `validar_quantidade`, `tipo_por_nome`, `ml_para_litros`, `litros_para_ml` e `formatar_despacho`.

Esse módulo é usado por **estados, páginas e exportação de CSV** — e é isso que garante que as telas não divirjam entre si. Sem ele, cada tela implementaria sua própria conversão, e uma delas estaria errada.

> [!dados] O princípio
> **Guarde sempre na mesma unidade canônica** (aqui: litros). Converta **na borda** — na entrada do usuário e na exibição. Nunca no meio.
>
> Assim o saldo sempre fecha, porque entradas e saídas estão na mesma escala, e a unidade que o usuário vê é uma questão de apresentação.

## Onde a unidade precisa aparecer

Tela de entrada, tela de despacho, saldo do item, tabela de histórico, painel, relatórios e **CSV exportado** — que ganhou uma coluna `Unidade` e números em formato brasileiro (`1,5`).

Um sistema que mostra `5` sem dizer `5 o quê` está pedindo um erro de operação.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Problema: [[../Problemas-Resolvidos/11-Saldo-Geral-Misturando-Unidades|Saldo geral misturando unidades]]
- Mapa: [[../Mapas/02-Mapa-Dados|Mapa de Dados]]
