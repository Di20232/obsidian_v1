---
tags: [php, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-php]
---

# Laços de Repetição

## `for` clássico, igual JavaScript

```php
<?php
for ($i = 0; $i < 5; $i++) {
    echo $i . "\n";
}
```

Mesma estrutura de três partes vista em [[../JavaScript/08-Lacos-de-Repeticao]]: inicialização, condição, incremento — só muda o `$` na frente da variável.

## `foreach`: o equivalente do `for...of` de JavaScript / `for` de Python

```php
$frutas = ["maçã", "banana", "uva"];

foreach ($frutas as $fruta) {
    echo $fruta . "\n";
}

// Com índice
foreach ($frutas as $indice => $fruta) {
    echo "$indice: $fruta\n";
}
```

`foreach` é a forma **mais usada** para percorrer arrays em PHP — equivalente direto ao `for fruta in frutas` de Python ([[../Python/08-Lacos-de-Repeticao]]) e ao `for...of` de JavaScript ([[../JavaScript/08-Lacos-de-Repeticao]]). Como arrays em PHP também servem de dicionário (ver [[08-Arrays]]), `foreach ($array as $chave => $valor)` funciona tanto para índices numéricos quanto para chaves nomeadas:

```php
$pessoa = ["nome" => "Diego", "idade" => 25];

foreach ($pessoa as $chave => $valor) {
    echo "$chave -> $valor\n";
}
```

## `while`

```php
$contador = 0;
while ($contador < 5) {
    echo $contador . "\n";
    $contador++;
}
```

Idêntico em conceito a [[../Python/08-Lacos-de-Repeticao]] e [[../JavaScript/08-Lacos-de-Repeticao]] — mesmo risco de loop infinito se a condição nunca virar falsa.

## `do...while`: garante rodar pelo menos uma vez

```php
$numero = 10;
do {
    echo $numero . "\n";
    $numero++;
} while ($numero < 5);   // a condição é falsa desde o início...
// ...mas "10" ainda é impresso uma vez, porque o corpo roda ANTES de checar a condição
```

Diferente do `while` normal (que checa a condição **antes** de rodar o bloco), `do...while` checa **depois** — garantindo que o bloco rode ao menos uma vez, mesmo que a condição já comece falsa. Python não tem um equivalente direto para isso; JavaScript tem a mesma estrutura (`do { } while (...)`), com o mesmo comportamento.

## `break` e `continue`

Idênticos em comportamento aos já vistos em [[../Python/08-Lacos-de-Repeticao]] e [[../JavaScript/08-Lacos-de-Repeticao]]:

```php
for ($i = 0; $i < 10; $i++) {
    if ($i === 5) break;
    echo $i . "\n";
}

for ($i = 0; $i < 10; $i++) {
    if ($i % 2 === 0) continue;
    echo $i . "\n";
}
```

## Exercício

Escreva um script que exiba a tabuada de um número fixo (por exemplo, `$numero = 7;`) de 1 a 10, usando `for`. Depois, use `foreach` para percorrer um array associativo (visto em [[08-Arrays]]) com 3 produtos e preços, exibindo cada um.

## Perguntas de revisão

Qual o laço mais usado para percorrer arrays em PHP? :: foreach, como foreach ($frutas as $fruta).

Como percorrer chave e valor num foreach? :: foreach ($array as $chave => $valor).

Qual a diferença entre while e do...while? :: while testa antes de rodar; do...while roda o bloco pelo menos uma vez e testa depois.

O for clássico do PHP é igual ao de qual linguagem? :: Ao do JavaScript, com inicialização, condição e incremento, só que com $ nas variáveis.

---
Veja o exemplo em `PHP/exemplos/07_lacos.php`. Próxima nota: [[08-Arrays]]
