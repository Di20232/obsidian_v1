---
tags: [css, layout, flexbox]
cssclasses: [cerebro-nota, cerebro-css]
---

# Flexbox

## O problema que Flexbox resolve

Antes de Flexbox, centralizar um elemento verticalmente, ou distribuir itens uniformemente em uma barra de navegação, exigia truques indiretos (tabelas, `float`, posicionamento manual calculado). **Flexbox** foi desenhado especificamente para o problema mais comum de layout: organizar itens **em uma única linha ou coluna**, controlando alinhamento e distribuição de espaço de forma direta.

## Ativando: `display: flex`

```css
.container {
    display: flex;
}
```

Isso já muda o comportamento de **todos os filhos diretos** de `.container` — eles passam a ficar lado a lado, em linha, por padrão.

## O eixo principal e o eixo cruzado

Todo o vocabulário de Flexbox gira em torno de dois eixos:

```css
.container {
    display: flex;
    flex-direction: row;     /* padrão: eixo principal é HORIZONTAL, itens em linha */
    flex-direction: column;   /* eixo principal é VERTICAL, itens em coluna */
}
```

- **Eixo principal** (main axis): a direção em que os itens fluem (`row` = horizontal, `column` = vertical).
- **Eixo cruzado** (cross axis): perpendicular ao principal.

Todas as propriedades de alinhamento abaixo se referem a um desses dois eixos — é o conceito mais importante para não se perder em Flexbox.

## Alinhando no eixo principal: `justify-content`

```css
.container {
    display: flex;
    justify-content: flex-start;    /* padrão: tudo junto no início */
    justify-content: center;         /* tudo centralizado */
    justify-content: flex-end;       /* tudo no final */
    justify-content: space-between;  /* primeiro no início, último no fim, espaço igual entre os demais */
    justify-content: space-around;   /* espaço igual AO REDOR de cada item */
    justify-content: space-evenly;   /* espaço igual entre TODOS, incluindo pontas */
}
```

## Alinhando no eixo cruzado: `align-items`

```css
.container {
    display: flex;
    align-items: stretch;      /* padrão: estica os itens para ocupar toda a altura disponível */
    align-items: center;        /* centraliza no eixo cruzado */
    align-items: flex-start;    /* alinha ao início do eixo cruzado */
    align-items: flex-end;      /* alinha ao final do eixo cruzado */
}
```

**A combinação mais buscada em CSS, resolvida em duas linhas**: centralizar um elemento tanto horizontal quanto verticalmente, historicamente um dos problemas mais repetidos (e piadas) de CSS:

```css
.centralizador {
    display: flex;
    justify-content: center;  /* centraliza no eixo principal */
    align-items: center;       /* centraliza no eixo cruzado */
    height: 100vh;               /* precisa de altura definida para o efeito aparecer */
}
```

## Controlando itens individuais: `flex-grow`, `flex-shrink`, `flex-basis`

```css
.item {
    flex-grow: 1;     /* quanto este item deve "crescer" para ocupar espaço extra, relativo aos irmãos */
    flex-shrink: 1;    /* quanto pode encolher se faltar espaço */
    flex-basis: 200px; /* tamanho "de partida", antes de crescer/encolher */

    flex: 1;            /* atalho comum: equivale a "flex-grow: 1; flex-shrink: 1; flex-basis: 0;" */
}
```

`flex: 1` em todos os itens de um container faz eles dividirem o espaço **igualmente** entre si — um dos padrões mais usados na prática (por exemplo, colunas de largura igual).

## `gap`: espaçamento entre itens, sem margin manual

```css
.container {
    display: flex;
    gap: 16px;   /* espaço entre os itens, sem precisar de margin em cada um */
}
```

`gap` substituiu a necessidade de `margin-right` em todo item exceto o último (um truque antigo, chato de manter) — é a forma moderna e recomendada de espaçar itens dentro de um Flexbox.

## `flex-wrap`: permitindo quebra de linha

```css
.container {
    display: flex;
    flex-wrap: wrap;   /* por padrão, Flexbox tenta espremer tudo em uma linha só; wrap permite quebrar */
}
```

## Exercício

Abra `CSS/exemplos/04_flexbox.html`. Construa uma barra de navegação com um logo à esquerda e 3 links à direita, usando `justify-content: space-between`. Depois, centralize um card (com largura e altura fixas) no meio da tela inteira, combinando `justify-content: center`, `align-items: center` e `height: 100vh`.

---
Veja o exemplo em `CSS/exemplos/04_flexbox.html`. Próxima nota: [[05-Grid]]
