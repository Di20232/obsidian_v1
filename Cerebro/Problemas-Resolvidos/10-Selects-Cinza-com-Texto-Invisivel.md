---
tags: [problema-resolvido, interface, css, usabilidade, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Campos cinza e texto invisível ao selecionar

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · telas de **Entrada** e **Despacho** · campos de data, filial, departamento, item, quantidade e número de chamado.

## Sintoma e impacto

Relatado pelo usuário em duas etapas:

1. os campos ficavam **cinza**, destoando dos demais campos brancos do formulário;
2. pior: ao escolher uma opção, o **texto ficava transparente** — a filial estava de fato selecionada, mas o usuário **não conseguia ler qual era**.

Impacto direto de usabilidade: impossível conferir o que se estava prestes a registrar.

## Causa-raiz

Os selects herdavam o estilo padrão do tema do componente em vez de receber cor explícita. Fundo cinza por padrão e cor de texto não definida — que, sobre o fundo claro, resultava em texto praticamente invisível.

É o mesmo tipo de descuido do [[08-Toast-Invisivel-com-Classes-Tailwind|toast invisível]]: o elemento funciona, o dado está certo, mas a apresentação esconde o resultado.

## Correção aplicada

Fundo **branco** e texto **preto** explícitos nos selects, alinhando-os aos demais campos do formulário, e garantindo que o valor escolhido permanecesse legível.

## Prevenção

> [!problema] Regra de contraste
> Todo campo que exibe uma escolha do usuário precisa de **fundo e cor de texto definidos explicitamente**, nunca herdados. E o teste é simples: *depois de selecionar, dá para ler o que foi selecionado?*

Vale checar isso na revisão de qualquer formulário — foi o tipo de defeito que só apareceu porque o usuário usou o sistema de verdade.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Relacionados: [[06-Selects-Reflex-Nao-Enviam-Valor|O outro problema dos mesmos selects]] · [[08-Toast-Invisivel-com-Classes-Tailwind|Toast invisível]]

## Perguntas de revisão

Por que o texto de um select pode ficar invisível depois de escolher? :: Porque herda o estilo do tema sem cor de texto definida, e o texto fica sem contraste com o fundo.

Qual a regra de contraste para campos de formulário? :: Definir fundo e cor de texto explicitamente, e testar se dá para ler o valor escolhido.
