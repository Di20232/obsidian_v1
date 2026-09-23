---
tags: [tailwindcss, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-tailwind]
---

# Utility Classes Fundamentais

## Espaçamento: padding e margin numéricos

```html
<div class="p-4">padding em todos os lados</div>
<div class="px-4">padding horizontal (esquerda + direita)</div>
<div class="py-4">padding vertical (topo + baixo)</div>
<div class="pt-4">só padding-top</div>

<div class="m-4">margin em todos os lados</div>
<div class="mx-auto">margin horizontal automática -> centraliza um elemento com largura definida</div>
```

A escala numérica (`1`, `2`, `4`, `8`...) segue incrementos de `0.25rem` (`p-1` = `0.25rem`, `p-4` = `1rem`, `p-8` = `2rem`) — a mesma unidade `rem` discutida em [[../CSS/03-Cores-Unidades-e-Tipografia]], escolhida deliberadamente pelo Tailwind por escalar bem com preferências de acessibilidade do usuário.

## Cores: nome + intensidade

```html
<p class="text-blue-600">Texto azul, intensidade 600</p>
<div class="bg-red-100">Fundo vermelho bem claro (100)</div>
<div class="bg-red-900">Fundo vermelho bem escuro (900)</div>
```

Cada cor (`blue`, `red`, `green`, `gray`...) vem em uma escala de **intensidade de 50 a 900** (quanto maior o número, mais escuro) — dezenas de tons prontos e consistentes entre si, sem precisar escolher valores de `hex`/`rgb` manualmente como em [[../CSS/03-Cores-Unidades-e-Tipografia]].

## Tipografia

```html
<p class="text-sm">Pequeno</p>
<p class="text-base">Padrão</p>
<p class="text-xl">Grande</p>
<p class="text-3xl">Bem grande (títulos)</p>

<p class="font-normal">Peso normal</p>
<p class="font-semibold">Semi-negrito</p>
<p class="font-bold">Negrito</p>

<p class="text-center">Centralizado</p>
<p class="uppercase">Maiúsculas</p>
<p class="italic">Itálico</p>
<p class="leading-relaxed">Espaçamento de linha relaxado (equivalente a line-height maior)</p>
```

## Bordas e cantos arredondados

```html
<div class="border border-gray-300">Borda cinza clara</div>
<div class="border-2 border-blue-500">Borda mais grossa, azul</div>
<div class="rounded">Cantos levemente arredondados</div>
<div class="rounded-lg">Cantos mais arredondados</div>
<div class="rounded-full">Círculo/pílula completo</div>
```

## Largura, altura e sombra

```html
<div class="w-64">Largura fixa (16rem)</div>
<div class="w-full">Largura 100% do container pai</div>
<div class="h-screen">Altura igual à altura da janela (100vh)</div>

<div class="shadow-sm">Sombra sutil</div>
<div class="shadow-md">Sombra média</div>
<div class="shadow-lg">Sombra grande</div>
```

## Compondo um card completo

```html
<div class="max-w-sm mx-auto p-6 bg-white rounded-lg shadow-md border border-gray-200">
    <h2 class="text-xl font-bold text-gray-800">Título do Card</h2>
    <p class="text-gray-600 mt-2">Algum texto descritivo aqui dentro.</p>
    <button class="mt-4 bg-blue-600 text-white font-semibold py-2 px-4 rounded hover:bg-blue-700">
        Ação
    </button>
</div>
```

Repare: **nenhuma linha de CSS separada foi escrita** — o card inteiro, incluindo o botão com efeito de hover (aprofundado em [[05-Estados-e-Dark-Mode]]), é composto só de classes.

## Exercício

Abra `TailwindCSS/exemplos/03_utilitarios.html`. Construa o card do exemplo acima do zero, e depois modifique as cores, o arredondamento e o espaçamento até chegar em um visual próprio.

## Perguntas de revisão

Qual a escala de espaçamento do Tailwind? :: Incrementos de 0.25rem: p-1 é 0.25rem, p-4 é 1rem e p-8 é 2rem.

Como funcionam as cores do Tailwind? :: Nome da cor com intensidade de 50 a 900, como bg-red-100 (clara) ou bg-red-900 (escura).

Como centralizar um bloco com largura definida no Tailwind? :: Com mx-auto.

O que fazem w-full e h-screen? :: w-full dá 100% da largura do pai; h-screen dá a altura da janela (100vh).

O que faz rounded-full? :: Arredonda por completo, formando círculo ou pílula.

---
Veja o exemplo em `TailwindCSS/exemplos/03_utilitarios.html`. Próxima nota: [[04-Layout-Flexbox-Grid-Responsividade]]
