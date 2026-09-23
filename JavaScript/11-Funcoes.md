---
tags: [javascript, basico]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Funções

## Mesmo conceito de [[../Python/11-Funcoes]], com uma sintaxe a mais

JavaScript tem **três formas** comuns de escrever uma função — todas fazem a mesma coisa, mas você vai encontrar as três em código real, então vale reconhecer todas.

### 1. Declaração de função (a mais parecida com Python)

```javascript
function saudacao(nome) {
    console.log(`Olá, ${nome}!`);
}

saudacao("Diego");
```

Mesma estrutura de `def saudacao(nome):` em Python ([[../Python/11-Funcoes]]) — `function` no lugar de `def`, parênteses e chaves no lugar de `:` e indentação.

### 2. Expressão de função

```javascript
const saudacao2 = function(nome) {
    console.log(`Olá, ${nome}!`);
};

saudacao2("Diego");
```

Aqui a função é criada e guardada em uma variável, sem nome próprio (função "anônima"). Funciona de forma parecida, com uma diferença técnica sobre **quando** ela pode ser chamada (só depois dessa linha rodar) que vale conhecer, mas não é crítica agora.

### 3. Arrow function (a forma mais usada em código moderno)

```javascript
const saudacao3 = (nome) => {
    console.log(`Olá, ${nome}!`);
};

saudacao3("Diego");

// Se o corpo é só uma linha que retorna algo, pode simplificar bastante:
const dobro = (numero) => numero * 2;
console.log(dobro(5));   // 10 -> return é implícito quando não há chaves
```

Arrow functions (`=>`) são a forma predominante em JavaScript moderno, especialmente para funções curtas passadas como argumento — você já viu isso em `map`, `filter`, `forEach` na nota [[09-Arrays-e-Objetos]].

## `return`: idêntico em conceito a [[../Python/11-Funcoes]]

```javascript
function somar(a, b) {
    return a + b;
}

let resultado = somar(3, 4);
console.log(resultado);          // 7
console.log(somar(10, 5) * 2);   // 30
```

Mesma regra: assim que `return` executa, a função termina imediatamente.

## Parâmetros com valor padrão

```javascript
function saudacao4(nome, saudacaoInicial = "Olá") {
    console.log(`${saudacaoInicial}, ${nome}!`);
}

saudacao4("Diego");               // "Olá, Diego!"
saudacao4("Diego", "Bom dia");    // "Bom dia, Diego!"
```

Sintaxe quase idêntica ao `saudacao_inicial="Olá"` de Python ([[../Python/11-Funcoes]]).

## Sem argumentos nomeados — o substituto é desestruturar um objeto

Python permite `apresentar(nome="Diego", cidade="São Paulo", idade=25)` fora de ordem, chamado de argumento nomeado ([[../Python/11-Funcoes]]). JavaScript não tem isso nativamente — o padrão equivalente é passar um **objeto único** e "desestruturá-lo" nos parâmetros:

```javascript
function apresentar({ nome, idade, cidade }) {
    console.log(`${nome}, ${idade} anos, de ${cidade}`);
}

apresentar({ cidade: "São Paulo", nome: "Diego", idade: 25 });  // ordem não importa, igual ao objeto
```

## Funções como valores: a base de tudo em JavaScript

Diferente de Python, onde isso existe mas é menos central no dia a dia, em JavaScript **funções são tratadas como qualquer outro valor** — podem ser guardadas em variáveis (você já viu acima), passadas como argumento para outra função, e retornadas por outra função:

```javascript
function executarDuasVezes(funcao) {
    funcao();
    funcao();
}

executarDuasVezes(() => console.log("Executando!"));
```

Isso é a base do que possibilita `array.forEach(item => ...)`, `array.map(item => ...)` (vistos em [[09-Arrays-e-Objetos]]), e todo o modelo de assincronismo que vem em [[14-Assincronismo]].

## Escopo: mesmo conceito de [[../Python/11-Funcoes]]

```javascript
function calcular() {
    let resultado = 10;  // existe só dentro desta função
    return resultado;
}

console.log(calcular());
console.log(resultado);   // ERRO: ReferenceError: resultado is not defined
```

## Exercício

Escreva uma **arrow function** `ehPar` que recebe um número e retorna `true`/`false`. Depois, use um `for...of` (de [[08-Lacos-de-Repeticao]]) para testá-la com os números de 1 a 10.

---
Veja o exemplo em `JavaScript/exemplos/11_funcoes.js`. Próxima nota: [[12-Modulos-e-NPM]]
