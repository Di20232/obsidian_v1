---
tags: [javascript, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Laços de Repetição

## `for` clássico: mais explícito que o `for` do Python

O `for` de Python ([[../Python/08-Lacos-de-Repeticao]]) sempre percorre uma sequência (`range`, lista, etc). O `for` "clássico" de JavaScript é mais parecido com o de C ([[../Programacao-Geral/11-C-e-Memoria]]): você controla explicitamente três partes.

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

Desmontando as três partes, separadas por `;`:
1. `let i = 0` — roda **uma vez**, antes de tudo: inicializa a variável de controle.
2. `i < 5` — a **condição**: checada antes de cada repetição; enquanto for `true`, o loop continua.
3. `i++` — roda **depois de cada repetição**: geralmente incrementa a variável de controle.

Isso substitui o `for numero in range(5)` do Python — o `range` fazia isso por trás; aqui você escreve as três partes manualmente.

## `for...of`: percorrer uma coleção (mais parecido com o `for` do Python)

```javascript
let frutas = ["maçã", "banana", "uva"];

for (const fruta of frutas) {
    console.log(fruta);
}
```

Este é o mais parecido com `for fruta in frutas` do Python ([[../Python/08-Lacos-de-Repeticao]]) — percorre diretamente os **valores** de um array (arrays são vistos em detalhe em [[09-Arrays-e-Objetos]]).

## `for...in`: percorrer chaves/índices

```javascript
let pessoa = { nome: "Diego", idade: 25 };

for (const chave in pessoa) {
    console.log(chave, "->", pessoa[chave]);
}
```

Percorre as **chaves** de um objeto (ver [[09-Arrays-e-Objetos]]) — equivalente próximo do `.items()` de um dicionário em Python ([[../Python/09-Listas-Tuplas-Dicionarios]]), embora a sintaxe entregue só a chave, e você acesse o valor com `pessoa[chave]`.

## `while`

Idêntico em conceito ao `while` de Python ([[../Python/08-Lacos-de-Repeticao]]), só muda a sintaxe:

```javascript
let contador = 0;
while (contador < 5) {
    console.log(contador);
    contador++;
}
```

O mesmo risco de **loop infinito** existe se a condição nunca virar `false` — sempre confira que algo dentro do loop caminha em direção a isso.

## `break` e `continue`

Comportamento idêntico ao de [[../Python/08-Lacos-de-Repeticao]]:

```javascript
for (let i = 0; i < 10; i++) {
    if (i === 5) break;       // encerra o loop
    console.log(i);
}

for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) continue; // pula para a próxima repetição
    console.log(i);
}
```

## Loops aninhados

```javascript
for (let linha = 0; linha < 3; linha++) {
    for (let coluna = 0; coluna < 3; coluna++) {
        process.stdout.write(`(${linha}, ${coluna}) `);
    }
    console.log(); // pula linha
}
```

`process.stdout.write` escreve sem quebrar linha automaticamente (diferente de `console.log`) — equivalente ao `print(..., end=" ")` de Python visto em [[../Python/08-Lacos-de-Repeticao]].

## Qual `for` usar

- Precisa do **índice numérico** e controle total sobre o passo? `for` clássico.
- Só quer percorrer os **valores** de um array? `for...of` (o mais comum no dia a dia).
- Precisa das **chaves** de um objeto? `for...in`.
- Depende de uma **condição**, não de uma quantidade fixa? `while`.

## Exercício

Escreva um script que receba um número como argumento (`process.argv`, [[06-Entrada-e-Saida]]) e imprima a tabuada dele de 1 a 10, usando um `for` clássico. Depois, use `for...of` para percorrer um array de 3 nomes e cumprimentar cada um com template string.

## Perguntas de revisão

Quais as três partes do for clássico em JavaScript? :: Inicialização (roda uma vez), condição (checada antes de cada volta) e incremento (roda depois de cada volta).

Qual a diferença entre for...of e for...in? :: for...of percorre os valores de um array; for...in percorre as chaves de um objeto.

Qual laço de JavaScript é mais parecido com o for do Python? :: O for...of.

Como escrever sem quebrar linha no Node.js? :: Com process.stdout.write, equivalente ao print com end no Python.

Quando usar while em vez de for? :: Quando a repetição depende de uma condição, não de uma quantidade fixa.

---
Veja o exemplo em `JavaScript/exemplos/08_lacos.js`. Próxima nota: [[09-Arrays-e-Objetos]]
