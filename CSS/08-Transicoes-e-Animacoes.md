---
tags: [css, animacoes, flashcards]
cssclasses: [cerebro-nota, cerebro-css]
---

# Transições e Animações

## Transições: interpolando entre dois estados

Uma **transição** anima a mudança de um valor de propriedade CSS quando ele muda — por exemplo, ao passar o mouse (`:hover`, visto em [[01-Seletores-e-Especificidade]]), em vez do navegador simplesmente "pular" instantaneamente do valor antigo para o novo.

```css
.botao {
    background: blue;
    transition: background 0.3s ease;
}

.botao:hover {
    background: darkblue;   /* a transição faz essa mudança de cor ser suave, não instantânea */
}
```

## Anatomia de `transition`

```css
.elemento {
    transition: propriedade duração timing-function delay;
    transition: background-color 0.3s ease-in-out 0s;
    transition: all 0.2s linear;    /* "all": anima QUALQUER propriedade que mudar (menos preciso, mas simples) */
}
```

- **Propriedade**: qual propriedade CSS animar (`background-color`, `transform`, `opacity`...). Use `all` com moderação — animar só o necessário é mais previsível e mais barato para o navegador processar.
- **Duração**: quanto tempo a transição leva (`0.3s`, `300ms`).
- **Timing function**: como a velocidade varia ao longo da transição — `ease` (padrão, começa rápido e desacelera), `linear` (velocidade constante), `ease-in` (começa devagar), `ease-out` (termina devagar).
- **Delay**: espera antes de começar (opcional).

## Múltiplas propriedades

```css
.card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);       /* "levanta" o card 5px */
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}
```

Esse padrão — elevar levemente e adicionar sombra ao passar o mouse — é extremamente comum em cards de interface moderna.

## `transform`: mover, girar, escalar sem afetar o layout

```css
.mover { transform: translateX(20px); }        /* desloca horizontalmente */
.girar { transform: rotate(45deg); }             /* gira */
.escalar { transform: scale(1.1); }               /* aumenta 10% */
.combinado { transform: translateY(-5px) scale(1.05); }  /* várias transformações juntas */
```

**Por que `transform` é preferível a mudar `top`/`left`/`width` para animações**: `transform` é processado pela GPU do dispositivo, de forma muito mais eficiente, e **não recalcula o layout** da página inteira (diferente de mudar `width` ou `margin`, que obriga o navegador a recalcular a posição de outros elementos ao redor). Para animações suaves, prefira sempre `transform` e `opacity` quando possível.

## `@keyframes`: animações com múltiplos estágios

Transições só interpolam entre **dois** estados (antes/depois). Para animações mais complexas, com vários estágios, ou que rodam **sozinhas** (sem depender de `:hover` ou outra mudança de estado), usa-se `@keyframes`:

```css
@keyframes pulsar {
    0%   { transform: scale(1); }
    50%  { transform: scale(1.1); }
    100% { transform: scale(1); }
}

.notificacao {
    animation: pulsar 1.5s ease-in-out infinite;
}
```

`@keyframes pulsar { ... }` define os estágios (de `0%` a `100%` do tempo total); `animation: pulsar 1.5s ease-in-out infinite;` aplica essa animação a um elemento — `infinite` faz repetir para sempre; um número (`animation-iteration-count: 3`) roda um número fixo de vezes.

## Propriedades de `animation`, separadas

```css
.elemento {
    animation-name: pulsar;
    animation-duration: 1.5s;
    animation-timing-function: ease-in-out;
    animation-iteration-count: infinite;
    animation-delay: 0.5s;
    animation-direction: alternate;   /* alterna ida/volta a cada repetição, em vez de sempre reiniciar do começo */
}
```

## Respeitando quem prefere menos movimento (acessibilidade)

```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation: none !important;
        transition: none !important;
    }
}
```

Alguns usuários configuram o sistema operacional para reduzir animações (por enjoo de movimento, ou preferência pessoal) — `prefers-reduced-motion` permite ao CSS respeitar essa escolha, desligando animações não essenciais para quem ativou essa preferência.

## Exercício

Abra `CSS/exemplos/08_transicoes_animacoes.html`. Crie um botão que muda de cor suavemente e "levanta" levemente ao passar o mouse (`transition` + `transform`). Depois, crie um elemento com uma animação de `@keyframes` que gira infinitamente (`transform: rotate(360deg)` ao longo do tempo).

## Perguntas de revisão

Qual a diferença entre transition e animation com @keyframes? :: transition anima a mudança entre dois estados; @keyframes cria animações com vários estágios que podem rodar sozinhas.

Quais as partes de uma transition? :: Propriedade, duração, função de tempo e atraso, como transition: background 0.3s ease.

Por que animar com transform e opacity? :: Porque são processados pela GPU e não recalculam o layout da página, ao contrário de width ou margin.

O que faz animation-iteration-count: infinite? :: Repete a animação para sempre.

Para que serve prefers-reduced-motion? :: Para desligar animações de quem configurou o sistema para reduzir movimento.

---
Veja o exemplo em `CSS/exemplos/08_transicoes_animacoes.html`. Próxima nota: [[09-Boas-Praticas-e-Proximos-Passos]]
