---
tags: [javascript, basico]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Tratamento de Erros

## Mesmo problema de [[../Python/13-Tratamento-de-Erros]]

Coisas dão errado em tempo de execução — dados inválidos, arquivos ausentes, respostas de rede que falham. Sem tratamento, isso derruba o programa.

## Vendo o erro acontecer

```javascript
let idade = Number("abc");
console.log(idade);   // NaN -> "Not a Number"
console.log(idade + 1); // NaN -> qualquer operação com NaN vira NaN
```

**Diferença importante em relação a Python**: `int("abc")` em Python **lança um erro** imediatamente ([[../Python/13-Tratamento-de-Erros]]). `Number("abc")` em JavaScript **não lança erro** — devolve um valor especial chamado `NaN`, que silenciosamente contamina qualquer cálculo seguinte. Isso é uma das diferenças de comportamento mais importantes entre as duas linguagens: em JS, você precisa checar `NaN` manualmente, com `Number.isNaN(valor)`.

## `try` / `catch`: capturando erros de verdade

Erros de verdade (não o `NaN` silencioso acima) ainda existem em JavaScript — por exemplo, ao acessar algo de uma forma inválida:

```javascript
try {
    let resultado = JSON.parse("{ isso não é json válido }");
    console.log(resultado);
} catch (erro) {
    console.log("Não foi possível interpretar o JSON:", erro.message);
}
```

Mesma estrutura de [[../Python/13-Tratamento-de-Erros]]: o bloco `try` roda o código arriscado; se algo lançar um erro, a execução pula direto para `catch`, sem derrubar o programa. `erro.message` guarda a descrição do problema.

## `finally`

```javascript
try {
    console.log("Tentando...");
    throw new Error("Algo deu errado");
} catch (erro) {
    console.log("Capturado:", erro.message);
} finally {
    console.log("Isto roda sempre, com erro ou sem erro.");
}
```

Mesmo comportamento do `finally` de Python ([[../Python/13-Tratamento-de-Erros]]) — útil para "limpeza" que deve acontecer independente do resultado.

## Lançando seus próprios erros: `throw`

```javascript
function dividir(a, b) {
    if (b === 0) {
        throw new Error("Não é possível dividir por zero");
    }
    return a / b;
}

try {
    console.log(dividir(10, 0));
} catch (erro) {
    console.log(erro.message);
}
```

`throw new Error("...")` é o equivalente a `raise ValueError("...")` em Python ([[../Python/13-Tratamento-de-Erros]]) — cria e "lança" um erro deliberadamente, para que o código que chamou a função decida como lidar com aquela situação.

## Validando entrada, combinando com `NaN`

Como visto acima, conversão inválida não lança erro sozinha em JS — então a validação, ao lidar com entrada do usuário (ver [[06-Entrada-e-Saida]]), costuma ser manual:

```javascript
let idadeTexto = process.argv[2];
let idade = Number(idadeTexto);

if (Number.isNaN(idade)) {
    console.log("Isso não é um número válido!");
} else {
    console.log(`Idade registrada: ${idade}`);
}
```

## Tipos de erro embutidos (para reconhecer em mensagens)

- `TypeError` — operação em um tipo que não suporta ela (ex.: chamar algo que não é função).
- `ReferenceError` — usar uma variável que não existe (equivalente ao `NameError` de Python).
- `SyntaxError` — código mal formado, geralmente pego antes mesmo de rodar.
- `RangeError` — um valor numérico fora do intervalo esperado (ex.: tamanho de array inválido).

## Exercício

Escreva uma função `dividir(a, b)` que lança um erro (`throw new Error(...)`) se `b` for zero. Chame-a dentro de um `try`/`catch`, testando com um divisor válido e depois com zero, mostrando as duas saídas.

---
Veja o exemplo em `JavaScript/exemplos/13_erros.js`. Próxima nota: [[14-Assincronismo]]
