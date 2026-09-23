---
tags: [javascript, basico]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Estruturas Condicionais

## Mesma lógica de [[../Python/07-Condicionais]], sintaxe com parênteses e chaves

```javascript
let idade = 20;

if (idade >= 18) {
    console.log("Pode entrar");
}
```

Diferenças de sintaxe em relação ao `if` do Python:
- A condição fica entre **parênteses** `( )`.
- O bloco fica entre **chaves** `{ }`, não depende de indentação (embora você deva indentar por legibilidade, como visto em [[03-Primeiro-Programa]]).
- Não existe `:` no final da linha.

## if / else

```javascript
let idade = 15;

if (idade >= 18) {
    console.log("Pode entrar");
} else {
    console.log("Não pode entrar");
}
```

## if / else if / else

O `elif` do Python vira `else if` (duas palavras) em JavaScript:

```javascript
let nota = 7;

if (nota >= 9) {
    console.log("Conceito A");
} else if (nota >= 7) {
    console.log("Conceito B");
} else if (nota >= 5) {
    console.log("Conceito C");
} else {
    console.log("Reprovado");
}
```

Mesma regra de [[../Python/07-Condicionais]]: o JavaScript testa de cima para baixo e para no primeiro `true` — a ordem das condições importa.

## Operador ternário: um `if`/`else` compacto para expressões

```javascript
let idade = 20;
let status = idade >= 18 ? "adulto" : "menor de idade";
console.log(status);
```

Lê-se: "se `idade >= 18` for verdadeiro, `status` recebe `'adulto'`; senão, recebe `'menor de idade'`". É útil quando o `if`/`else` só serve para **escolher um valor** para uma variável — Python tem um equivalente direto, visto normalmente como `"adulto" if idade >= 18 else "menor de idade"`, mas em JavaScript o operador ternário (`condição ? valorSeVerdadeiro : valorSeFalso`) é muito mais usado no dia a dia.

## `switch`: alternativa ao `if`/`else if` encadeado, quando há muitos casos fixos

Python não tem um equivalente direto e tradicionalmente resolve isso com `if`/`elif` mesmo (ou dicionários). JavaScript tem o `switch`:

```javascript
let diaDaSemana = 3;

switch (diaDaSemana) {
    case 1:
        console.log("Segunda");
        break;
    case 2:
        console.log("Terça");
        break;
    case 3:
        console.log("Quarta");
        break;
    default:
        console.log("Dia inválido");
}
```

**O `break` é essencial**: sem ele, a execução "cai" para o próximo `case` mesmo que ele não bata com o valor (comportamento chamado de "fall-through") — um dos erros mais comuns e sutis de quem começa com `switch`.

## Truthy e falsy: o mesmo conceito de [[../Python/07-Condicionais]], com uma lista diferente

JavaScript também converte qualquer valor para verdadeiro/falso dentro de um `if`. São **falsy**: `false`, `0`, `""` (string vazia), `null`, `undefined`, `NaN`. Todo o resto é **truthy** — inclusive `"0"` (string com o caractere zero) e `[]`/`{}` (array e objeto vazios), que em Python seriam falsy mas em JavaScript **são truthy**. Essa é uma diferença real entre as duas linguagens, não só de sintaxe — vale prestar atenção.

```javascript
let nome = "";
if (nome) {
    console.log(`Olá, ${nome}`);
} else {
    console.log("Nome não informado");
}
```

## Exercício

Escreva um script que receba um número como argumento de linha de comando (`process.argv`, visto em [[06-Entrada-e-Saida]]) e diga se ele é positivo, negativo ou zero, e também se é par ou ímpar. Compare com a solução que você já fez em Python, [[../Python/07-Condicionais]].

---
Veja o exemplo em `JavaScript/exemplos/07_condicionais.js`. Próxima nota: [[08-Lacos-de-Repeticao]]
