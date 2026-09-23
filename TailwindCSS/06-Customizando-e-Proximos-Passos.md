---
tags: [tailwindcss, boas-praticas]
cssclasses: [cerebro-nota, cerebro-tailwind]
---

# Customizando e Próximos Passos

## Você terminou o essencial de TailwindCSS

Classes utilitárias fundamentais, layout com Flexbox/Grid, responsividade, estados e dark mode — o suficiente para compor qualquer interface, sabendo exatamente qual propriedade CSS cada classe representa (graças a [[../CSS/00-Indice]]).

## Customizando o tema: `tailwind.config.js`

Diferente do Bootstrap, que exige Sass para customização profunda ([[../Bootstrap/06-Boas-Praticas-e-Proximos-Passos]]), o Tailwind é customizado através de um arquivo de configuração JavaScript, já mencionado em [[02-Instalando-e-Configurando]]:

```javascript
// tailwind.config.js
module.exports = {
    content: ["./src/**/*.{html,js}"],
    theme: {
        extend: {
            colors: {
                marca: "#ff6600",   // cria uma nova cor: bg-marca, text-marca...
            },
            fontFamily: {
                sans: ["Roboto", "sans-serif"],   // muda a fonte padrão de todo o projeto
            },
            spacing: {
                128: "32rem",   // adiciona um novo valor de espaçamento: p-128, w-128...
            },
        },
    },
};
```

`theme.extend` **adiciona** aos valores padrão do Tailwind (sem removê-los); usar `theme` diretamente (sem `extend`) **substitui** os padrões inteiros — geralmente você quer `extend`, para manter a escala padrão e só adicionar o que falta.

## Evitando repetição: extraindo componentes

Quando o mesmo conjunto longo de classes se repete várias vezes (um botão usado em 10 lugares diferentes), o princípio DRY ([[../Programacao-Geral/13-Boas-Praticas-de-Codigo]]) ainda se aplica — a solução mais comum não é escrever CSS customizado, é **extrair um componente** na linguagem/framework que você está usando:

```php
<!-- PHP: um "componente" reaproveitável via include, ver [[../PHP/15-Boas-Praticas-e-Proximos-Passos]] -->
<?php function botao($texto) { ?>
    <button class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded transition-colors">
        <?php echo $texto; ?>
    </button>
<?php } ?>
```

```jsx
// React: um componente de verdade
function Botao({ texto }) {
    return (
        <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded transition-colors">
            {texto}
        </button>
    );
}
```

Em vez de criar uma classe CSS nova para "botão padrão", você reaproveita a **composição de classes** através de um componente de código — mantendo a filosofia utility-first mesmo ao evitar repetição.

## `@apply`: extraindo para CSS quando fizer sentido

```css
.btn-primario {
    @apply bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded transition-colors;
}
```

`@apply` permite agrupar várias classes utilitárias sob um nome de classe CSS tradicional, para os casos em que reaproveitar via componente de código não é prático. É usado com moderação — abusar de `@apply` tende a recriar o mesmo problema que motivou a filosofia utility-first (mencionado em [[01-O-que-e-Tailwind]]) desde o início.

## Plugins oficiais úteis

- `@tailwindcss/forms`: estiliza campos de formulário de forma consistente entre navegadores, sem precisar de classes extras.
- `@tailwindcss/typography`: uma classe `prose` que estiliza automaticamente um bloco de texto longo (títulos, parágrafos, listas), útil para conteúdo vindo de um CMS ou Markdown.

## Bootstrap vs. Tailwind: revisitando a decisão

Depois de terminar as duas trilhas ([[../Bootstrap/00-Indice]] e esta), a escolha entre elas se resume a:
- **Prototipagem rápida, visual "padrão" aceitável**: Bootstrap.
- **Controle total sobre o design, disposto a compor manualmente**: Tailwind.
- **Equipe já experiente com um dos dois**: geralmente vale manter consistência com o que o time já domina.

## Para onde ir a partir daqui

- **Pratique reconstruindo uma interface real** só com Tailwind, sem nenhum CSS customizado — força a fluência com as classes.
- **Configure um projeto real com build** (npm + `tailwind.config.js`), saindo do Play CDN usado nesta trilha.
- Volte para [[../CSS/00-Indice]] sempre que uma classe utilitária não bastar — saber CSS puro é o que torna qualquer framework CSS mais fácil de dominar de verdade, não o contrário.

---
Fim da trilha de TailwindCSS. Volte ao [[00-Indice|índice deste curso]], ao [[../Bootstrap/00-Indice|curso de Bootstrap]] ou ao [[../CSS/00-Indice|curso de CSS avançado]] a qualquer momento.
