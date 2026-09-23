---
tags: [php, basico]
cssclasses: [cerebro-nota, cerebro-php]
---

# Variáveis e Tipos de Dados

## A regra mais visível de PHP: todo nome de variável começa com `$`

```php
<?php

$nome = "Diego";
$idade = 25;
$altura = 1.78;
```

Diferente de Python (`nome = "Diego"`, [[../Python/04-Variaveis-e-Tipos]]) e JavaScript (`let nome = "Diego"`, [[../JavaScript/04-Variaveis-e-Tipos]]), PHP não usa uma palavra-chave como `let`/`const`/`var` para declarar — o `$` na frente já basta, e a variável passa a existir na primeira vez que recebe um valor.

## Tipos de dado

```php
$idade = 25;              // int
$altura = 1.78;            // float
$nome = "Diego";           // string
$estaEstudando = true;     // bool
$semValor = null;           // null -> mesmo conceito de None (Python) / null (JavaScript)
```

Verificando o tipo, equivalente a `type()` (Python) e `typeof` (JavaScript):

```php
var_dump($idade);   // mostra tipo E valor: int(25)
echo gettype($idade); // "integer" -> só o nome do tipo
```

## Tipagem dinâmica, como Python e JavaScript

```php
$x = 10;        // $x é int agora
$x = "dez";     // agora $x é string -> permitido, mesma flexibilidade de Python/JS
```

Mesmo eixo discutido em [[../Programacao-Geral/06-Paradigmas-e-Panorama-de-Linguagens]]: PHP é dinamicamente tipada — o tipo é decidido pelo valor atual, não travado na declaração.

## Convertendo tipos (casting)

```php
$idadeTexto = "25";
$idadeNumero = (int) $idadeTexto;   // casting explícito, colocando o tipo entre parênteses
echo $idadeNumero + 1;                // 26

$numero = 10;
$numeroTexto = (string) $numero;
echo "Tenho " . $numeroTexto . " anos";  // . é o operador de concatenação, ver [[09-Strings]]

// Funções equivalentes, mais legíveis:
$idadeNumero2 = intval("25");
$numeroTexto2 = strval(10);
```

## Type juggling: a versão PHP da conversão automática

Assim como JavaScript ([[../JavaScript/04-Variaveis-e-Tipos]]), PHP também converte tipos automaticamente em certas operações — chamado de **type juggling**:

```php
echo "5" + 3;      // 8   -> "5" é convertido para número (diferente de JS, onde "5" + 3 concatena!)
echo "5" . 3;       // "53" -> . sempre concatena, convertendo o número para texto
echo "5abc" + 3;    // aviso + 8 em versões antigas; erro em PHP 8+ (mais rígido nisso)
```

**Diferença real em relação a JavaScript**: em JS, `+` faz concatenação se qualquer lado for string ([[../JavaScript/04-Variaveis-e-Tipos]]). Em PHP, `+` é **sempre** aritmético — para concatenar texto, PHP usa um operador **próprio**, o ponto (`.`), nunca o `+`. Isso evita a ambiguidade que existe em JS, mas exige lembrar que os dois operadores têm papéis totalmente separados.

## Constantes de verdade

Diferente da convenção informal do Python (`IDADE_MINIMA = 18`, [[../Python/04-Variaveis-e-Tipos]]), PHP tem uma forma de criar uma constante **de verdade**, travada pela linguagem:

```php
define("PI", 3.14159);
echo PI;              // sem $ na frente ao usar!

const IDADE_MINIMA = 18;   // forma mais moderna, só pode ser usada fora de funções condicionais
```

## Nomes de variáveis

Mesmas regras gerais de Python/JavaScript (letras, números, `_`, não pode começar com número), sempre precedidas de `$`. A convenção da comunidade PHP é **camelCase** (`nomeCompleto`), igual JavaScript ([[../JavaScript/04-Variaveis-e-Tipos]]), embora `snake_case` também apareça bastante em código PHP mais antigo ou seguindo o padrão do WordPress.

## Exercício

Crie `$nome`, `$idade` e `$cidade`, e exiba uma frase juntando os três com `.` (concatenação). Depois, teste `echo "5" + "3";` e `echo "5" . "3";` e compare os resultados, explicando a diferença para si mesmo.

---
Veja o exemplo em `PHP/exemplos/04_variaveis.php`. Próxima nota: [[05-Operadores]]
