---
tags: [css, layout]
cssclasses: [cerebro-nota, cerebro-css]
---

# Box Model

## Todo elemento HTML é uma caixa

Esse é o conceito mais fundamental de layout em CSS: **todo** elemento — um parágrafo, uma imagem, um botão — é renderizado como uma caixa retangular, composta por quatro camadas, de dentro para fora:

```
┌─────────────────────────────────┐
│           margin                 │  espaço FORA da borda, transparente
│  ┌─────────────────────────────┐ │
│  │          border              │ │  a borda em si
│  │  ┌─────────────────────────┐│ │
│  │  │        padding           ││ │  espaço DENTRO da borda, mesma cor do fundo
│  │  │  ┌─────────────────────┐││ │
│  │  │  │       content        │││ │  o conteúdo em si (texto, imagem)
│  │  │  └─────────────────────┘││ │
│  │  └─────────────────────────┘│ │
│  └─────────────────────────────┘ │
└─────────────────────────────────┘
```

```css
.caixa {
    width: 200px;
    padding: 20px;
    border: 2px solid black;
    margin: 10px;
}
```

## `content-box` vs `border-box`: a pegadinha mais famosa de CSS

Por padrão, `width: 200px` define o tamanho **só do conteúdo** — padding e border são **somados** por cima, aumentando o tamanho final da caixa além dos 200px:

```css
.caixa-padrao {
    box-sizing: content-box;  /* padrão do navegador */
    width: 200px;
    padding: 20px;
    border: 2px solid black;
    /* largura REAL renderizada: 200 + 20+20 (padding) + 2+2 (border) = 244px */
}
```

Isso é extremamente contra-intuitivo — você pede 200px e a caixa ocupa 244px de verdade. A solução, universalmente adotada em CSS moderno:

```css
* {
    box-sizing: border-box;   /* recomendado: aplique isso a TUDO, no início de qualquer projeto */
}

.caixa-border-box {
    box-sizing: border-box;
    width: 200px;
    padding: 20px;
    border: 2px solid black;
    /* largura REAL renderizada: exatamente 200px — padding e border são "descontados" de dentro */
}
```

**Regra prática, sem exceção**: comece todo projeto CSS com `* { box-sizing: border-box; }` — isso faz `width`/`height` significarem "o tamanho final da caixa", que é o que praticamente todo mundo espera intuitivamente.

## Margin: espaço entre caixas

```css
.item {
    margin: 10px;              /* todos os lados */
    margin: 10px 20px;          /* topo/baixo, esquerda/direita */
    margin: 10px 20px 5px 15px; /* topo, direita, baixo, esquerda — sentido horário */
    margin-top: 10px;            /* só um lado específico */
}
```

## Margin collapse: duas margens verticais podem "se fundir"

```css
.a { margin-bottom: 30px; }
.b { margin-top: 20px; }
```

Quando `.a` e `.b` são elementos irmãos empilhados, o espaço real entre eles **não é 30+20=50px** — é o **maior** dos dois valores (30px). Esse comportamento, chamado **margin collapse**, só acontece com margens **verticais** de elementos em fluxo normal (não acontece com Flexbox, visto em [[04-Flexbox]]) — é uma das particularidades mais surpreendentes de CSS para quem está aprendendo.

## Padding: espaço interno

```css
.card {
    padding: 16px;   /* mesma sintaxe de margin, mas empurra o CONTEÚDO para dentro, não afasta outras caixas */
}
```

## `display`: como a caixa se comporta no fluxo da página

```css
.bloco { display: block; }        /* ocupa a largura toda disponível, quebra linha antes/depois (div, p, h1...) */
.linha { display: inline; }        /* só o espaço do próprio conteúdo, não quebra linha (span, a, strong...) */
.hibrido { display: inline-block; } /* não quebra linha, mas aceita width/height/padding como um bloco */
.escondido { display: none; }       /* remove da renderização por completo, como se não existisse */
```

Elementos `block` (como `<div>`) e `inline` (como `<span>`) têm essa diferença de comportamento **por padrão** — `display` permite mudar isso explicitamente.

## Exercício

Abra `CSS/exemplos/02_box_model.html`. Compare visualmente duas caixas com o mesmo `width: 200px`, uma com `box-sizing: content-box` e outra com `border-box`, ambas com `padding: 20px` e `border: 2px solid` — meça a diferença de tamanho final.

---
Veja o exemplo em `CSS/exemplos/02_box_model.html`. Próxima nota: [[03-Cores-Unidades-e-Tipografia]]
