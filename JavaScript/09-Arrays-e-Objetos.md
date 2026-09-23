---
tags: [javascript, basico, estruturas-de-dados]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Arrays e Objetos

## O equivalente de [[../Python/09-Listas-Tuplas-Dicionarios]]

JavaScript não separa lista/tupla/dicionário em três tipos distintos como Python — tem **array** (equivalente à lista) e **objeto** (equivalente ao dicionário). Não existe um tipo imutável embutido equivalente direto à tupla (o mais próximo, `Object.freeze()`, é visto mais abaixo).

## Arrays: coleção ordenada

```javascript
let frutas = ["maçã", "banana", "uva"];

console.log(frutas[0]);     // "maçã" -> índice começa em 0, igual Python
console.log(frutas[frutas.length - 1]);  // "uva" -> não existe índice negativo como frutas[-1] em Python puro

frutas.push("pera");         // adiciona no fim (equivalente a .append() em Python)
frutas.pop();                  // remove e devolve o último elemento
frutas.shift();                // remove e devolve o PRIMEIRO elemento
frutas.unshift("abacaxi");    // adiciona no início

console.log(frutas.length);   // tamanho do array (equivalente a len() em Python)
```

**Diferença notável**: Python permite `lista[-1]` para pegar o último item diretamente ([[../Python/09-Listas-Tuplas-Dicionarios]]); JavaScript não tem esse atalho — é preciso usar `frutas[frutas.length - 1]`, ou o método mais recente `frutas.at(-1)`.

## Percorrendo (conecta com [[08-Lacos-de-Repeticao]])

```javascript
for (const fruta of frutas) {
    console.log(fruta);
}

frutas.forEach((fruta, indice) => {
    console.log(indice, fruta);
});
```

`forEach` é um **método** de array que recebe uma função e a executa para cada elemento — o mesmo padrão de "função passada como argumento" mencionado em [[06-Entrada-e-Saida]], aprofundado em [[11-Funcoes]].

## Métodos de array que transformam dados (muito usados no dia a dia)

```javascript
let numeros = [1, 2, 3, 4, 5];

let dobrados = numeros.map(n => n * 2);          // [2, 4, 6, 8, 10] -> transforma cada item
let pares = numeros.filter(n => n % 2 === 0);     // [2, 4]           -> mantém só quem passa no teste
let soma = numeros.reduce((total, n) => total + n, 0);  // 15         -> reduz tudo a um único valor
```

Esses três (`map`, `filter`, `reduce`) são o equivalente funcional de escrever um `for` manual com `if` dentro, como em [[../Python/08-Lacos-de-Repeticao]] — Python tem equivalentes com `map()`, `filter()` e list comprehensions, mas em JavaScript esses métodos de array são o estilo predominante do dia a dia.

## Fatiamento

```javascript
let numeros2 = [10, 20, 30, 40, 50];
console.log(numeros2.slice(1, 3));   // [20, 30] -> mesma lógica do fatiamento de Python, [[../Python/09-Listas-Tuplas-Dicionarios]]
console.log(numeros2.slice(2));       // [30, 40, 50]
```

## Objetos: coleção de pares chave → valor

```javascript
const pessoa = {
    nome: "Diego",
    idade: 25,
    cidade: "São Paulo",
};

console.log(pessoa.nome);        // acesso por . (o mais comum)
console.log(pessoa["nome"]);     // acesso por [] (útil quando a chave vem de uma variável)

pessoa.idade = 26;                // altera um valor existente
pessoa.profissao = "Dev";         // adiciona uma nova chave
```

Equivalente direto ao dicionário de Python ([[../Python/09-Listas-Tuplas-Dicionarios]]) — a diferença de sintaxe é que JavaScript permite acessar com `.chave` além de `["chave"]`, desde que o nome da chave siga as regras de nome de variável.

## Percorrendo um objeto

```javascript
for (const chave in pessoa) {
    console.log(chave, "->", pessoa[chave]);
}

// Ou, de forma mais moderna:
Object.entries(pessoa).forEach(([chave, valor]) => {
    console.log(chave, "->", valor);
});
```

## Verificando se uma chave existe

```javascript
if ("profissao" in pessoa) {
    console.log(pessoa.profissao);
}
```

## `const` com arrays e objetos: uma pegadinha importante

```javascript
const numeros3 = [1, 2, 3];
numeros3.push(4);          // permitido! const impede REATRIBUIR a variável, não alterar o conteúdo
console.log(numeros3);      // [1, 2, 3, 4]

numeros3 = [9, 9, 9];       // ERRO: isso sim é reatribuição, e const não permite
```

`const` trava a **variável** apontar para outra coisa — não trava o **conteúdo** de um array/objeto de ser modificado por dentro. Para de fato travar o conteúdo, existe `Object.freeze(objeto)`, mais raramente usado no dia a dia.

## Arrays de objetos (muito comum na prática)

```javascript
const usuarios = [
    { nome: "Ana", idade: 30 },
    { nome: "Bruno", idade: 22 },
];

for (const usuario of usuarios) {
    console.log(`${usuario.nome} tem ${usuario.idade} anos`);
}
```

Igual mencionado em [[../Python/09-Listas-Tuplas-Dicionarios]]: essa é a forma padrão de representar dados tabulares, e é exatamente o formato que aparece ao consumir uma API (dados JSON, ver [[../Programacao-Geral/10-Como-a-Web-Funciona]]).

## Exercício

Crie um array de objetos representando 3 produtos, cada um com `nome` e `preco`. Use `forEach` para exibir cada um, e use `reduce` para calcular o preço total de todos.

---
Veja o exemplo em `JavaScript/exemplos/09_estruturas.js`. Próxima nota: [[10-Strings]]
