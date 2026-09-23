---
tags: [javascript, boas-praticas]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Boas Práticas e Próximos Passos

## Você terminou o essencial de JavaScript

As 16 notas anteriores cobrem o que a grande maioria do código JavaScript do mundo real usa: variáveis, decisões, repetição, arrays/objetos, funções, módulos, erros, assincronismo, classes e DOM. Combinado com o [[../Python/00-Indice|curso de Python]], você agora tem duas linguagens de paradigmas de uso diferentes (script/dados de um lado, web interativa do outro) — o que deixa muito mais fácil aprender uma terceira quando precisar (ver [[../Programacao-Geral/06-Paradigmas-e-Panorama-de-Linguagens]]).

## `use strict` e o motivo de existir

```javascript
"use strict";

x = 10;   // ERRO em modo estrito: variável não declarada
```

No topo de um arquivo (ou função), `"use strict"` faz o motor JavaScript ser mais rígido — por exemplo, proíbe criar uma variável sem `let`/`const`/`var` por acidente (o que, sem modo estrito, JavaScript permite silenciosamente, criando uma variável global sem querer). Módulos com `import`/`export` (vistos em [[12-Modulos-e-NPM]]) já ativam modo estrito automaticamente.

## Ferramentas que aplicam estilo automaticamente

Mesma ideia de [[../Python/16-Boas-Praticas-e-Proximos-Passos]], adaptada para o ecossistema JS:

- **Prettier**: formata o código automaticamente em um estilo consistente (equivalente ao `black` de Python).
- **ESLint**: aponta problemas de estilo e possíveis bugs antes de rodar (equivalente ao `ruff`/`flake8`).

```bash
npm install --save-dev prettier eslint
npx prettier --write arquivo.js
```

## Convenções de nome, revisitando

- Variáveis e funções: `camelCase` (`minhaVariavel`) — visto em [[04-Variaveis-e-Tipos]].
- Classes: `PascalCase` (`MinhaClasse`) — visto em [[15-Classes-e-POO]].
- Constantes que nunca mudam de propósito: `MAIUSCULO_COM_UNDERSCORE`, mesma convenção do Python ([[../Python/04-Variaveis-e-Tipos]]).

## `const` por padrão, `let` quando necessário

Já mencionado em [[04-Variaveis-e-Tipos]], mas vale reforçar como hábito: comece toda variável com `const`; só troque para `let` quando o próprio código exigir reatribuição. Isso deixa a intenção clara para quem lê, e evita bugs de reatribuição acidental.

## Sempre `===`, nunca `==`

O erro de estilo mais citado em revisões de código JavaScript ([[05-Operadores]]). Configure o ESLint para reclamar automaticamente se alguém (inclusive você) esquecer.

## Testando seu código

```javascript
function somar(a, b) {
    return a + b;
}

console.assert(somar(2, 3) === 5, "somar(2, 3) deveria ser 5");
console.assert(somar(-1, 1) === 0, "somar(-1, 1) deveria ser 0");
console.log("Testes executados.");
```

`console.assert` é o equivalente simples ao `assert` de Python ([[../Python/16-Boas-Praticas-e-Proximos-Passos]]) — só imprime algo se a condição for **falsa**. Em projetos reais, usa-se uma biblioteca de testes de verdade, como **Jest** ou **Vitest** (`npm install --save-dev vitest`), com uma sintaxe parecida com `pytest` — ver o conceito geral em [[../Programacao-Geral/12-Debugging-e-Testes]].

## Organizando um projeto maior

```
meu-projeto/
├── package.json         # descreve o projeto e suas dependências (ver [[12-Modulos-e-NPM]])
├── index.js               # ponto de entrada
├── utilidades.js           # funções auxiliares
├── testes.js                # testes automatizados
└── node_modules/            # pacotes instalados (nunca versionar no Git — [[../Programacao-Geral/03-Git-e-Controle-de-Versao]])
```

## TypeScript: o próximo passo natural para projetos maiores

Como mencionado em [[../Programacao-Geral/08-JavaScript-Basico]], **TypeScript** adiciona tipagem estática (o eixo visto em [[../Programacao-Geral/06-Paradigmas-e-Panorama-de-Linguagens]]) por cima de JavaScript comum — o mesmo código que você já sabe escrever, com um verificador extra que aponta erros de tipo antes mesmo de rodar. Vale explorar depois de estar confortável com o JavaScript puro desta trilha.

## Para onde ir a partir daqui

- **Pratique com um projeto de página web completo**: uma lista de tarefas interativa usando o DOM ([[16-DOM-e-Eventos]]), guardando os dados no navegador com `localStorage`.
- **Explore frameworks de front-end** (React, Vue, Svelte) — todos são construídos em cima dos conceitos desta trilha (funções, componentes reativos ao estado, eventos); eles ficam muito mais fáceis de aprender já sabendo JavaScript puro.
- **Explore o Node.js como back-end**: frameworks como Express permitem construir APIs (conceito visto em [[../Programacao-Geral/10-Como-a-Web-Funciona]]) inteiramente em JavaScript.
- Volte para [[../Programacao-Geral/00-Indice|o conhecimento geral de programação]] se ainda não tiver visto — muitas das notas de lá (Git, estruturas de dados, SQL, testes) se aplicam igualmente a projetos em JavaScript.

---
Fim da trilha de JavaScript. Volte ao [[00-Indice|índice deste curso]], ao [[../Python/00-Indice|curso de Python]], ou ao [[../Programacao-Geral/00-Indice|conhecimento geral de programação]] a qualquer momento.
