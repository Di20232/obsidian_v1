---
tags: [php, basico]
cssclasses: [cerebro-nota, cerebro-php]
---

# Tratamento de Erros

## Mesmo problema de [[../Python/13-Tratamento-de-Erros]] e [[../JavaScript/13-Tratamento-de-Erros]]

Coisas dão errado: dados inválidos, conexão com banco falhando, arquivos ausentes. PHP moderno (7+) usa `try`/`catch`, com sintaxe muito parecida com a de JavaScript.

## `try` / `catch`

```php
<?php
function dividir($a, $b) {
    if ($b === 0) {
        throw new Exception("Não é possível dividir por zero");
    }
    return $a / $b;
}

try {
    echo dividir(10, 0);
} catch (Exception $erro) {
    echo "Erro: " . $erro->getMessage();
}
```

Mesma estrutura de [[../JavaScript/13-Tratamento-de-Erros]]: `throw new Exception(...)` lança um erro (equivalente a `throw new Error(...)` em JS, ou `raise ValueError(...)` em Python); `$erro->getMessage()` recupera o texto da mensagem — `->` é a sintaxe de acesso a métodos/propriedades de objeto em PHP, aprofundada em [[13-POO]].

## `finally`

```php
try {
    echo "Tentando...\n";
    throw new Exception("Algo deu errado");
} catch (Exception $erro) {
    echo "Capturado: " . $erro->getMessage() . "\n";
} finally {
    echo "Isto roda sempre.\n";
}
```

Mesmo comportamento já visto nas outras duas linguagens.

## Tipos de exceção: capturando o erro certo

Assim como Python tem `ValueError`, `TypeError` etc. ([[../Python/13-Tratamento-de-Erros]]), PHP tem uma hierarquia de classes de exceção. Você pode capturar tipos específicos:

```php
try {
    $resultado = 10 / 0;   // DivisionByZeroError em PHP 8+
} catch (DivisionByZeroError $erro) {
    echo "Divisão por zero: " . $erro->getMessage() . "\n";
} catch (Exception $erro) {
    echo "Outro erro: " . $erro->getMessage() . "\n";
}
```

Capturar do tipo mais específico para o mais genérico (como no exemplo, `DivisionByZeroError` antes de `Exception`) segue a mesma lógica de [[../Python/13-Tratamento-de-Erros]]: dá uma mensagem mais precisa para cada situação.

## Criando seu próprio tipo de exceção

```php
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
```

`extends Exception` (herança, aprofundada em [[13-POO]]) cria um tipo de erro próprio do seu domínio — o mesmo espírito de criar uma classe de exceção personalizada em Python, e algo que, em JavaScript, seria feito estendendo a classe `Error`.

## `Errors` vs `Exceptions`: uma distinção específica de PHP

PHP 7+ distingue **Errors** (problemas graves, geralmente de programação — como chamar um método que não existe) de **Exceptions** (problemas esperados do fluxo do programa, como os exemplos acima). Ambos podem ser capturados com `catch`, e ambos implementam uma interface comum chamada `Throwable`:

```php
try {
    metodoQueNaoExiste();
} catch (Throwable $erro) {
    echo "Capturado: " . $erro->getMessage() . "\n";
}
```

Na prática do dia a dia, capturar `Exception` (ou tipos mais específicos) já cobre a grande maioria dos casos — `Throwable` é útil quando você realmente quer capturar **qualquer coisa**, incluindo erros de programação, o que geralmente só faz sentido em um ponto central da aplicação (ver o mesmo alerta contra `except` genérico demais em [[../Python/13-Tratamento-de-Erros]]).

## Exercício

Escreva uma função `dividir($a, $b)` que lança `DivisionByZeroError` (ou uma exceção sua) quando `$b` é zero. Chame-a dentro de `try`/`catch`, testando com um divisor válido e depois com zero.

---
Veja o exemplo em `PHP/exemplos/12_erros.php`. Próxima nota: [[13-POO]]
