---
tags: [php, basico, estruturas-de-dados, flashcards]
cssclasses: [cerebro-nota, cerebro-php]
---

# Arrays

## A grande particularidade de PHP: um único tipo faz o trabalho de dois

Python separa lista e dicionário ([[../Python/09-Listas-Tuplas-Dicionarios]]); JavaScript separa array e objeto ([[../JavaScript/09-Arrays-e-Objetos]]). **PHP usa um único tipo, `array`, para os dois casos** — ele pode ter índices numéricos automáticos (como uma lista) ou chaves nomeadas (como um dicionário), e até misturar os dois.

## Array indexado (equivalente a lista/array)

```php
<?php
$frutas = ["maçã", "banana", "uva"];   // sintaxe moderna
$frutas2 = array("maçã", "banana");     // sintaxe antiga, ainda válida, evite em código novo

echo $frutas[0];        // "maçã" -> índice começa em 0, igual Python/JS
echo count($frutas);     // 3 -> equivalente a len()/​.length

$frutas[] = "pera";       // adiciona no fim (equivalente a .append()/.push())
array_push($frutas, "abacaxi");  // forma alternativa de adicionar

unset($frutas[0]);         // remove o item do índice 0 (deixa um "buraco" nos índices!)
$frutas = array_values($frutas);  // reindexa, fechando o buraco
```

**Diferença sutil e importante**: `unset()` remove o valor, mas **não reorganiza os índices** automaticamente — se você remover o item do meio, o array fica com índices "faltando" (`0, 2, 3` em vez de `0, 1, 2`). `array_values()` reconstrói os índices em sequência, se isso importar para o seu caso.

## Array associativo (equivalente a dicionário/objeto)

```php
$pessoa = [
    "nome" => "Diego",
    "idade" => 25,
    "cidade" => "São Paulo",
];

echo $pessoa["nome"];      // acesso por chave, igual dicionário Python
$pessoa["idade"] = 26;      // altera
$pessoa["profissao"] = "Dev"; // adiciona

if (isset($pessoa["profissao"])) {   // equivalente a "in" (Python) / "in" (JS)
    echo $pessoa["profissao"];
}
```

`isset()` verifica se uma chave existe **e** não é `null` — a forma padrão de checar chaves em PHP antes de acessá-las, evitando um aviso do interpretador ao acessar uma chave inexistente.

## Percorrendo (conecta com [[07-Lacos-de-Repeticao]])

```php
foreach ($frutas as $fruta) {
    echo $fruta . "\n";
}

foreach ($pessoa as $chave => $valor) {
    echo "$chave -> $valor\n";
}
```

## Funções úteis de array, equivalentes a `map`/`filter`/`reduce` de JavaScript

```php
$numeros = [1, 2, 3, 4, 5];

$dobrados = array_map(fn($n) => $n * 2, $numeros);         // equivalente a .map() (JS)
$pares = array_filter($numeros, fn($n) => $n % 2 === 0);    // equivalente a .filter() (JS)
$soma = array_reduce($numeros, fn($total, $n) => $total + $n, 0);  // equivalente a .reduce() (JS)

print_r($dobrados);
print_r($pares);
echo $soma . "\n";
```

`fn($n) => $n * 2` é uma **arrow function** de PHP (desde PHP 7.4) — sintaxe parecida com a de JavaScript ([[../JavaScript/11-Funcoes]]), usada com frequência dentro dessas funções de array. `print_r()` exibe um array de forma legível para depuração, parecido com `console.log` em um array/objeto do JavaScript.

## Fatiamento

```php
$numeros2 = [10, 20, 30, 40, 50];
print_r(array_slice($numeros2, 1, 2));   // [20, 30] -> a partir do índice 1, pegando 2 itens
```

**Diferença de sintaxe**: `array_slice($array, inicio, quantidade)` usa **quantidade**, não um índice final como o `slice()`/fatiamento de Python e JavaScript.

## Array de arrays associativos (o "array de objetos" de PHP)

```php
$produtos = [
    ["nome" => "Caderno", "preco" => 15.90],
    ["nome" => "Caneta", "preco" => 3.50],
];

foreach ($produtos as $produto) {
    echo $produto["nome"] . ": R$ " . $produto["preco"] . "\n";
}
```

Mesma ideia de "tabela de dados" vista em [[../Python/09-Listas-Tuplas-Dicionarios]] e [[../JavaScript/09-Arrays-e-Objetos]] — e, igual nas outras linguagens, é o formato que aparece ao decodificar uma resposta JSON de uma API (ver [[../Programacao-Geral/10-Como-a-Web-Funciona]]) com `json_decode()`.

## Exercício

Crie um array de arrays associativos representando 3 produtos (`nome`, `preco`). Use `foreach` para exibir cada um, e `array_reduce` para calcular o preço total.

## Perguntas de revisão

Qual a particularidade dos arrays em PHP? :: Um único tipo array serve como lista (índices numéricos) e como dicionário (chaves nomeadas).

Como adicionar um item no fim de um array em PHP? :: Com $array[] = valor ou array_push($array, valor).

O que acontece com os índices depois de unset num array? :: Ficam buracos na sequência; array_values reconstrói os índices.

Como verificar se uma chave existe num array PHP? :: Com isset($array["chave"]), que também exige que o valor não seja null.

Quais os equivalentes de map, filter e reduce em PHP? :: array_map, array_filter e array_reduce.

Como array_slice difere do fatiamento de Python? :: O terceiro argumento é a quantidade de itens, não o índice final.

Como contar os itens de um array em PHP? :: Com count($array).

---
Veja o exemplo em `PHP/exemplos/08_arrays.php`. Próxima nota: [[09-Strings]]
