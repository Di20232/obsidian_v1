---
tags: [php, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-php]
---

# Primeiro Programa

## Duas formas de começar

Para simplificar o aprendizado da linguagem em si (sem misturar com HTML ainda), as primeiras notas desta trilha usam arquivos `.php` "puros", rodados direto pelo terminal — só voltamos a misturar com HTML explicitamente em [[11-Formularios-e-Superglobais]].

```php
<?php

echo "Olá, mundo!";
```

Veja o exemplo completo em `PHP/exemplos/03_ola_mundo.php`.

## Executando

```bash
php 03_ola_mundo.php
```

Saída:

```
Olá, mundo!
```

## Desmontando

- `<?php` — abre a tag PHP; tudo depois disso, até um `?>` (ou o fim do arquivo), é código PHP. Quando o arquivo é **só** código PHP, como neste caso, a convenção moderna é **nem fechar** a tag com `?>` no final — evita espaços em branco acidentais depois dela que podem causar bugs sutis em páginas reais.
- `echo` — a instrução mais comum para gerar saída. Não são parênteses obrigatórios (diferente de `print()` em Python e `console.log()` em JavaScript): `echo "Olá, mundo!";` já é válido sozinho.
- `;` — obrigatório no fim de toda instrução, sem exceção (diferente de JavaScript, onde é convencional mas dispensável em muitos casos, ver [[../JavaScript/03-Primeiro-Programa]]).

## Chaves `{ }`, como em JavaScript

PHP usa chaves para blocos de código, igual visto em [[../JavaScript/03-Primeiro-Programa]] — não indentação, como em Python:

```php
if (true) {
    echo "dentro do bloco";
}
```

## Comentários

```php
// Comentário de uma linha (mesmo estilo de JavaScript)
# Também é comentário de uma linha (estilo herdado do shell/Perl)
/* Comentário
   de várias linhas */

echo "Isto é executado.";
```

## `echo` vs `print`

```php
echo "Olá";     // mais comum, aceita múltiplos valores separados por vírgula
print "Olá";     // praticamente idêntico, mas só aceita um valor e "retorna" 1
```

Na prática, use `echo` — é ligeiramente mais rápido e mais flexível; `print` aparece por herança histórica da linguagem.

## Erros comuns

- Esquecer o `;` no fim de uma instrução.
- Esquecer a tag de abertura `<?php` — sem ela, o servidor trata o arquivo inteiro como texto puro, exibindo o código PHP literalmente na página em vez de executá-lo.
- Fechar a tag `?>` com espaço ou quebra de linha depois dela em arquivos que serão incluídos em outros (ver [[12-Tratamento-de-Erros]] mais adiante) — causa o clássico erro "headers already sent".

## Exercício

Altere `03_ola_mundo.php` para exibir seu nome em uma linha e uma frase sobre por que está aprendendo PHP em outra (dois `echo`, ou um `echo` com quebra de linha usando `\n` dentro de aspas duplas — veja mais sobre isso em [[09-Strings]]).

## Perguntas de revisão

Qual a instrução mais comum para gerar saída em PHP? :: echo, que não exige parênteses.

O ponto e vírgula é obrigatório em PHP? :: Sim, no fim de toda instrução, sem exceção.

Por que não fechar a tag ?> em arquivos só com PHP? :: Para evitar espaços acidentais depois dela, que causam o erro headers already sent.

O que acontece se faltar a tag <?php? :: O servidor trata o arquivo como texto e exibe o código em vez de executá-lo.

Quais as formas de comentário em PHP? :: // ou # para uma linha, e /* */ para várias linhas.

---
Veja o exemplo em `PHP/exemplos/03_ola_mundo.php`. Próxima nota: [[04-Variaveis-e-Tipos]]
