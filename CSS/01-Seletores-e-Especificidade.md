---
tags: [css, seletores, flashcards]
cssclasses: [cerebro-nota, cerebro-css]
---

# Seletores e Especificidade

## Recapitulando o básico

Em [[../Programacao-Geral/07-HTML-e-CSS]], você viu seletor de tag (`h1`), classe (`.destaque`) e id (`#titulo-principal`). Esta nota aprofunda como **combinar** seletores, e o que acontece quando **duas regras diferentes** miram o mesmo elemento.

## Combinadores: mirando elementos pela relação entre eles

```css
/* Descendente: QUALQUER <p> dentro de .card, não importa a profundidade */
.card p {
    color: gray;
}

/* Filho direto: só <p> que é filho IMEDIATO de .card */
.card > p {
    font-weight: bold;
}

/* Irmão adjacente: o <p> logo depois de um <h2>, mesmo nível */
h2 + p {
    margin-top: 0;
}

/* Irmãos gerais: TODO <p> depois de um <h2>, mesmo nível, não só o primeiro */
h2 ~ p {
    color: darkblue;
}
```

O espaço (` `), o `>`, o `+` e o `~` mudam completamente o que é selecionado — esse é o tipo de detalhe que separa "escrever CSS que meio que funciona" de "escrever CSS previsível".

## Pseudo-classes: estilizando **estados**

```css
a:hover { color: red; }         /* enquanto o mouse está sobre o elemento */
input:focus { border-color: blue; }  /* enquanto o campo está selecionado */
li:first-child { font-weight: bold; }  /* o primeiro item de uma lista */
li:last-child { border-bottom: none; }
li:nth-child(2) { background: #eee; }   /* o segundo item, especificamente */
button:disabled { opacity: 0.5; }        /* enquanto o botão está desabilitado */
```

Pseudo-classes (`:algo`) selecionam um elemento baseado em um **estado** ou **posição**, não em uma classe/id que você escreveu no HTML.

## Pseudo-elementos: estilizando uma **parte** do elemento

```css
p::first-letter { font-size: 200%; }     /* só a primeira letra do parágrafo */
p::before { content: "→ "; }              /* insere conteúdo ANTES, sem editar o HTML */
input::placeholder { color: #999; }       /* o texto de exemplo dentro de um campo vazio */
```

`::before`/`::after` com `content` são muito usados para adicionar pequenos elementos visuais (ícones, decorações) sem "sujar" o HTML com `<span>` extras só para estilo.

## Especificidade: o que decide quando duas regras conflitam

```css
p { color: blue; }
.destaque { color: red; }
#titulo { color: green; }
```

Se um elemento é alvo de **mais de uma regra** com a mesma propriedade, o CSS decide qual vence por um sistema de pontuação chamado **especificidade**, do menos para o mais específico:

1. Seletor de tag (`p`) — peso mais baixo.
2. Classe (`.destaque`), pseudo-classe (`:hover`), atributo (`[type="text"]`) — peso médio.
3. Id (`#titulo`) — peso alto.
4. `style="..."` direto no HTML — vence quase tudo.
5. `!important` — ignora a especificidade normal e força a regra a vencer (evite usar; é o último recurso, não uma ferramenta do dia a dia).

```html
<p id="titulo" class="destaque">Qual cor vence?</p>
```

Com as três regras acima, o texto fica **verde** — `#titulo` tem especificidade maior que `.destaque`, que por sua vez vence `p`.

## Quando há empate: a última regra escrita vence

```css
p { color: blue; }
p { color: purple; }   /* mesma especificidade, mas vem depois -> esta vence */
```

Com especificidade igual, o CSS usa a **ordem no arquivo** como critério de desempate — a regra que aparece **depois** vence. Isso explica boa parte dos "por que meu CSS não está aplicando", quando na verdade outra regra, mais abaixo (ou mais específica), está sobrescrevendo silenciosamente.

## Exercício

Abra `CSS/exemplos/01_seletores.html` no navegador. Altere as regras para fazer o segundo item de uma lista ficar com fundo amarelo usando `:nth-child`, e faça todo link dentro de um `<nav>` (mas não fora dele) ficar sublinhado só ao passar o mouse, usando um combinador descendente com `:hover`.

## Perguntas de revisão

Qual a diferença entre .card p e .card > p? :: .card p seleciona qualquer p dentro de .card; .card > p só os filhos diretos.

O que selecionam h2 + p e h2 ~ p? :: h2 + p seleciona o p logo depois do h2; h2 ~ p seleciona todos os p irmãos depois do h2.

Qual a diferença entre pseudo-classe e pseudo-elemento? :: Pseudo-classe (:hover) seleciona por estado ou posição; pseudo-elemento (::before) estiliza uma parte do elemento.

Qual a ordem de especificidade no CSS, do menor para o maior? :: Tag, depois classe/pseudo-classe/atributo, depois id, depois style inline; !important força acima de tudo.

Quem vence quando duas regras têm a mesma especificidade? :: A que aparece por último no código.

Por que evitar !important? :: Porque quebra a cascata e vira um problema crescente; é último recurso, não ferramenta do dia a dia.

---
Veja o exemplo em `CSS/exemplos/01_seletores.html`. Próxima nota: [[02-Box-Model]]
