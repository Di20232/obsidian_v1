---
tags: [javascript, setup]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Preparando o Ambiente

## Duas formas de rodar JavaScript

Diferente de Python, que sempre roda através do mesmo interpretador (visto em [[../Python/02-Instalando-Python]]), JavaScript tem dois ambientes comuns de execução, e vamos usar os dois nesta trilha:

1. **O console do navegador** — sem instalar nada, útil para testar trechos pequenos rapidamente.
2. **O Node.js** — para rodar arquivos `.js` pelo terminal, como você fez com `python arquivo.py`.

## 1. Console do navegador (sem instalação)

Abra qualquer navegador (Chrome, Edge, Firefox), pressione `F12` (ou clique direito → "Inspecionar"), e vá na aba **Console**. Digite:

```javascript
console.log("Olá, mundo!")
```

e pressione Enter. Isso já é JavaScript rodando de verdade, dentro do navegador — ótimo para experimentar algo rápido sem criar arquivo nenhum.

## 2. Instalando o Node.js

Para escrever e rodar arquivos `.js` como programas de verdade (o que faremos na maior parte desta trilha), instale o **Node.js**:

1. Acesse `nodejs.org` e baixe a versão **LTS** (a mais estável, recomendada para a maioria dos casos).
2. Rode o instalador com as opções padrão.
3. Confirme no terminal (o mesmo conceito de terminal visto em [[../Programacao-Geral/02-Terminal-e-Linha-de-Comando]]):

```bash
node --version
```

Se aparecer algo como `v20.x.x`, deu certo. O Node.js também instala automaticamente o **npm** (gerenciador de pacotes, que vamos usar em [[12-Modulos-e-NPM]]):

```bash
npm --version
```

## 3. Editor de código

Se você já configurou o **VS Code** para Python ([[../Python/02-Instalando-Python]]), ótimo — ele já vem com suporte a JavaScript embutido, sem precisar de extensão extra.

## 4. Rodando um arquivo `.js`

Crie um arquivo `ola.js` com:

```javascript
console.log("Olá, mundo!");
```

No terminal, na pasta do arquivo:

```bash
node ola.js
```

Isso é o equivalente direto de `python arquivo.py`.

## Node.js vs. navegador: quando usar qual

- Aprendendo a **lógica da linguagem** (variáveis, loops, funções): tanto faz, mas Node.js pelo terminal é mais parecido com o fluxo que você já usa em Python, então é o que esta trilha vai usar por padrão.
- Testando algo relacionado a **página web** (manipular HTML, reagir a clique): precisa ser no navegador, porque só ele tem o DOM (ver [[16-DOM-e-Eventos]]).

## Erros comuns nesta etapa

- Rodar `node arquivo.js` de dentro da pasta errada → `Error: Cannot find module`. Confira em qual pasta o terminal está (visto em [[../Programacao-Geral/02-Terminal-e-Linha-de-Comando]]).
- Confundir o console do **navegador** com o terminal do **sistema operacional** — são coisas diferentes, cada um roda JS em um contexto diferente.

## Exercício

Rode `node --version` e `npm --version` no terminal para confirmar a instalação. Depois abra o console do navegador e digite `2 + 2`, comparando com o que você fez no modo interativo do Python em [[../Python/02-Instalando-Python]].

---
Próxima nota: [[03-Primeiro-Programa]]
