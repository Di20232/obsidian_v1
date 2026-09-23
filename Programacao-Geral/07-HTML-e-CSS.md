---
tags: [programacao, web, html, css]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# HTML e CSS

> Esta nota é um resumo panorâmico. Para uma trilha completa de CSS, do zero, com exemplos executáveis nota a nota — igual ao [[../Python/00-Indice|curso de Python]] — veja [[../CSS/00-Indice|Curso de CSS do Zero (Avançado)]]. Depois dele, [[../Bootstrap/00-Indice|Bootstrap]] e [[../TailwindCSS/00-Indice|TailwindCSS]] são os dois frameworks CSS mais usados na prática.

## O que cada um resolve

Toda página da web que você já visitou é feita, na base, de duas linguagens que trabalham juntas:

- **HTML** (HyperText Markup Language): descreve a **estrutura e o conteúdo** — o que é um título, o que é um parágrafo, o que é uma imagem, o que é um link.
- **CSS** (Cascading Style Sheets): descreve a **aparência** desse conteúdo — cores, tamanhos, espaçamento, posicionamento.

Separar "o que é" (HTML) de "como se parece" (CSS) é uma decisão de design deliberada: o mesmo HTML pode ganhar aparências completamente diferentes trocando só o CSS.

## HTML: a estrutura

```html
<!DOCTYPE html>
<html>
<head>
    <title>Minha Página</title>
</head>
<body>
    <h1>Bem-vindo</h1>
    <p>Este é um parágrafo de texto.</p>
    <a href="https://exemplo.com">Este é um link</a>
    <img src="foto.jpg" alt="Descrição da foto">
</body>
</html>
```

Conceitos-chave:
- **Tag (elemento)**: marcada por `<algo>conteúdo</algo>` — a tag de abertura e a de fechamento (com `/`) envolvem o conteúdo. `<h1>` é título principal, `<p>` é parágrafo, `<a>` é link (âncora), `<img>` é imagem.
- **Atributo**: informação extra dentro da tag de abertura, como `href` (o destino de um link) ou `src` (a origem de uma imagem) e `alt` (texto alternativo, importante para acessibilidade).
- **Hierarquia**: tags ficam dentro de outras tags (`<body>` contém `<h1>` e `<p>`), formando uma **árvore** — o mesmo conceito de árvore visto em [[04-Estruturas-de-Dados]]. Essa árvore é chamada de **DOM** (Document Object Model), e é o que JavaScript manipula para tornar páginas interativas (ver [[08-JavaScript-Basico]]).

## CSS: a aparência

```css
h1 {
    color: blue;
    font-size: 32px;
}

p {
    color: gray;
    line-height: 1.5;
}
```

Um bloco de CSS tem um **seletor** (`h1`, `p` — a qual elemento a regra se aplica) e um conjunto de **propriedades: valor** entre chaves. O exemplo acima diz "todo título `h1` deve ser azul e ter fonte 32px; todo parágrafo `p` deve ser cinza".

Conectando CSS a um HTML:

```html
<head>
    <link rel="stylesheet" href="estilo.css">
</head>
```

## Seletores mais usados

```css
.destaque { color: red; }       /* seleciona por classe: <p class="destaque"> */
#titulo-principal { color: blue; }  /* seleciona por id único: <h1 id="titulo-principal"> */
```

- **Classe** (`class="..."`, selecionada com `.`): pode ser reaproveitada em vários elementos.
- **Id** (`id="..."`, selecionado com `#`): deve ser único na página, usado para um elemento específico.

## Layout: o essencial

Duas propriedades modernas resolvem a maior parte do posicionamento de elementos na tela:

- **Flexbox** (`display: flex`): organiza elementos em uma linha ou coluna, distribuindo espaço entre eles — ótimo para barras de navegação, alinhamento de itens.
- **Grid** (`display: grid`): organiza elementos em uma grade de linhas e colunas — ótimo para layouts de página inteira.

```css
.container {
    display: flex;
    justify-content: space-between;
}
```

## Responsividade

Páginas modernas precisam funcionar em telas de tamanhos muito diferentes (celular, tablet, monitor). Isso é feito com **media queries**, que aplicam CSS diferente dependendo do tamanho da tela:

```css
@media (max-width: 600px) {
    h1 { font-size: 20px; }   /* título menor em telas pequenas */
}
```

## Por que isso importa mesmo se você não vai fazer front-end

Mesmo trabalhando com Python no back-end (ver [[10-Como-a-Web-Funciona]]), é comum precisar ler ou ajustar um HTML/CSS simples — de um e-mail automático, de um relatório gerado, de uma página de administração. Reconhecer a estrutura básica evita depender de outra pessoa para qualquer ajuste pequeno.

## Exercício

Crie um arquivo `pagina.html` com um título, dois parágrafos e um link. Depois crie um arquivo `estilo.css` que deixe o título azul e centralizado, e conecte os dois arquivos. Abra o `pagina.html` no navegador para ver o resultado.

---
Próxima nota: [[08-JavaScript-Basico]]
