---
tags: [bootstrap, setup]
cssclasses: [cerebro-nota, cerebro-bootstrap]
---

# Instalando e Configurando

## Via CDN: a forma mais rápida de começar

Um **CDN** (Content Delivery Network) hospeda os arquivos do Bootstrap prontos, e você só precisa apontar um `<link>`/`<script>` para eles — sem baixar, sem instalar nada:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Projeto</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <h1>Olá, Bootstrap!</h1>
    <button class="btn btn-primary">Botão</button>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

- O `<link>` no `<head>` traz o **CSS** — necessário para qualquer classe visual do Bootstrap (`btn`, `container`, `row`...) funcionar.
- O `<script>` no fim do `<body>` traz o **JavaScript** — necessário só para componentes **interativos** (modais, dropdowns, carrosséis, vistos em [[04-Componentes]]). Se sua página só usa layout e estilo, o `<script>` é dispensável.
- O `<meta name="viewport" ...>` é o mesmo requisito de responsividade já visto em [[../CSS/07-Responsividade]] — obrigatório para o grid do Bootstrap funcionar corretamente em celulares.

## Via npm: para projetos com processo de build

```bash
npm install bootstrap
```

```javascript
// em um projeto com bundler (Vite, Webpack...)
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
```

Mesmo conceito de `npm install` já visto em [[../JavaScript/12-Modulos-e-NPM]] — usado quando o projeto já tem um processo de build (comum em projetos React/Vue), permitindo customizar o Bootstrap via Sass antes de gerar o CSS final (aprofundado em [[06-Boas-Praticas-e-Proximos-Passos]]).

## CDN vs. npm: qual usar

- **CDN**: aprendizado, protótipos, páginas simples sem processo de build — o que esta trilha usa.
- **npm**: projetos reais com um bundler já configurado, especialmente se você planeja customizar cores/fontes do Bootstrap de forma mais profunda.

## Estrutura mínima obrigatória: `container`

```html
<body>
    <div class="container">
        <h1>Conteúdo aqui</h1>
    </div>
</body>
```

`container` é a classe que dá o espaçamento lateral e a largura máxima responsiva ao conteúdo — praticamente toda página Bootstrap começa envolvendo o conteúdo principal em um `container` (ou `container-fluid`, que ocupa 100% da largura, sem limite máximo).

## Exercício

Crie um arquivo `teste.html` com a estrutura básica acima (CDN de CSS e JS, `container`, um `<h1>` e um `btn btn-primary`), e abra no navegador para confirmar que o botão já vem estilizado, sem você ter escrito nenhum CSS.

---
Veja o exemplo em `Bootstrap/exemplos/02_setup.html`. Próxima nota: [[03-Grid-System]]
