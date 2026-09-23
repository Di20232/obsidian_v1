---
tags: [css, layout, grid, flashcards]
cssclasses: [cerebro-nota, cerebro-css]
---

# Grid

## Flexbox é 1D, Grid é 2D

Flexbox ([[04-Flexbox]]) organiza itens em **uma** direção por vez (linha OU coluna). **Grid** foi desenhado para layouts **bidimensionais** de verdade — controlando linhas **e** colunas ao mesmo tempo, o que o torna a ferramenta certa para o layout geral de uma página inteira (cabeçalho, menu lateral, conteúdo, rodapé), enquanto Flexbox brilha mais em componentes menores (uma barra de navegação, uma lista de cards).

## Ativando: `display: grid`

```css
.container {
    display: grid;
    grid-template-columns: 200px 1fr 1fr;   /* 3 colunas: uma fixa de 200px, duas que dividem o resto */
    grid-template-rows: 80px auto 60px;       /* 3 linhas: cabeçalho, conteúdo (auto), rodapé */
    gap: 16px;
}
```

## A unidade `fr`: a peça mais importante de Grid

`fr` significa "fração do espaço disponível" — é uma unidade que **só existe** em Grid, desenhada especificamente para dividir espaço restante:

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;   /* 3 colunas de largura IGUAL, dividindo 100% do espaço */
    grid-template-columns: 2fr 1fr;        /* a primeira coluna é o DOBRO da largura da segunda */
    grid-template-columns: 200px 1fr;      /* uma coluna fixa, a outra ocupa TODO o espaço restante */
}
```

## `repeat()`: evitando repetir o mesmo valor várias vezes

```css
.galeria {
    display: grid;
    grid-template-columns: repeat(4, 1fr);   /* equivalente a "1fr 1fr 1fr 1fr" */
}
```

## `auto-fit` / `auto-fill` + `minmax`: grids responsivos sem media query

```css
.galeria-responsiva {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
}
```

Isso é um dos truques mais poderosos de CSS moderno: **cria quantas colunas couberem**, cada uma com no mínimo 200px e no máximo dividindo igualmente o espaço (`1fr`) — conforme a tela fica mais estreita, menos colunas cabem, e os itens se reorganizam **automaticamente**, sem precisar escrever uma única media query (aprofundado em [[07-Responsividade]]).

## Posicionando itens explicitamente: `grid-column` e `grid-row`

```css
.item-grande {
    grid-column: 1 / 3;    /* ocupa da linha de grade 1 até a 3 -> atravessa 2 colunas */
    grid-row: 1 / 3;         /* atravessa 2 linhas */
}

.item-atalho {
    grid-column: span 2;    /* atalho: "ocupe 2 colunas a partir daqui", sem contar linhas de grade manualmente */
}
```

Isso permite que um item específico **quebre o padrão** do grid — útil para destacar uma notícia principal maior em um grid de notícias, por exemplo.

## `grid-template-areas`: nomeando o layout visualmente

```css
.pagina {
    display: grid;
    grid-template-columns: 200px 1fr;
    grid-template-rows: 80px 1fr 60px;
    grid-template-areas:
        "cabecalho cabecalho"
        "menu conteudo"
        "rodape rodape";
}

.cabecalho { grid-area: cabecalho; }
.menu { grid-area: menu; }
.conteudo { grid-area: conteudo; }
.rodape { grid-area: rodape; }
```

Essa é, possivelmente, a forma **mais legível** de descrever um layout de página inteira em CSS — o `grid-template-areas` literalmente "desenha" o layout usando texto, e cada elemento HTML só precisa dizer em qual área nomeada ele entra.

## Grid vs. Flexbox: qual usar

- **Layout geral da página** (cabeçalho, menu, conteúdo, rodapé): Grid.
- **Alinhar itens dentro de um componente** (uma barra de botões, um card): Flexbox.
- Nada impede combinar os dois no mesmo projeto — um Grid para o esqueleto da página, com Flexbox dentro de cada área para organizar seu conteúdo interno.

## Exercício

Abra `CSS/exemplos/05_grid.html`. Construa o layout clássico de página (cabeçalho, menu lateral, conteúdo, rodapé) usando `grid-template-areas`. Depois, crie uma galeria de 6 cards usando `repeat(auto-fit, minmax(150px, 1fr))` e redimensione a janela do navegador para ver as colunas se reorganizarem sozinhas.

## Perguntas de revisão

Qual a diferença entre Flexbox e Grid? :: Flexbox é unidimensional (linha ou coluna); Grid é bidimensional, controlando linhas e colunas ao mesmo tempo.

O que significa a unidade fr? :: Uma fração do espaço disponível, existente só no Grid.

Como criar colunas responsivas sem media query? :: Com grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)).

O que faz grid-column: span 2? :: Faz o item ocupar duas colunas a partir da posição dele.

Para que serve grid-template-areas? :: Para desenhar o layout com nomes de áreas em texto e encaixar cada elemento com grid-area.

Quando usar Grid e quando usar Flexbox? :: Grid para o esqueleto da página; Flexbox para alinhar itens dentro de componentes.

---
Veja o exemplo em `CSS/exemplos/05_grid.html`. Próxima nota: [[06-Posicionamento]]
