---
tags: [css, tipografia]
cssclasses: [cerebro-nota, cerebro-css]
---

# Cores, Unidades e Tipografia

## Formas de definir cor

```css
.a { color: red; }                  /* nome de cor (limitado, ~150 nomes) */
.b { color: #ff0000; }               /* hexadecimal: RR GG BB, cada par de 00 a ff */
.c { color: #f00; }                   /* hexadecimal curto, quando os pares se repetem */
.d { color: rgb(255, 0, 0); }         /* vermelho, verde, azul: 0 a 255 cada */
.e { color: rgba(255, 0, 0, 0.5); }   /* rgb + alpha (transparência): 0 (invisível) a 1 (opaco) */
.f { color: hsl(0, 100%, 50%); }       /* matiz (0-360), saturação, luminosidade — mais intuitivo para ajustar tons */
```

**Quando usar cada uma**: nomes para protótipos rápidos; `hex` é o mais comum em projetos reais (fácil de copiar de um design); `rgba`/`hsl` quando você precisa de transparência ou quer ajustar luminosidade/saturação de forma previsível (por exemplo, gerar tons mais claros/escuros da mesma cor).

## Unidades de tamanho: absolutas vs. relativas

```css
.absoluta { font-size: 16px; }        /* pixel: tamanho fixo, não escala com nada */

.relativa-pai { font-size: 1.5em; }    /* em: relativo ao font-size do elemento PAI */
.relativa-raiz { font-size: 1.5rem; }  /* rem: relativo ao font-size da RAIZ (<html>), sempre previsível */

.porcentagem { width: 50%; }            /* relativo ao elemento PAI */
.viewport { width: 50vw; height: 50vh; } /* relativo ao tamanho da JANELA do navegador (viewport) */
```

**Por que `rem` é geralmente preferível a `em` para fontes**: `em` composto (elemento dentro de elemento, cada um com seu próprio `em`) pode multiplicar de forma inesperada — um `1.5em` dentro de outro `1.5em` vira `2.25em` do tamanho raiz, e isso escala rápido e fica difícil de prever. `rem` sempre se refere à mesma raiz (`<html>`, cujo `font-size` padrão do navegador é `16px`), então o tamanho final é sempre previsível, não importa o quão aninhado o elemento esteja.

**Por que isso importa para acessibilidade**: se um usuário aumenta o tamanho de fonte padrão do navegador (uma necessidade real de acessibilidade), elementos em `rem`/`em`/`%` escalam junto; elementos em `px` **não** escalam — ficam fixos, ignorando a preferência do usuário. Prefira `rem` para fontes e espaçamentos em projetos reais.

## Tipografia

```css
body {
    font-family: "Segoe UI", Arial, sans-serif;   /* lista de opções, da preferida à última alternativa */
    font-size: 16px;
    font-weight: 400;      /* 400 = normal, 700 = negrito — também aceita "normal"/"bold" */
    line-height: 1.5;       /* espaço entre linhas: 1.5x o tamanho da fonte, sem unidade */
    letter-spacing: 0.02em; /* espaço entre letras */
    text-align: left;        /* left, right, center, justify */
    text-transform: uppercase; /* uppercase, lowercase, capitalize */
}
```

**`font-family` como lista, não um valor único**: se a primeira fonte não estiver instalada no dispositivo de quem visita a página, o navegador tenta a próxima da lista — por isso sempre termine com uma família genérica (`sans-serif`, `serif`, `monospace`), garantindo que sempre haja algo razoável para cair.

## Google Fonts: usando fontes que não vêm no sistema

```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
```

```css
body {
    font-family: "Roboto", sans-serif;
}
```

Isso carrega a fonte de um servidor externo e a disponibiliza para uso — extremamente comum, já que a maioria dos dispositivos não vem com fontes de design "bonitas" pré-instaladas.

## `line-height` sem unidade: por que é a forma recomendada

```css
.bom { line-height: 1.5; }        /* recomendado: escala junto com font-size do próprio elemento */
.evite { line-height: 24px; }      /* fixo: não se ajusta se font-size mudar depois */
```

Um `line-height` sem unidade é um **multiplicador** do `font-size` daquele elemento — se você mudar o tamanho da fonte depois, o espaçamento de linha se ajusta proporcionalmente, sem precisar lembrar de mudar os dois valores juntos.

## Exercício

Abra `CSS/exemplos/03_cores_tipografia.html`. Crie três parágrafos com a mesma cor de fundo, mas escritos em `hex`, `rgb` e `hsl` respectivamente (a mesma cor, três formas diferentes), e confirme visualmente que são idênticos. Depois, experimente aumentar o `font-size` do `<html>` e observe como elementos em `rem` escalam, enquanto os em `px` não mudam.

---
Veja o exemplo em `CSS/exemplos/03_cores_tipografia.html`. Próxima nota: [[04-Flexbox]]
