<?php

for ($i = 0; $i < 5; $i++) {
    echo $i . "\n";
}

$frutas = ["maçã", "banana", "uva"];
foreach ($frutas as $indice => $fruta) {
    echo "$indice: $fruta\n";
}

$pessoa = ["nome" => "Diego", "idade" => 25];
foreach ($pessoa as $chave => $valor) {
    echo "$chave -> $valor\n";
}

$contador = 0;
while ($contador < 5) {
    echo $contador . "\n";
    $contador++;
}

// do...while
$numero = 10;
do {
    echo "rodou pelo menos uma vez: $numero\n";
    $numero++;
} while ($numero < 5);

// Exercício resolvido: tabuada
$numeroTabuada = 7;
for ($i = 1; $i <= 10; $i++) {
    echo "$numeroTabuada x $i = " . ($numeroTabuada * $i) . "\n";
}

// Exercício resolvido: produtos
$produtos = ["Caderno" => 15.90, "Caneta" => 3.50, "Mochila" => 120.00];
foreach ($produtos as $nome => $preco) {
    echo "$nome: R$ " . number_format($preco, 2, ",", ".") . "\n";
}
