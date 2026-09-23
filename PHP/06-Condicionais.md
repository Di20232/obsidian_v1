---
tags: [php, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-php]
---

# Estruturas Condicionais

## Sintaxe quase idêntica à de JavaScript

```php
<?php
$idade = 20;

if ($idade >= 18) {
    echo "Pode entrar";
}
```

Mesma estrutura de [[../JavaScript/07-Condicionais]]: parênteses na condição, chaves no bloco. A diferença visual mais imediata é o `$` obrigatório em toda variável.

## if / else / elseif

Repare: PHP usa **`elseif`** (uma palavra só), diferente do `else if` (duas palavras) de JavaScript:

```php
$nota = 7;

if ($nota >= 9) {
    echo "Conceito A";
} elseif ($nota >= 7) {
    echo "Conceito B";
} elseif ($nota >= 5) {
    echo "Conceito C";
} else {
    echo "Reprovado";
}
```

(`else if`, com espaço, também funciona em PHP dentro de chaves, mas `elseif` é a convenção mais usada.)

## Operador ternário e o atalho "ternário curto"

```php
$idade = 20;
$status = $idade >= 18 ? "adulto" : "menor de idade";
echo $status;

// Atalho: se você só quer usar o próprio valor quando ele for "truthy"
$nome = $nomeDigitado ?: "visitante";  // equivalente a: $nomeDigitado ? $nomeDigitado : "visitante"
```

Mesmo operador ternário visto em [[../JavaScript/07-Condicionais]]. O atalho `?:` (sem a parte do meio) é específico de PHP.

## `match`: mais seguro que `switch`

PHP tem `switch` (igual ao de [[../JavaScript/07-Condicionais]], com o mesmo risco de esquecer `break`), mas desde PHP 8 existe `match`, uma alternativa mais moderna e sem essa armadilha:

```php
$diaDaSemana = 3;

$nome = match ($diaDaSemana) {
    1 => "Segunda",
    2 => "Terça",
    3 => "Quarta",
    default => "Dia inválido",
};

echo $nome;
```

`match` **não precisa de `break`** (não existe fall-through, o problema mencionado em [[../JavaScript/07-Condicionais]]) e **retorna um valor diretamente**, então pode ser atribuído a uma variável, como no exemplo acima — mais parecido com o `match`/`case` do que outras linguagens modernas oferecem. Prefira `match` a `switch` sempre que possível em código novo.

## Truthy e falsy

PHP também converte qualquer valor para verdadeiro/falso dentro de um `if`, com uma lista parecida com a de Python ([[../Python/07-Condicionais]]): são **falsy** — `false`, `0`, `0.0`, `""` (string vazia), `"0"` (!), `null`, array vazio `[]`. Repare: `"0"` é falsy em PHP (diferente de JavaScript, onde `"0"` é truthy, ver [[../JavaScript/07-Condicionais]]) — mais uma pegadinha de comparação entre as duas linguagens que vale gravar.

```php
$nome = "";
if ($nome) {
    echo "Olá, $nome";
} else {
    echo "Nome não informado";
}
```

## Exercício

Escreva um script que peça um número (pode fixar em uma variável por enquanto, já que entrada interativa via terminal só é vista em profundidade em [[11-Formularios-e-Superglobais]]) e diga se ele é positivo, negativo ou zero, e se é par ou ímpar. Depois, reescreva a lógica do dia da semana usando `match` em vez de `if`/`elseif`.

## Perguntas de revisão

Como se escreve else if em PHP? :: elseif, numa palavra só, é a convenção.

O que faz o operador ?: em PHP? :: Usa o próprio valor se for verdadeiro, senão o padrão: $nome ?: "visitante".

Por que preferir match a switch em PHP? :: match não precisa de break, não tem fall-through e retorna um valor diretamente.

"0" é verdadeiro ou falso em PHP? :: Falso; em JavaScript, "0" seria verdadeiro.

Quais valores são falsy em PHP? :: false, 0, 0.0, string vazia, "0", null e array vazio.

---
Veja o exemplo em `PHP/exemplos/06_condicionais.php`. Próxima nota: [[07-Lacos-de-Repeticao]]
