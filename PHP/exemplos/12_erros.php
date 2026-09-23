<?php

function dividir($a, $b) {
    if ($b === 0) {
        throw new Exception("Não é possível dividir por zero");
    }
    return $a / $b;
}

try {
    echo dividir(10, 2) . "\n";
    echo dividir(10, 0) . "\n";
} catch (Exception $erro) {
    echo "Erro: " . $erro->getMessage() . "\n";
} finally {
    echo "Isto roda sempre.\n";
}

// Capturando tipo específico do PHP
try {
    $resultado = intdiv(10, 0);
} catch (DivisionByZeroError $erro) {
    echo "Divisão por zero: " . $erro->getMessage() . "\n";
}

// Exceção customizada
class IdadeInvalidaException extends Exception {}

function validarIdade($idade) {
    if ($idade < 0 || $idade > 120) {
        throw new IdadeInvalidaException("Idade fora do intervalo válido: $idade");
    }
    return $idade;
}

try {
    validarIdade(200);
} catch (IdadeInvalidaException $erro) {
    echo $erro->getMessage() . "\n";
}
