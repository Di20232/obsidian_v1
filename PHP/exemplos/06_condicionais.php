<?php

$numero = -4;

if ($numero > 0) {
    echo "Positivo\n";
} elseif ($numero < 0) {
    echo "Negativo\n";
} else {
    echo "É zero\n";
}

echo ($numero % 2 === 0 ? "Par" : "Ímpar") . "\n";

// match
$diaDaSemana = 3;
$nomeDia = match ($diaDaSemana) {
    1 => "Segunda",
    2 => "Terça",
    3 => "Quarta",
    default => "Dia inválido",
};
echo $nomeDia . "\n";

// Truthy/falsy: "0" é falsy em PHP
if ("0") {
    echo "truthy\n";
} else {
    echo "falsy\n"; // isto imprime
}
