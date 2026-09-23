<?php

$nome = "Diego";
$idade = 25;
$altura = 1.78;
$estaEstudando = true;

echo $nome . "\n";
echo $idade . "\n";
echo $altura . "\n";
var_dump($estaEstudando);

echo gettype($idade) . "\n";

// Conversão de tipos
$idadeTexto = "25";
$idadeNumero = (int) $idadeTexto;
echo ($idadeNumero + 1) . "\n";

$numero = 10;
$numeroTexto = (string) $numero;
echo "Tenho " . $numeroTexto . " anos\n";

// Type juggling: + é aritmético, . é concatenação
echo ("5" + 3) . "\n";  // 8
echo ("5" . 3) . "\n";  // 53

// Constante
define("PI", 3.14159);
echo PI . "\n";
