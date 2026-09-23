---
tags: [php, basico]
cssclasses: [cerebro-nota, cerebro-php]
---

# Operadores

## Aritméticos

```php
<?php
echo 10 + 3;   // 13
echo 10 - 3;   // 7
echo 10 * 3;   // 30
echo 10 / 3;   // 3.3333333333333
echo 10 % 3;   // 1
echo 10 ** 2;  // 100 -> potência
echo intdiv(10, 3); // 3 -> divisão inteira (equivalente ao // de Python)
```

`intdiv()` é o equivalente direto do `//` de Python ([[../Python/05-Operadores]]) — JavaScript não tem nenhum dos dois nativamente, e usa `Math.floor()` ([[../JavaScript/05-Operadores]]).

## Concatenação: `.`, não `+`

Já visto em [[04-Variaveis-e-Tipos]], mas essencial repetir: em PHP, texto é unido com **ponto**, nunca com `+`:

```php
$nome = "Diego";
echo "Olá, " . $nome . "!";

$saudacao = "Olá, ";
$saudacao .= $nome;   // .= concatena e reatribui, equivalente ao += para números
echo $saudacao;
```

## Comparação: `==` vs `===`, a mesma pegadinha de JavaScript

```php
var_dump(5 == "5");    // true  -> compara valor, convertendo tipos
var_dump(5 === "5");   // false -> compara valor E tipo, sem converter
var_dump(5 != "5");    // false
var_dump(5 !== "5");   // true
```

Mesma regra de ouro de [[../JavaScript/05-Operadores]]: **sempre prefira `===` e `!==`**. O `==` de PHP tem um histórico de comportamentos ainda mais surpreendentes que o de JavaScript em alguns casos (comparações entre strings e números "parecidos"), então essa regra é ainda mais importante aqui.

```php
echo 5 > 3;    // 1 (PHP imprime true como "1")
var_dump(5 > 3); // bool(true) -> var_dump mostra o tipo real, melhor para depurar
```

**Detalhe de saída**: `echo` de um `bool` imprime `1` para `true` e **nada** (string vazia) para `false` — por isso `var_dump()` é preferível ao depurar valores booleanos, porque mostra o tipo e o valor de forma explícita.

## Lógicos

```php
$idade = 20;
$temCarteira = true;

var_dump($idade >= 18 && $temCarteira);   // && = "e"
var_dump($idade >= 18 || $temCarteira);    // || = "ou"
var_dump(!$temCarteira);                    // ! = "não"

// PHP também aceita and/or/not por extenso, mas com precedência diferente — evite misturar
```

Sintaticamente idêntico a JavaScript ([[../JavaScript/05-Operadores]]).

## Atribuição composta

```php
$contador = 10;
$contador += 1;
$contador -= 2;
$contador *= 3;
$contador /= 3;
```

## Operador de coalescência nula (`??`): uma ferramenta que Python e JS têm de forma diferente

```php
$nome = $_GET['nome'] ?? "visitante";
```

`??` devolve o valor da esquerda se ele existir e não for `null`; senão, devolve o da direita. É extremamente comum ao lidar com dados que podem não existir — como campos de formulário (ver [[11-Formularios-e-Superglobais]]), evitando um `if` explícito só para checar isso.

## Precedência

Mesma regra geral: parênteses primeiro, depois potência, depois multiplicação/divisão, depois soma/subtração/concatenação. Use parênteses sempre que houver dúvida.

## Exercício

Calcule quantas semanas completas e quantos dias sobram em 100 dias, usando `intdiv()` e `%`. Depois, teste `var_dump(0 == "abc")` — em versões antigas de PHP (antes da 8) isso retornava `true`, uma das pegadinhas históricas mais famosas da linguagem; em PHP 8+ retorna `false`. Pesquise brevemente por que essa mudança foi feita, é um bom exemplo de como uma linguagem evolui para evitar armadilhas.

---
Veja o exemplo em `PHP/exemplos/05_operadores.php`. Próxima nota: [[06-Condicionais]]
