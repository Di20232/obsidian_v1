---
tags: [bootstrap, utilitarios]
cssclasses: [cerebro-nota, cerebro-bootstrap]
---

# Classes Utilitárias e Responsividade

## O que são classes utilitárias

Diferente dos componentes de [[04-Componentes]] (que já vêm com um visual pronto), **classes utilitárias** aplicam **uma única propriedade CSS** cada — são os "tijolos" que você combina livremente para ajustes finos, sem escrever CSS próprio.

## Espaçamento: margin e padding

```html
<div class="m-3">margin em todos os lados</div>
<div class="mt-3">margin-top</div>
<div class="mb-3">margin-bottom</div>
<div class="ms-3">margin-start (esquerda, ou direita em idiomas RTL)</div>
<div class="me-3">margin-end (direita)</div>
<div class="mx-3">margin horizontal (esquerda + direita)</div>
<div class="my-3">margin vertical (topo + baixo)</div>

<div class="p-3">padding em todos os lados</div>
<div class="pt-3">padding-top</div>
```

A escala vai de `0` a `5` (`m-0` a `m-5`), cada número representando um múltiplo fixo de espaçamento (definido nas variáveis do Bootstrap) — o mesmo espírito das variáveis CSS vistas em [[../CSS/09-Boas-Praticas-e-Proximos-Passos]], só que já prontas e nomeadas por número. `m-auto` centraliza horizontalmente um elemento com largura definida (equivalente a `margin: 0 auto`).

## Cores de texto e fundo

```html
<p class="text-primary">Texto azul (cor primária)</p>
<p class="text-danger">Texto vermelho (perigo)</p>
<p class="text-muted">Texto acinzentado (secundário)</p>

<div class="bg-primary text-white">Fundo azul, texto branco</div>
<div class="bg-light">Fundo cinza claro</div>
```

Mesmo vocabulário de cores semânticas (`primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark`) usado em botões e alertas ([[04-Componentes]]) — consistente em todo o framework.

## Texto: alinhamento e tamanho

```html
<p class="text-center">Centralizado</p>
<p class="text-end">Alinhado à direita</p>
<p class="fw-bold">Negrito</p>
<p class="fst-italic">Itálico</p>
<p class="fs-1">Tamanho de fonte grande (fs-1 a fs-6, do maior ao menor)</p>
```

## Flexbox, direto como classes

```html
<div class="d-flex justify-content-between align-items-center">
    <span>Esquerda</span>
    <span>Direita</span>
</div>
```

`d-flex` = `display: flex`; `justify-content-between`/`align-items-center` = exatamente as mesmas propriedades de [[../CSS/04-Flexbox]], como classe pronta. Reconhecer isso é a chave para usar Bootstrap com confiança: **cada classe utilitária tem um nome direto e prático de uma propriedade CSS real**.

## Visibilidade responsiva: mostrando/escondendo por tamanho de tela

```html
<div class="d-none d-md-block">Só aparece a partir do breakpoint md (tablets e acima)</div>
<div class="d-block d-md-none">Só aparece ABAIXO do breakpoint md (mobile)</div>
```

Mesmo padrão de prefixo por breakpoint já visto no grid ([[03-Grid-System]]) — `d-none` esconde, `d-md-block` reaparece a partir de `md`. Isso substitui a necessidade de escrever `@media` manualmente para esconder/mostrar elementos, como fizemos em [[../CSS/07-Responsividade]].

## Bordas e arredondamento

```html
<div class="border rounded p-3">Caixa com borda e cantos arredondados</div>
<div class="border-0">Sem borda</div>
<div class="rounded-circle" style="width: 50px; height: 50px; background: gray;"></div>
```

## Sombra

```html
<div class="shadow-sm p-3">Sombra sutil</div>
<div class="shadow p-3">Sombra padrão</div>
<div class="shadow-lg p-3">Sombra grande</div>
```

## Por que aprender essas classes vale a pena, além da conveniência

Cada uma delas mapeia **diretamente** para uma propriedade CSS que você já entende de [[../CSS/00-Indice]] — usar Bootstrap bem não é "decorar um monte de nomes mágicos", é reconhecer o CSS por trás de cada classe. Isso também ajuda a saber **quando** uma classe utilitária não é suficiente, e você precisa escrever CSS próprio para algo mais específico.

## Exercício

Abra `Bootstrap/exemplos/05_utilitarios.html`. Construa um cabeçalho usando `d-flex justify-content-between align-items-center`, com um logo à esquerda e um botão à direita, ambos com espaçamento (`p-3`) e uma sombra sutil (`shadow-sm`).

---
Veja o exemplo em `Bootstrap/exemplos/05_utilitarios.html`. Próxima nota: [[06-Boas-Praticas-e-Proximos-Passos]]
