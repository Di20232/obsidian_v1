---
tags: [php, basico]
cssclasses: [cerebro-nota, cerebro-php]
---

# Funções

## Sintaxe direta, parecida com JavaScript

```php
<?php
function saudacao($nome) {
    echo "Olá, $nome!\n";
}

saudacao("Diego");
```

Mesma estrutura de `function saudacao(nome) { ... }` em JavaScript ([[../JavaScript/11-Funcoes]]) — a diferença visual é o `$` em todo parâmetro e variável.

## `return`

```php
function somar($a, $b) {
    return $a + $b;
}

$resultado = somar(3, 4);
echo $resultado . "\n";          // 7
echo (somar(10, 5) * 2) . "\n";  // 30
```

Mesma regra já vista em Python ([[../Python/11-Funcoes]]) e JavaScript ([[../JavaScript/11-Funcoes]]): `return` encerra a função imediatamente.

## Parâmetros com valor padrão

```php
function saudacao2($nome, $saudacaoInicial = "Olá") {
    echo "$saudacaoInicial, $nome!\n";
}

saudacao2("Diego");               // "Olá, Diego!"
saudacao2("Diego", "Bom dia");    // "Bom dia, Diego!"
```

## Argumentos nomeados — PHP tem, nativamente (diferente de JavaScript!)

Lembra que em [[../Python/11-Funcoes]] você usou argumentos nomeados (`apresentar(nome="Diego", ...)`), e que JavaScript **não tem** isso nativamente ([[../JavaScript/11-Funcoes]], resolvido lá com desestruturação de objeto)? PHP (desde a versão 8) tem argumentos nomeados **de verdade**, com sintaxe própria:

```php
function apresentar($nome, $idade, $cidade) {
    echo "$nome, $idade anos, de $cidade\n";
}

apresentar(cidade: "São Paulo", nome: "Diego", idade: 25);  // ordem não importa, igual Python
```

## Type hints: tipagem opcional, uma diferença real em relação a Python/JS

PHP permite (mas não obriga) declarar o tipo esperado de cada parâmetro e do retorno — algo que nem Python nem JavaScript têm nativamente (lembre do eixo de tipagem em [[../Programacao-Geral/06-Paradigmas-e-Panorama-de-Linguagens]]; o mais próximo seria TypeScript):

```php
function somarTipado(int $a, int $b): int {
    return $a + $b;
}

echo somarTipado(3, 4) . "\n";     // 7
somarTipado("abc", 4);               // TypeError: em modo estrito, ou tenta converter em modo padrão
```

`int $a, int $b` são os tipos dos parâmetros; `: int` depois dos parênteses é o tipo do retorno. Isso é **opcional**, mas cada vez mais usado em código PHP moderno, porque captura erros de tipo mais cedo — o mesmo benefício discutido em [[../Programacao-Geral/06-Paradigmas-e-Panorama-de-Linguagens]] sobre tipagem estática.

## Arrow functions (`fn`), já vistas em [[08-Arrays]]

```php
$dobro = fn($numero) => $numero * 2;
echo $dobro(5) . "\n";   // 10
```

Equivalente compacto à arrow function de JavaScript ([[../JavaScript/11-Funcoes]]) — mas mais restrito: só aceita **uma expressão** (sem chaves, sem múltiplas linhas), sempre com `return` implícito.

## Closures: funções anônimas "normais"

Para uma função anônima com corpo mais longo (múltiplas linhas), PHP usa `function` sem nome:

```php
$saudacao3 = function ($nome) {
    echo "Olá (closure), $nome!\n";
};

$saudacao3("Diego");
```

## Escopo: mesma regra de Python e JavaScript

```php
function calcular() {
    $resultado = 10;  // existe só dentro desta função
    return $resultado;
}

echo calcular() . "\n";
echo $resultado . "\n";   // ERRO: Undefined variable $resultado
```

## Exercício

Escreva uma função `ehPar(int $numero): bool` usando type hints, que retorna `true`/`false`. Depois, use um `for` (de [[07-Lacos-de-Repeticao]]) para testá-la com os números de 1 a 10.

---
Veja o exemplo em `PHP/exemplos/10_funcoes.php`. Próxima nota: [[11-Formularios-e-Superglobais]]
