---
tags: [tailwindcss, css, conceitos]
cssclasses: [cerebro-nota, cerebro-tailwind]
---

# O que é Tailwind

## Utility-first: a filosofia central

Em [[../Bootstrap/01-O-que-e-Bootstrap]], `btn btn-primary` já é um botão inteiro com aparência pronta e definida pelo framework. **Tailwind não tem esse conceito de componente visual pronto** — em vez disso, oferece uma classe para **cada propriedade CSS individual**, e você monta a aparência combinando várias delas diretamente no HTML:

```html
<!-- Bootstrap: um componente pronto -->
<button class="btn btn-primary">Clique aqui</button>

<!-- Tailwind: compõe visualmente, propriedade por propriedade -->
<button class="bg-blue-600 text-white font-semibold py-2 px-4 rounded hover:bg-blue-700">
    Clique aqui
</button>
```

Cada classe do Tailwind corresponde a **uma única regra CSS**: `bg-blue-600` = uma cor de fundo específica; `text-white` = cor do texto; `py-2 px-4` = padding vertical e horizontal; `rounded` = cantos arredondados; `hover:bg-blue-700` = muda a cor de fundo no hover ([[../CSS/01-Seletores-e-Especificidade]]). Nada disso "já vem pronto" como um botão — você o constrói.

## Por que essa abordagem existe

- **Nenhum CSS customizado necessário na maioria dos casos**: em vez de inventar nomes de classe (`.botao-principal`) e escrever CSS separado, você compõe direto no HTML — elimina a etapa de "pensar em nomes" e o vaivém entre arquivo HTML e arquivo CSS.
- **Nada de "cara de Tailwind"**: como não existem componentes visuais padrão (diferente do "cara de Bootstrap" mencionado em [[../Bootstrap/01-O-que-e-Bootstrap]]), dois sites em Tailwind podem parecer completamente diferentes entre si — a aparência final é 100% definida por você.
- **Sem CSS não utilizado**: ferramentas de build do Tailwind (ver [[02-Instalando-e-Configurando]]) escaneiam seu HTML e geram **só** o CSS das classes que você realmente usou — o oposto de carregar um framework inteiro "por via das dúvidas".

## A desvantagem mais discutida: HTML "carregado" de classes

```html
<div class="flex flex-col md:flex-row items-center justify-between gap-4 p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
```

Uma linha de HTML pode acumular dezenas de classes — isso é visualmente "poluído" para quem não está acostumado, e é a crítica mais comum ao Tailwind. A defesa da comunidade Tailwind é que essa "poluição" é, na prática, mais fácil de manter do que caçar regras espalhadas em arquivos `.css` separados — depois de acostumado, ler as classes de uma linha já diz exatamente como aquele elemento se parece, sem precisar pular entre arquivos.

## Comparando Bootstrap e Tailwind lado a lado

| | Bootstrap | Tailwind |
|---|---|---|
| Unidade de trabalho | componente pronto | propriedade CSS individual |
| Visual "de fábrica" | reconhecível, consistente | nenhum — você define tudo |
| Curva de entrada | mais rápida para prototipar | exige saber CSS bem para compor |
| Customização profunda | mais trabalhosa (Sass, ver [[../Bootstrap/06-Boas-Praticas-e-Proximos-Passos]]) | nativa — você já compõe do zero |
| HTML resultante | mais limpo | mais denso de classes |

## Exercício

Sem escrever código ainda: olhe de novo o exemplo de botão Bootstrap (`btn btn-primary`) e o de Tailwind (`bg-blue-600 text-white...`) acima, e liste, propriedade por propriedade, o que cada classe do Tailwind está fazendo — isso já é o essencial da mentalidade "utility-first".

---
Próxima nota: [[02-Instalando-e-Configurando]]
