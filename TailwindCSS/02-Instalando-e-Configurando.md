---
tags: [tailwindcss, setup, flashcards]
cssclasses: [cerebro-nota, cerebro-tailwind]
---

# Instalando e Configurando

> [!warning] Esta nota descreve o Tailwind 3
> O **Tailwind 4** (lançado em janeiro de 2025) mudou a instalação:
> - o CSS de entrada passa a ter só `@import "tailwindcss";`, no lugar das três diretivas `@tailwind`;
> - a personalização vai para o próprio CSS, com `@theme`, em vez do `tailwind.config.js`;
> - os arquivos com classes são detectados automaticamente, sem a lista `content`;
> - o CDN de testes passou a ser o pacote `@tailwindcss/browser`.
>
> Os conceitos (classes utilitárias, breakpoints, estados) continuam iguais. Antes de começar um projeto novo, siga a documentação oficial da versão atual em tailwindcss.com.

## Play CDN: a forma mais rápida de experimentar

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Projeto</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="p-8">
    <h1 class="text-3xl font-bold text-blue-600">Olá, Tailwind!</h1>
</body>
</html>
```

Esse `<script>` carrega o Tailwind e processa **no navegador, em tempo real**, todas as classes usadas na página — sem instalar nada, sem etapa de build. Ótimo para aprender e prototipar (é o que esta trilha usa nos exemplos), mas **não recomendado para produção**: processar CSS no navegador a cada carregamento de página é mais lento, e gera um arquivo muito maior do que o necessário, incluindo suporte a classes que a página nem usa.

## Instalação real: com build, para produção

```bash
npm install -D tailwindcss
npx tailwindcss init
```

Isso cria um arquivo `tailwind.config.js`, onde você diz **quais arquivos escanear** em busca de classes usadas:

```javascript
// tailwind.config.js
module.exports = {
    content: ["./src/**/*.{html,js}"],   // Tailwind escaneia esses arquivos
    theme: { extend: {} },
    plugins: [],
};
```

```css
/* entrada.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```bash
npx tailwindcss -i ./entrada.css -o ./saida.css --watch
```

Esse comando **gera** um arquivo `saida.css` contendo **só** o CSS das classes efetivamente usadas nos arquivos listados em `content` — é assim que o Tailwind evita carregar milhares de classes não utilizadas, resolvendo o problema de peso mencionado em [[01-O-que-e-Tailwind]]. `--watch` mantém o processo rodando, regenerando automaticamente a cada mudança nos arquivos, parecido com o `php -S` "sempre ativo" de [[../PHP/02-Preparando-o-Ambiente]], mas para geração de CSS.

## Frameworks modernos já vêm com Tailwind integrado

Ferramentas como **Vite** (usado com React, Vue) e **Next.js** costumam oferecer configuração de Tailwind praticamente automática ao criar um novo projeto — o processo de build acima já vem embutido no fluxo de desenvolvimento, sem precisar configurar manualmente.

## Extensão de editor recomendada

No VS Code (já configurado em [[../Python/02-Instalando-Python]]), instale a extensão oficial "Tailwind CSS IntelliSense" — ela dá autocompletar das classes e mostra um preview do CSS real por trás de cada uma ao passar o mouse, essencial dado o volume de classes que o Tailwind oferece.

## Play CDN vs. instalação real: qual usar

- **Play CDN**: aprendizado (esta trilha), protótipos rápidos, um `.html` isolado sem processo de build.
- **Instalação real**: qualquer projeto que vá para produção — o ganho de performance de gerar só o CSS necessário é significativo.

## Exercício

Crie um arquivo `teste.html` usando o Play CDN, com um `<h1>` estilizado com `text-3xl font-bold text-blue-600` e um `<p>` com `text-gray-600 mt-2`. Abra no navegador e confirme que os estilos são aplicados instantaneamente, sem nenhum arquivo `.css` separado.

## Perguntas de revisão

Por que o Play CDN do Tailwind não serve para produção? :: Porque processa o CSS no navegador a cada carregamento, é mais lento e maior que o necessário.

Para que serve content no tailwind.config.js (Tailwind 3)? :: Diz quais arquivos o Tailwind escaneia para gerar só o CSS das classes usadas.

O que mudou na configuração do Tailwind 4? :: A configuração passou para o próprio CSS, com @import "tailwindcss" e @theme, e os arquivos são detectados automaticamente.

Que extensão do VS Code ajuda com Tailwind? :: Tailwind CSS IntelliSense, com autocompletar e prévia do CSS de cada classe.

---
Veja o exemplo em `TailwindCSS/exemplos/02_setup.html`. Próxima nota: [[03-Utility-Classes-Fundamentais]]
