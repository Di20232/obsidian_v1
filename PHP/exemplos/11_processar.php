<?php

$nome = $_POST['nome'] ?? '';
$idade = (int) ($_POST['idade'] ?? 0);

if ($idade < 0 || $idade > 120) {
    echo "Idade inválida";
} else {
    echo "Olá, $nome! Você tem $idade anos.";
}

// Rode: php -S localhost:8000
// Depois abra: http://localhost:8000/11_formulario.html
