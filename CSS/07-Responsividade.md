---
tags: [css, responsividade, flashcards]
cssclasses: [cerebro-nota, cerebro-css]
---

# Responsividade

## O problema: uma página, telas de tamanhos muito diferentes

Um celular tem ~360px de largura; um monitor grande pode ter mais de 2000px. **Responsividade** é a prática de fazer o mesmo HTML/CSS se adaptar bem a qualquer tamanho de tela, sem precisar manter páginas separadas para "versão mobile" e "versão desktop".

## O meta viewport: o passo que ninguém pode esquecer

```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

Sem essa linha no `<head>`, navegadores de celular **simulam** uma tela larga (geralmente ~980px) e depois encolhem tudo para caber — resultado: texto minúsculo, ilegível, exigindo zoom manual. Essa meta tag diz "use a largura real do dispositivo, sem simular nada" — é o primeiro requisito, antes de qualquer CSS responsivo funcionar de verdade.

## Media queries: CSS condicional por tamanho de tela

```css
/* Estilo padrão: pensado "mobile first" — o mais simples, para telas pequenas */
.container {
    display: block;
    padding: 10px;
}

/* A partir de 768px de largura (tablets e acima) */
@media (min-width: 768px) {
    .container {
        display: flex;
        padding: 20px;
    }
}

/* A partir de 1200px de largura (desktops grandes) */
@media (min-width: 1200px) {
    .container {
        max-width: 1140px;
        margin: 0 auto;   /* centraliza o conteúdo, com espaço sobrando nas laterais */
    }
}
```

## Mobile-first: por que começar pelo menor, não pelo maior

A convenção moderna (e a usada no exemplo acima) é escrever o **CSS base pensando em telas pequenas**, e usar `@media (min-width: ...)` para **adicionar** complexidade conforme a tela cresce — em vez do caminho inverso (`max-width`, "encolhendo" um layout desktop). Isso tende a gerar CSS mais simples e menos sujeito a sobreposição confusa de regras, porque cada media query só **adiciona**, nunca precisa desfazer o que veio antes.

## Breakpoints comuns (pontos de quebra)

Não existe um padrão universal obrigatório, mas os valores abaixo são amplamente usados como referência (e são os mesmos que o Bootstrap usa, ver [[../Bootstrap/00-Indice]]):

| Nome | Largura mínima | Dispositivo típico |
|---|---|---|
| sm | 576px | celular grande, na horizontal |
| md | 768px | tablet |
| lg | 992px | laptop |
| xl | 1200px | desktop |

## Imagens responsivas

```css
img {
    max-width: 100%;
    height: auto;
}
```

Isso é praticamente obrigatório em qualquer projeto: sem `max-width: 100%`, uma imagem grande **estoura** a largura do container em uma tela pequena, quebrando o layout inteiro.

## Grid e Flexbox já ajudam bastante sozinhos

Como visto em [[05-Grid]], `repeat(auto-fit, minmax(...))` já cria layouts que se adaptam **sem nenhuma media query**. Da mesma forma, `flex-wrap: wrap` ([[04-Flexbox]]) permite que itens quebrem linha naturalmente em telas estreitas. Media queries continuam necessárias para mudanças mais estruturais (esconder um menu lateral inteiro em telas pequenas, por exemplo), mas boa parte da responsividade moderna vem "de graça" com Grid/Flexbox bem usados.

## Escondendo/mostrando elementos por tamanho de tela

```css
.menu-mobile { display: block; }
.menu-desktop { display: none; }

@media (min-width: 768px) {
    .menu-mobile { display: none; }
    .menu-desktop { display: block; }
}
```

Padrão comum para trocar um menu "hambúrguer" (mobile) por uma barra de navegação horizontal completa (desktop).

## Testando responsividade

No navegador, `F12` → ícone de celular/tablet (DevTools em modo responsivo) simula tamanhos de tela diferentes sem precisar de um dispositivo físico — a forma padrão de testar durante o desenvolvimento.

## Exercício

Abra `CSS/exemplos/07_responsividade.html`, redimensione a janela do navegador (ou use o modo responsivo do DevTools) e observe o layout mudando de uma coluna (mobile) para uma grade de 3 colunas (desktop) ao cruzar o breakpoint de 768px.

## Perguntas de revisão

Qual meta tag é obrigatória para responsividade? :: <meta name="viewport" content="width=device-width, initial-scale=1.0">.

O que é mobile-first? :: Escrever o CSS base para telas pequenas e adicionar complexidade com @media (min-width: ...) conforme a tela cresce.

Quais são os breakpoints comuns de referência? :: sm 576px, md 768px, lg 992px e xl 1200px, os mesmos do Bootstrap.

Como impedir que imagens estourem o layout em telas pequenas? :: Com img { max-width: 100%; height: auto; }.

Como testar responsividade sem um celular? :: Pelo modo responsivo das ferramentas de desenvolvedor do navegador (F12).

---
Veja o exemplo em `CSS/exemplos/07_responsividade.html`. Próxima nota: [[08-Transicoes-e-Animacoes]]
