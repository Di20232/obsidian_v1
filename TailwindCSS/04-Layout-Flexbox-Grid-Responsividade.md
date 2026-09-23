---
tags: [tailwindcss, layout, responsividade]
cssclasses: [cerebro-nota, cerebro-tailwind]
---

# Layout: Flexbox, Grid e Responsividade

## Flexbox como classes diretas

```html
<div class="flex justify-between items-center">
    <span>Esquerda</span>
    <span>Direita</span>
</div>

<div class="flex flex-col gap-4">
    <div>Item em coluna</div>
    <div>Item em coluna</div>
</div>
```

Cada classe mapeia direto para uma propriedade de [[../CSS/04-Flexbox]]: `flex` = `display: flex`; `flex-col` = `flex-direction: column`; `justify-between` = `justify-content: space-between`; `items-center` = `align-items: center`; `gap-4` = `gap: 1rem`. Não há tradução a decorar — é literalmente o nome da propriedade CSS, abreviado.

## Grid como classes diretas

```html
<div class="grid grid-cols-3 gap-4">
    <div class="bg-gray-100 p-4">1</div>
    <div class="bg-gray-100 p-4">2</div>
    <div class="bg-gray-100 p-4">3</div>
</div>
```

`grid` = `display: grid`; `grid-cols-3` = `grid-template-columns: repeat(3, minmax(0, 1fr))` — o mesmo conceito de `repeat()` e `fr` visto em [[../CSS/05-Grid]], só que embutido em uma única classe numerada.

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
    <!-- 1 coluna no mobile, 3 a partir do breakpoint md -->
</div>
```

## Responsividade: prefixo de breakpoint antes da classe

```html
<div class="text-sm md:text-base lg:text-lg">
    Texto pequeno no mobile, médio em tablets, grande em desktops
</div>

<div class="flex flex-col md:flex-row">
    Empilhado no mobile, lado a lado a partir de md
</div>
```

Mesma filosofia **mobile-first** discutida em [[../CSS/07-Responsividade]] e em [[../Bootstrap/03-Grid-System]]: a classe **sem prefixo** vale sempre (desde o mobile); `md:`, `lg:` **adicionam** ou **sobrescrevem** o comportamento a partir daquele breakpoint. Os breakpoints padrão do Tailwind:

| Prefixo | Largura mínima |
|---|---|
| (nenhum) | sempre |
| `sm:` | ≥640px |
| `md:` | ≥768px |
| `lg:` | ≥1024px |
| `xl:` | ≥1280px |

Praticamente os mesmos valores usados por Bootstrap ([[../Bootstrap/03-Grid-System]]) e pela convenção geral discutida em [[../CSS/07-Responsividade]] — não é coincidência, é o consenso da indústria sobre tamanhos de dispositivo comuns.

## Posicionamento

```html
<div class="relative">
    <span class="absolute top-0 right-0 bg-red-500 text-white text-xs px-2 rounded">Novo</span>
</div>

<nav class="sticky top-0 bg-white shadow">Barra fixa ao rolar</nav>
```

Mesmas classes diretas para os conceitos de [[../CSS/06-Posicionamento]]: `relative`, `absolute`, `fixed`, `sticky` — sem tradução nenhuma, os nomes são idênticos aos valores da propriedade `position`.

## Espaçamento entre elementos filhos: `space-x`/`space-y`

```html
<div class="flex space-x-4">
    <button class="bg-blue-600 text-white px-4 py-2 rounded">A</button>
    <button class="bg-blue-600 text-white px-4 py-2 rounded">B</button>
</div>
```

`space-x-4` adiciona espaço horizontal **entre** os filhos diretos (mas não antes do primeiro nem depois do último) — uma alternativa ao `gap` quando o elemento pai não é `flex`/`grid`.

## Exercício

Abra `TailwindCSS/exemplos/04_layout.html`. Construa uma navbar com `flex justify-between items-center`, e uma galeria de cards com `grid grid-cols-1 md:grid-cols-3 gap-4`, redimensionando a janela para confirmar a mudança de colunas.

---
Veja o exemplo em `TailwindCSS/exemplos/04_layout.html`. Próxima nota: [[05-Estados-e-Dark-Mode]]
