---
tags: [javascript, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Variáveis e Tipos de Dados

## O mesmo conceito de [[../Python/04-Variaveis-e-Tipos]]

Uma variável guarda um valor sob um nome, para usar depois. O que muda em JavaScript é que existem **três palavras-chave** diferentes para declarar uma variável, cada uma com uma regra própria — Python não tem esse problema porque só existe uma forma (`nome = valor`).

## `let`, `const` e `var`

```javascript
let idade = 25;       // pode ser reatribuída depois
idade = 26;             // OK

const nome = "Diego";  // NÃO pode ser reatribuída
nome = "Ana";            // ERRO: TypeError: Assignment to constant variable.

var cidade = "São Paulo"; // forma antiga, evite em código novo (motivo abaixo)
```

**Regra prática**: use `const` por padrão; troque para `let` só quando você sabe que vai precisar reatribuir aquela variável depois. Isso comunica intenção — quem lê o código já sabe, só pelo `const`, que aquele valor nunca muda. `var` é a forma original de JavaScript (antes de 2015) e tem um comportamento de escopo mais confuso e propenso a erro — hoje é considerada legada; você vai encontrá-la em código antigo, mas não deve escrevê-la em código novo.

**Diferença chave em relação ao Python**: em Python, `IDADE_MINIMA = 18` (visto em [[../Python/04-Variaveis-e-Tipos]]) é só uma **convenção** de nome — nada impede reatribuir. Em JavaScript, `const` é uma **trava real**, aplicada pela linguagem: tentar reatribuir dá erro de verdade.

## Tipos primitivos

```javascript
let idade = 25;              // number  -> JS não separa int de float, é um tipo só
let altura = 1.78;           // number  -> mesmo tipo do inteiro acima
let nome = "Diego";          // string
let estaEstudando = true;    // boolean
let qualquerCoisa;           // undefined -> declarada, mas sem valor ainda
let semValor = null;         // null -> "vazio" atribuído de propósito
```

**Diferença importante em relação a Python**: Python separa `int` e `float` ([[../Python/04-Variaveis-e-Tipos]]). JavaScript tem um único tipo `number` para qualquer número, inteiro ou decimal.

Verificando o tipo com `typeof` (equivalente ao `type()` do Python):

```javascript
console.log(typeof 25);           // "number"
console.log(typeof "Diego");      // "string"
console.log(typeof true);         // "boolean"
console.log(typeof undefined);    // "undefined"
```

## `undefined` vs. `null`: a distinção que Python não tem

Python tem só `None` para representar "nenhum valor" ([[../Python/13-Tratamento-de-Erros]] menciona o conceito de perto). JavaScript separa em dois:
- **`undefined`**: uma variável existe, mas ainda não recebeu valor nenhum (o estado padrão).
- **`null`**: um valor **deliberadamente vazio**, atribuído por quem escreveu o código, para dizer "isto está vazio de propósito".

## Convenção de nomes: camelCase

Diferente do `snake_case` do Python (`minha_variavel`, visto em [[../Python/04-Variaveis-e-Tipos]]), a convenção de JavaScript é **camelCase**: a primeira palavra minúscula, as seguintes começando com maiúscula, sem underscore:

```javascript
let nomeCompleto = "Diego Souza";   // JS: camelCase
// nome_completo seria o estilo Python, evite em JS
```

## Convertendo tipos (casting)

```javascript
let idadeTexto = "25";
let idadeNumero = Number(idadeTexto);   // string -> number
console.log(idadeNumero + 1);            // 26

let numero = 10;
let numeroTexto = String(numero);        // number -> string
console.log("Tenho " + numeroTexto + " anos");

let outraConversao = parseInt("42px");   // 42 -> lê só a parte numérica inicial
```

## Type coercion: a pegadinha mais famosa de JavaScript

Diferente do Python, que **recusa** somar string com número (visto em [[../Python/04-Variaveis-e-Tipos]]), JavaScript tenta converter automaticamente — o que às vezes ajuda, e às vezes confunde bastante:

```javascript
console.log("5" + 3);     // "53"  -> número é convertido para texto, e concatenado
console.log("5" - 3);     // 2      -> aqui o texto é convertido para número
console.log("5" * "2");   // 10     -> os dois viram número
```

Essa inconsistência (`+` concatena, `-` e `*` convertem) é uma fonte clássica de bugs para quem começa em JS. A defesa é sempre **converter explicitamente** você mesmo (`Number(...)`, `String(...)`) em vez de depender da conversão automática.

## Exercício

Crie variáveis `nome`, `idade` e `cidade` com `const`/`let` apropriados, e exiba uma frase juntando as três com `console.log`. Depois, teste no console do navegador (ou em um arquivo `.js`) o que `"10" + 5` e `"10" - 5` retornam, e explique para si mesmo por que a diferença acontece.

## Perguntas de revisão

Qual a diferença entre let, const e var? :: let permite reatribuir, const não permite reatribuir, e var é a forma antiga com escopo confuso, que não se usa em código novo.

Qual a regra prática para declarar variáveis em JavaScript? :: Usar const por padrão e trocar para let só quando precisar reatribuir.

Quantos tipos numéricos JavaScript tem? :: Um só, number, para inteiros e decimais, diferente de Python que separa int e float.

Qual a diferença entre undefined e null? :: undefined é variável que ainda não recebeu valor; null é um vazio atribuído de propósito.

Qual a convenção de nomes de variáveis em JavaScript? :: camelCase, como nomeCompleto.

Quanto dá "5" + 3 e "5" - 3 em JavaScript? :: "53" e 2: o + concatena convertendo o número em texto, e o - converte o texto em número.

Como evitar bugs de conversão automática de tipos em JavaScript? :: Convertendo explicitamente com Number() e String() em vez de depender da coerção.

---
Veja o exemplo em `JavaScript/exemplos/04_variaveis.js`. Próxima nota: [[05-Operadores]]
