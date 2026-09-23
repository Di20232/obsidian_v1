---
tags: [javascript, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Strings em Detalhe

## Mesma ideia central de [[../Python/10-Strings]]

Strings são sequências de caracteres, acessíveis por índice, e **imutáveis** — qualquer método que "modifica" uma string na verdade devolve uma nova.

```javascript
let nome = "Diego";
console.log(nome[0]);        // "D"
console.log(nome.length);     // 5 -> em JS é uma PROPRIEDADE (sem parênteses), não uma função como len() em Python
console.log(nome.slice(0, 3)); // "Die" -> fatiamento, mesmo conceito de [[../Python/10-Strings]]
```

**Diferença de sintaxe importante**: em Python, `len(nome)` é uma função separada ([[../Python/10-Strings]]). Em JavaScript, `nome.length` é uma **propriedade** do próprio valor — sem parênteses, porque não está "fazendo" nada, só devolvendo uma informação que já existe.

## Métodos úteis de string

```javascript
let texto = "  Olá, Mundo!  ";

console.log(texto.trim());                    // remove espaços das pontas -> "Olá, Mundo!"
console.log(texto.toLowerCase());               // tudo minúsculo
console.log(texto.toUpperCase());               // tudo maiúsculo
console.log(texto.replace("Olá", "Oi"));         // troca a PRIMEIRA ocorrência
console.log(texto.replaceAll("l", "L"));          // troca TODAS as ocorrências
```

Assim como em Python ([[../Python/10-Strings]]), **nenhum método altera a string original** — sempre reatribua se quiser guardar o resultado:

```javascript
texto = texto.trim();
```

## Comparando nomes de métodos: Python vs JavaScript

| Python | JavaScript | Faz o quê |
|---|---|---|
| `.strip()` | `.trim()` | remove espaços das pontas |
| `.lower()` | `.toLowerCase()` | minúsculas |
| `.upper()` | `.toUpperCase()` | maiúsculas |
| `.replace(a, b)` | `.replace(a, b)` / `.replaceAll(a, b)` | substitui trecho |
| `len(s)` | `s.length` | tamanho |
| `.split(sep)` | `.split(sep)` | divide em array |
| `sep.join(lista)` | `array.join(sep)` | junta em texto (repare: o "dono" do método troca de lugar!) |

## Template strings, revisitando

Já vistas em [[06-Entrada-e-Saida]] — são o principal jeito de montar texto com variáveis em JavaScript moderno:

```javascript
let preco = 19.9;
console.log(`R$ ${preco.toFixed(2)}`);   // R$ 19.90 -> toFixed formata casas decimais

let nomeMaiusculo = `${nome.toUpperCase()}`;  // dá pra chamar métodos dentro de ${}
```

`.toFixed(2)` é o equivalente ao `:.2f` das f-strings de Python ([[../Python/10-Strings]]).

## Concatenação e repetição

```javascript
let saudacao = "Olá" + " " + "mundo";
let linha = "-".repeat(20);   // equivalente ao "-" * 20 de Python
```

## Verificando conteúdo

```javascript
let email = "diego@exemplo.com";

console.log(email.includes("@"));       // equivalente a "@" in email, do Python
console.log(email.startsWith("diego"));
console.log(email.endsWith(".com"));
```

**Diferença de sintaxe**: em Python, `"@" in email` usa o operador `in` diretamente ([[../Python/10-Strings]]). Em JavaScript, é um método: `email.includes("@")`.

## Dividindo e juntando: `split` e `join` trocam de "dono"

```javascript
let frase = "o rato roeu a roupa";
let palavras = frase.split(" ");          // string -> array
console.log(palavras);

let novaFrase = palavras.join(" ");        // array -> string (repare: .join() é chamado no ARRAY, não no separador)
console.log(novaFrase);
```

Essa é uma diferença de sintaxe que costuma confundir quem vem de Python: lá, `" ".join(lista)` é chamado **na string separadora**; aqui, `array.join(" ")` é chamado **no array**, passando o separador como argumento.

## Exercício

Receba um e-mail como argumento de linha de comando ([[06-Entrada-e-Saida]]) e verifique se contém `"@"` e termina com `.com`. Depois, receba uma frase e conte quantas palavras ela tem usando `.split(" ").length`.

## Perguntas de revisão

Como obter o tamanho de uma string em JavaScript? :: Pela propriedade .length, sem parênteses.

Qual a diferença entre replace e replaceAll? :: replace troca só a primeira ocorrência; replaceAll troca todas.

Como formatar um número com duas casas decimais em JavaScript? :: Com .toFixed(2).

Como verificar se uma string contém um trecho em JavaScript? :: Com o método .includes(), como email.includes("@").

Qual a diferença do join em Python e em JavaScript? :: Em Python é chamado na string separadora (" ".join(lista)); em JavaScript é chamado no array (array.join(" ")).

Quais os equivalentes de strip, lower e upper em JavaScript? :: trim(), toLowerCase() e toUpperCase().

---
Veja o exemplo em `JavaScript/exemplos/10_strings.js`. Próxima nota: [[11-Funcoes]]
