<?php

echo (10 + 3) . "\n";
echo (10 - 3) . "\n";
echo (10 * 3) . "\n";
echo (10 / 3) . "\n";
echo (10 % 3) . "\n";
echo (10 ** 2) . "\n";
echo intdiv(10, 3) . "\n";

// Concatenação
$nome = "Diego";
echo "Olá, " . $nome . "!\n";

// Comparação
var_dump(5 == "5");
var_dump(5 === "5");

// Lógicos
$idade = 20;
$temCarteira = true;
var_dump($idade >= 18 && $temCarteira);

// Atribuição composta
$contador = 0;
$contador += 1;
$contador += 1;
echo $contador . "\n"; // 2

// Coalescência nula
$dados = [];
$nomeVisitante = $dados['nome'] ?? "visitante";
echo $nomeVisitante . "\n";

// Exercício resolvido: semanas e dias em 100 dias
$dias = 100;
$semanas = intdiv($dias, 7);
$diasRestantes = $dias % 7;
echo "$semanas semanas completas e $diasRestantes dias restantes\n";
