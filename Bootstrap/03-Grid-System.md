---
tags: [bootstrap, layout]
cssclasses: [cerebro-nota, cerebro-bootstrap]
---

# Grid System

## 12 colunas: a base de todo layout Bootstrap

O grid do Bootstrap divide a largura disponível em **12 colunas** — qualquer layout é construído dizendo quantas dessas 12 colunas cada elemento deve ocupar. Por trás, é Flexbox ([[../CSS/04-Flexbox]]) fazendo o trabalho real; o Bootstrap só te dá classes prontas em vez de você escrever o CSS.

## As três camadas obrigatórias: container, row, col

```html
<div class="container">
    <div class="row">
        <div class="col">Coluna 1</div>
        <div class="col">Coluna 2</div>
        <div class="col">Coluna 3</div>
    </div>
</div>
```

- **`container`** (ou `container-fluid`): a moldura externa, já vista em [[02-Instalando-e-Configurando]].
- **`row`**: uma linha do grid — cria um contexto Flexbox horizontal para as colunas dentro dela.
- **`col`**: uma coluna. Sem número, `col` divide o espaço **igualmente** entre todas as colunas da mesma `row` (3 `col` = cada uma ocupa 1/3).

## Especificando a largura: `col-N`

```html
<div class="row">
    <div class="col-8">Ocupa 8 de 12 colunas (~66%)</div>
    <div class="col-4">Ocupa 4 de 12 colunas (~33%)</div>
</div>
```

`col-8` + `col-4` = 12 — o total deve somar 12 (ou menos, deixando espaço vazio) para caber em uma única linha; se somar mais que 12, o excedente **quebra para a próxima linha** automaticamente.

## Responsivo por padrão: breakpoints no próprio nome da classe

```html
<div class="row">
    <div class="col-12 col-md-6 col-lg-4">
        Ocupa 12/12 (linha inteira) no mobile, 6/12 (metade) em tablets, 4/12 (um terço) em desktops
    </div>
</div>
```

Essa é a característica mais poderosa do grid do Bootstrap: cada breakpoint (`sm`, `md`, `lg`, `xl`, os mesmos valores discutidos em [[../CSS/07-Responsividade]]) tem seu próprio prefixo de classe. `col-md-6` significa "a partir do breakpoint `md` (768px) em diante, ocupe 6 colunas" — **abaixo** disso, cai no valor do breakpoint anterior definido (ou `col-12`, se for o único especificado). Isso substitui escrever `@media` manualmente ([[../CSS/07-Responsividade]]) — o Bootstrap já embutiu as media queries dentro de cada classe.

| Prefixo | Largura mínima |
|---|---|
| (nenhum, ex.: `col-6`) | sempre, desde o mobile |
| `col-sm-6` | ≥576px |
| `col-md-6` | ≥768px |
| `col-lg-6` | ≥992px |
| `col-xl-6` | ≥1200px |

## `gap` (ou `g-*`): espaçamento entre colunas

```html
<div class="row g-3">
    <div class="col-6">Coluna com espaçamento</div>
    <div class="col-6">Coluna com espaçamento</div>
</div>
```

`g-3` adiciona espaço (gutter) entre as colunas e entre linhas — o número (`0` a `5`) corresponde à escala de espaçamento do Bootstrap, aprofundada em [[05-Utilitarios-e-Responsividade]].

## Alinhamento dentro da row: classes de Flexbox do Bootstrap

```html
<div class="row justify-content-center align-items-center" style="height: 200px;">
    <div class="col-4">Centralizado</div>
</div>
```

`justify-content-center` e `align-items-center` são classes do Bootstrap que aplicam diretamente as propriedades Flexbox de mesmo nome vistas em [[../CSS/04-Flexbox]] — reconhecer isso deixa claro que não é "mágica nova", é o CSS que você já sabe, só embrulhado em uma classe pronta.

## Exercício

Abra `Bootstrap/exemplos/03_grid.html`. Crie um layout de 3 cards que ocupam a linha inteira no celular (`col-12`), metade da linha em tablets (`col-md-6`) e um terço em desktops (`col-lg-4`), e redimensione a janela para ver o comportamento.

---
Veja o exemplo em `Bootstrap/exemplos/03_grid.html`. Próxima nota: [[04-Componentes]]
