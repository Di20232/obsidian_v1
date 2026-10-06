---
tags: [tailwindcss, css, indice]
cssclasses: [cerebro-nota, cerebro-tailwind]
---

# Curso de TailwindCSS do Zero

Mesmo formato das outras trilhas. Tailwind é outro framework CSS, como o [[../Bootstrap/00-Indice|Bootstrap]] — mas com uma filosofia praticamente oposta. Onde Bootstrap te dá **componentes prontos** (`btn btn-primary` já é um botão inteiro estilizado), Tailwind te dá **classes utilitárias puras** (uma classe por propriedade CSS) e deixa você compor o visual final combinando-as. Só faz sentido de verdade depois de [[../CSS/00-Indice]], porque cada classe do Tailwind é, literalmente, uma propriedade CSS com outro nome.

> **Nota sobre os exemplos**: os exemplos usam o **Play CDN** do Tailwind 3 (um `<script>` carregado de `cdn.tailwindcss.com` que processa as classes direto no navegador) — nenhuma instalação necessária para abrir e ver funcionando, mas é preciso ter internet; e não é recomendado para produção (motivo explicado em [[02-Instalando-e-Configurando]]).

## Trilha

1. [[01-O-que-e-Tailwind]] — a filosofia utility-first, e como ela difere do Bootstrap
2. [[02-Instalando-e-Configurando]] — Play CDN vs. instalação real com build
3. [[03-Utility-Classes-Fundamentais]] — espaçamento, cor, tipografia, bordas
4. [[04-Layout-Flexbox-Grid-Responsividade]] — Flexbox, Grid e breakpoints em classes
5. [[05-Estados-e-Dark-Mode]] — `hover:`, `focus:`, `dark:` — modificadores de classe
6. [[06-Customizando-e-Proximos-Passos]] — o arquivo de configuração, e como continuar depois deste curso

## Onde isto se conecta

- [[../CSS/00-Indice]] — o CSS puro por trás de cada classe utilitária do Tailwind.
- [[../Bootstrap/00-Indice]] — o outro framework desta sequência, com filosofia oposta; compare depois de terminar as duas trilhas.
- [[../JavaScript/00-Indice]] — Tailwind é extremamente comum em projetos com React/Vue, embora funcione igualmente bem com HTML puro, PHP ([[../PHP/00-Indice]]) etc.
