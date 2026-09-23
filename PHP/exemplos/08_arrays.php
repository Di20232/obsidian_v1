<?php

$frutas = ["maçã", "banana", "uva"];
echo $frutas[0] . "\n";
echo count($frutas) . "\n";
$frutas[] = "pera";
print_r($frutas);

$pessoa = ["nome" => "Diego", "idade" => 25, "cidade" => "São Paulo"];
echo $pessoa["nome"] . "\n";
$pessoa["idade"] = 26;
$pessoa["profissao"] = "Dev";

if (isset($pessoa["profissao"])) {
    echo $pessoa["profissao"] . "\n";
}

foreach ($pessoa as $chave => $valor) {
    echo "$chave -> $valor\n";
}

// map, filter, reduce
$numeros = [1, 2, 3, 4, 5];
$dobrados = array_map(fn($n) => $n * 2, $numeros);
$pares = array_filter($numeros, fn($n) => $n % 2 === 0);
$soma = array_reduce($numeros, fn($total, $n) => $total + $n, 0);

print_r($dobrados);
print_r($pares);
echo $soma . "\n";

// Exercício resolvido
$produtos = [
    ["nome" => "Caderno", "preco" => 15.90],
    ["nome" => "Caneta", "preco" => 3.50],
    ["nome" => "Mochila", "preco" => 120.00],
];

foreach ($produtos as $produto) {
    echo $produto["nome"] . ": R$ " . number_format($produto["preco"], 2, ",", ".") . "\n";
}

$total = array_reduce($produtos, fn($soma, $p) => $soma + $p["preco"], 0);
echo "Total: R$ " . number_format($total, 2, ",", ".") . "\n";
