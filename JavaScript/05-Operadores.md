---
tags: [javascript, basico]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Operadores

## Aritméticos

```javascript
console.log(10 + 3);   // 13
console.log(10 - 3);   // 7
console.log(10 * 3);   // 30
console.log(10 / 3);   // 3.3333333333333335
console.log(10 % 3);   // 1  -> resto da divisão, igual ao % de Python ([[../Python/05-Operadores]])
console.log(10 ** 2);  // 100 -> potência
```

**Diferença em relação a Python**: JavaScript **não tem** um operador de divisão inteira equivalente ao `//` do Python ([[../Python/05-Operadores]]). Para obter só a parte inteira, usa-se `Math.floor(10 / 3)`.

## Comparação: a pegadinha mais importante desta nota

JavaScript tem **dois** tipos de igualdade — e essa é a diferença de sintaxe mais importante em relação a Python nesta trilha inteira:

```javascript
console.log(5 == "5");     // true  -> compara só o VALOR, convertendo tipos (coerção, [[04-Variaveis-e-Tipos]])
console.log(5 === "5");    // false -> compara valor E tipo, sem converter nada
console.log(5 != "5");     // false
console.log(5 !== "5");    // true
```

**Regra prática, sem exceção**: sempre use `===` e `!==`, nunca `==` e `!=`. O operador de dois sinais de igual herda a mesma coerção automática confusa vista em [[04-Variaveis-e-Tipos]], e é responsável por bugs sutis e difíceis de rastrear. `===` se comporta como o `==` do Python — compara valor e tipo, sem surpresas.

```javascript
console.log(5 > 3);    // true
console.log(5 < 3);    // false
console.log(5 >= 5);   // true
console.log(5 <= 4);   // false
```

## Lógicos

```javascript
let idade = 20;
let temCarteira = true;

console.log(idade >= 18 && temCarteira);   // && = "e", igual ao "and" de Python
console.log(idade >= 18 || temCarteira);    // || = "ou", igual ao "or" de Python
console.log(!temCarteira);                   // ! = "não", igual ao "not" de Python
```

A única mudança em relação a [[../Python/05-Operadores]] é a sintaxe: `and`/`or`/`not` em Python viram `&&`/`||`/`!` em JavaScript.

## Atribuição composta

```javascript
let contador = 10;
contador += 1;   // 11
contador -= 2;   // 9
contador *= 3;   // 27
contador /= 3;   // 9
```

Idêntico ao conceito de [[../Python/05-Operadores]].

## Incremento e decremento: um atalho que Python não tem

```javascript
let x = 5;
x++;   // equivalente a x += 1  -> x agora é 6
x--;   // equivalente a x -= 1  -> x agora é 5
```

Python não tem `++`/`--` de propósito (a equipe da linguagem considerou que isso causa mais confusão do que ganho) — em Python você sempre escreve `x += 1`. Em JavaScript, `++`/`--` são extremamente comuns, principalmente dentro de loops `for` (ver [[08-Lacos-de-Repeticao]]).

## Precedência

Mesma regra de [[../Python/05-Operadores]]: parênteses primeiro, depois potência, depois multiplicação/divisão, depois soma/subtração. Na dúvida, use parênteses explicitamente.

```javascript
let resultado = 2 + 3 * 4;      // 14
let resultado2 = (2 + 3) * 4;   // 20
```

## Exercício

Calcule quantas semanas completas e quantos dias sobram em 100 dias, usando `Math.floor()` e `%` (compare com a solução que você já fez em Python, [[../Python/05-Operadores]]). Depois, escreva uma expressão com `===` que verifique se uma variável `nota` é estritamente igual a `10` (número), e teste o que acontece se `nota` for a string `"10"`.

---
Veja o exemplo em `JavaScript/exemplos/05_operadores.js`. Próxima nota: [[06-Entrada-e-Saida]]
