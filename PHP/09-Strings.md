---
tags: [php, basico, flashcards]
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
echo mb_strtolower($texto);      // minúsculas
echo mb_strtoupper($texto);      // maiúsculas: "  OLÁ, MUNDO!  "
echo str_replace("Olá", "Oi", $texto);  // substitui
echo mb_strlen($texto);           // tamanho em caracteres: 15 -> equivalente a len()/.length
```

> [!warning] Texto com acento: use as funções `mb_`
> `strtoupper`, `strtolower` e `strlen` trabalham com **bytes**, não com letras. Em UTF-8, o "á" ocupa 2 bytes. Por isso `strtoupper("  Olá, Mundo!  ")` devolve `"  OLá, MUNDO!  "` (o "á" continua minúsculo) e `strlen` do mesmo texto dá 16, não 15. As versões `mb_` (de *multibyte*) convertem e contam letras de verdade. O mesmo vale para `substr` e `$texto[0]`: com acento, use `mb_substr`. Saída conferida com o PHP 8.3.6 em 06/10/2026.
>
> Se o PHP disser que `mb_strtoupper` não existe, a extensão `mbstring` está desligada: no `php.ini`, tire o `;` do começo da linha `;extension=mbstring`. Na instalação pelo ZIP da [[02-Preparando-o-Ambiente|nota 02]], a pasta do PHP traz o `php.ini-development`, mas não o `php.ini`: copie o primeiro com o nome `php.ini` e faça a troca nele.

| Python | JavaScript | PHP |
|---|---|---|
| `.strip()` | `.trim()` | `trim($s)` |
| `.lower()` | `.toLowerCase()` | `mb_strtolower($s)` |
| `.upper()` | `.toUpperCase()` | `mb_strtoupper($s)` |
| `.replace(a,b)` | `.replace(a,b)` | `str_replace(a, b, $s)` |
| `len(s)` | `s.length` | `mb_strlen($s)` |
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

## Perguntas de revisão

Qual a diferença entre aspas simples e duplas em PHP? :: Aspas duplas interpolam variáveis; aspas simples imprimem o texto literalmente.

Expressões como $idade + 1 interpolam dentro de aspas duplas? :: Não; só variáveis simples interpolam, expressões precisam de concatenação.

Como as operações de string funcionam em PHP? :: Como funções soltas que recebem a string, como mb_strtoupper($s), e não como métodos.

Quais os equivalentes de split e join em PHP? :: explode(separador, $texto) e implode(separador, $array).

Como formatar R$ 19,90 em PHP? :: Com number_format($preco, 2, ",", "."), escolhendo vírgula decimal e ponto de milhar.

Como medir o tamanho de uma string com acento em PHP? :: Com mb_strlen($texto), que conta caracteres; strlen conta bytes, e em UTF-8 o "á" ocupa 2.

Por que strtoupper("Olá") não devolve "OLÁ"? :: Porque strtoupper trabalha com bytes e só converte letras sem acento; para texto em UTF-8, use mb_strtoupper.

---
Veja o exemplo em `PHP/exemplos/09_strings.php`. Próxima nota: [[10-Funcoes]]
