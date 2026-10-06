<?php

$nome = "Diego";
echo 'Olá, $nome' . "\n";   // literal
echo "Olá, $nome\n";         // interpolado
echo "Olá, {$nome}!\n";

$idade = 25;
echo "Você tem $idade anos.\n";
echo "Ano que vem: " . ($idade + 1) . "\n";

$texto = "  Olá, Mundo!  ";
echo trim($texto) . "\n";
echo mb_strtolower($texto) . "\n";   // mb_: entende acentos (UTF-8)
echo mb_strtoupper($texto) . "\n";   // "  OLÁ, MUNDO!  " (strtoupper deixaria o "á" minúsculo)
echo str_replace("Olá", "Oi", $texto) . "\n";
echo mb_strlen($texto) . "\n";       // 15 caracteres (strlen contaria 16 bytes: o "á" ocupa 2)

echo $nome[0] . "\n";
echo substr($nome, 0, 3) . "\n";

$email = "diego@exemplo.com";
var_dump(str_contains($email, "@"));
var_dump(str_ends_with($email, ".com"));

$frase = "o rato roeu a roupa";
$palavras = explode(" ", $frase);
print_r($palavras);
echo implode(" ", $palavras) . "\n";

$preco = 19.9;
echo "R$ " . number_format($preco, 2, ",", ".") . "\n";

// Exercício resolvido
if (str_contains($email, "@") && str_ends_with($email, ".com")) {
    echo "e-mail válido\n";
} else {
    echo "e-mail inválido\n";
}

echo "A frase tem " . count($palavras) . " palavras\n";
