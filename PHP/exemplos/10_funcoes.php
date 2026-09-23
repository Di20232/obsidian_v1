<?php

function saudacao($nome) {
    echo "Olá, $nome!\n";
}
saudacao("Diego");

function somar($a, $b) {
    return $a + $b;
}
echo somar(3, 4) . "\n";

function saudacao2($nome, $saudacaoInicial = "Olá") {
    echo "$saudacaoInicial, $nome!\n";
}
saudacao2("Diego");
saudacao2("Diego", "Bom dia");

function apresentar($nome, $idade, $cidade) {
    echo "$nome, $idade anos, de $cidade\n";
}
apresentar(cidade: "São Paulo", nome: "Diego", idade: 25);

function somarTipado(int $a, int $b): int {
    return $a + $b;
}
echo somarTipado(3, 4) . "\n";

$dobro = fn($numero) => $numero * 2;
echo $dobro(5) . "\n";

$saudacao3 = function ($nome) {
    echo "Olá (closure), $nome!\n";
};
$saudacao3("Diego");

// Exercício resolvido
function ehPar(int $numero): bool {
    return $numero % 2 === 0;
}

for ($numero = 1; $numero <= 10; $numero++) {
    var_dump(ehPar($numero));
}
