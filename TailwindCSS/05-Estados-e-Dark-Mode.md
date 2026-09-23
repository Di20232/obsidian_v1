---
tags: [tailwindcss, estados, dark-mode]
cssclasses: [cerebro-nota, cerebro-tailwind]
---

# Estados e Dark Mode

## Modificadores: prefixo de estado antes da classe

O mesmo padrão de prefixo usado para breakpoints ([[04-Layout-Flexbox-Grid-Responsividade]]) se aplica a **estados** do elemento — o equivalente direto às pseudo-classes de [[../CSS/01-Seletores-e-Especificidade]]:

```html
<button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded">
    Passe o mouse aqui
</button>

<input class="border border-gray-300 focus:border-blue-500 focus:outline-none rounded px-3 py-2">

<button class="bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed" disabled>
    Desabilitado
</button>
```

- `hover:` — equivalente a `:hover`.
- `focus:` — equivalente a `:focus`.
- `disabled:` — equivalente a `:disabled`.
- `active:` — enquanto o elemento está sendo clicado.

**A mesma classe base pode ter várias variantes de estado ao mesmo tempo**: `bg-blue-600 hover:bg-blue-700 focus:bg-blue-800` — cada prefixo se aplica de forma independente, sem conflito.

## Combinando breakpoint e estado

```html
<button class="bg-blue-600 md:hover:bg-blue-700">
    Efeito de hover só a partir do breakpoint md
</button>
```

Prefixos podem ser **empilhados** — isso é útil porque hover não faz muito sentido em telas de toque (celular), então é comum restringi-lo a partir de telas maiores, tipicamente usadas com mouse.

## Transições, direto como classe

```html
<button class="bg-blue-600 hover:bg-blue-700 transition-colors duration-300">
    Transição suave de cor
</button>

<div class="hover:scale-105 hover:shadow-lg transition-transform duration-300">
    Cresce levemente ao passar o mouse
</div>
```

`transition-colors`/`transition-transform` + `duration-300` reproduzem exatamente o `transition` de CSS puro visto em [[../CSS/08-Transicoes-e-Animacoes]] — a diferença é, de novo, só a forma de escrever.

## `group`: estilizando um filho baseado no estado do pai

```html
<div class="group border rounded p-4 hover:bg-gray-50">
    <h3 class="text-gray-800">Título do Card</h3>
    <p class="text-gray-500 group-hover:text-gray-700">
        Este texto muda de cor quando o MOUSE PASSA SOBRE O CARD INTEIRO, não sobre o próprio texto
    </p>
</div>
```

`group` na classe do elemento pai, combinado com `group-hover:` em um filho, permite que o **hover do pai** afete o estilo de um filho específico — algo que exigiria um seletor CSS mais elaborado (`.card:hover .texto`) em CSS puro, aqui é direto.

## Dark mode: `dark:`

```html
<div class="bg-white text-gray-900 dark:bg-gray-900 dark:text-white p-6 rounded">
    Este card se adapta ao modo escuro do sistema
</div>
```

`dark:` aplica a classe **só quando o modo escuro está ativo** — por padrão, o Tailwind segue a preferência do sistema operacional/navegador (`prefers-color-scheme`, mencionado em [[../Programacao-Geral/07-HTML-e-CSS]] no contexto de artifacts, e o mesmo mecanismo por trás de temas claro/escuro na web em geral). É possível também controlar manualmente via uma classe `dark` no `<html>`, alternada por JavaScript (conectando com [[../JavaScript/16-DOM-e-Eventos]]), para dar ao usuário um botão de "alternar tema" independente da preferência do sistema.

## Exercício

Abra `TailwindCSS/exemplos/05_estados.html`. Construa um card com `group`/`group-hover` onde o título muda de cor ao passar o mouse sobre o card inteiro. Depois, adicione classes `dark:` a um dos elementos e alterne o modo escuro do seu sistema operacional (ou do navegador) para ver o efeito.

---
Veja o exemplo em `TailwindCSS/exemplos/05_estados.html`. Próxima nota: [[06-Customizando-e-Proximos-Passos]]
