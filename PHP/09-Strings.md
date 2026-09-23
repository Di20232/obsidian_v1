---
tags: [php, basico]
cssclasses: [cerebro-nota, cerebro-php]
---

# Strings em Detalhe

## Aspas simples vs. duplas: uma diferença real, não só de estilo

Diferente de Python e JavaScript (onde aspas simples e duplas são intercambiáveis), em PHP elas **se comportam diferente**:

```php
<?php
$nome = "Diego";

echo 'Olá, $nome';    // imprime literalmente: Olá, $nome (aspas simples NÃO interpolam variável)
echo "Olá, $nome";     // imprime: Olá, Diego (aspas duplas interpolam variável)
echo "Olá, {$nome}!";  // forma mais explícita, útil quando há ambiguidade (ex.: {$nome}s)
```

**Regra prática**: use aspas simples para texto fixo, sem variáveis (é ligeiramente mais rápido e evita interpolação acidental); use aspas duplas quando precisar inserir variáveis diretamente no texto.

## Interpolação: o "quase f-string" do PHP

```php
$idade = 25;
echo "Você tem $idade anos.";           // funciona direto dentro de aspas duplas
echo "Ano que vem: " . ($idade + 1);     // expressões precisam de concatenação, não interpolam direto
echo "Ano que vem: {$idade}";             // {} delimita claramente onde a variável termina
```

Isso é parecido com as f-strings de Python ([[../Python/06-Entrada-e-Saida]]) e as template strings de JavaScript ([[../JavaScript/06-Entrada-e-Saida]]), mas com uma limitação: só **variáveis simples** interpolam diretamente; **expressões** (como `$idade + 1`) exigem concatenação com `.` fora das aspas.

## Métodos... na verdade, funções

Diferença estrutural importante: em Python (`"oi".upper()`) e JavaScript (`"oi".toUpperCase()`), strings têm **métodos** — chamados com `.` no próprio valor. Em PHP, a maioria das operações de string são **funções soltas**, que recebem a string como argumento:

```php
$texto = "  Olá, Mundo!  ";

echo trim($texto);              // remove espaços das pontas -> equivalente a .strip()/.trim()
echo strtolower($texto);         // minúsculas
echo strtoupper($texto);         // maiúsculas
echo str_replace("Olá", "Oi", $texto);  // substitui
echo strlen($texto);              // tamanho -> equivalente a len()/​.length
```

| Python | JavaScript | PHP |
|---|---|---|
| `.strip()` | `.trim()` | `trim($s)` |
| `.lower()` | `.toLowerCase()` | `strtolower($s)` |
| `.upper()` | `.toUpperCase()` | `strtoupper($s)` |
| `.replace(a,b)` | `.replace(a,b)` | `str_replace(a, b, $s)` |
| `len(s)` | `s.length` | `strlen($s)` |
| `.split(sep)` | `.split(sep)` | `explode(sep, $s)` |
| `sep.join(lista)` | `array.join(sep)` | `implode(sep, $array)` |

## Fatiamento e busca

```php
$nome = "Diego";
echo $nome[0];                    // "D" -> acesso por índice funciona igual array
echo substr($nome, 0, 3);          // "Die" -> equivalente a slice()/fatiamento

$email = "diego@exemplo.com";
var_dump(str_contains($email, "@"));       // equivalente a "in" (Python) / .includes() (JS)
var_dump(str_starts_with($email, "diego"));
var_dump(str_ends_with($email, ".com"));
```

`str_contains`, `str_starts_with` e `str_ends_with` só existem a partir do PHP 8 — versões anteriores precisavam de `strpos()`, mais indireta.

## Dividindo e juntando: `explode` e `implode`

```php
$frase = "o rato roeu a roupa";
$palavras = explode(" ", $frase);    // string -> array, equivalente a .split()
print_r($palavras);

$novaFrase = implode(" ", $palavras); // array -> string, equivalente a .join() (JS) / sep.join() (Python)
echo $novaFrase;
```

## Formatando números dentro de texto

```php
$preco = 19.9;
echo "R$ " . number_format($preco, 2, ",", ".");  // "R$ 19,90" -> casas decimais, vírgula, separador de milhar
```

`number_format()` é mais explícito que o `:.2f` de Python ou `.toFixed(2)` de JavaScript, mas também mais flexível — permite escolher o separador decimal e de milhar, útil para formatação em português (vírgula decimal, ponto de milhar).

## Exercício

Escreva um script que valide um e-mail fixo usando `str_contains` e `str_ends_with`. Depois, use `explode` para dividir uma frase em palavras e `count` (visto em [[08-Arrays]]) para contar quantas são.

---
Veja o exemplo em `PHP/exemplos/09_strings.php`. Próxima nota: [[10-Funcoes]]
