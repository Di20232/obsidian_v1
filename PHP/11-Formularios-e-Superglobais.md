---
tags: [php, web]
cssclasses: [cerebro-nota, cerebro-php]
---

# Formulários e Superglobais

## O verdadeiro "entrada e saída" de PHP

Em Python, `input()` lê do terminal ([[../Python/06-Entrada-e-Saida]]). Em JavaScript, `prompt()` ou eventos do DOM leem do navegador ([[../JavaScript/16-DOM-e-Eventos]]). Em PHP, a forma mais comum de receber dados é através de uma **requisição HTTP** enviada por um formulário HTML — lembrando o modelo cliente-servidor de [[../Programacao-Geral/10-Como-a-Web-Funciona]]: o navegador (cliente) envia dados, o PHP (rodando no servidor) os recebe e processa.

## Superglobais: variáveis sempre disponíveis

PHP disponibiliza automaticamente, em qualquer script, variáveis especiais chamadas **superglobais** que carregam dados da requisição atual:

- `$_GET` — dados enviados na **URL** (`?nome=Diego&idade=25`), típico de links e buscas.
- `$_POST` — dados enviados no **corpo** da requisição, típico de formulários que criam/alteram algo (mesmos métodos HTTP vistos em [[../Programacao-Geral/10-Como-a-Web-Funciona]]).
- `$_SERVER` — informações sobre o servidor e a requisição (método usado, URL, etc.).
- `$_SESSION` — dados que persistem **entre requisições** do mesmo usuário (visto adiante nesta nota).

## Um formulário HTML simples

```html
<!-- formulario.html -->
<form action="processar.php" method="POST">
    <input type="text" name="nome" placeholder="Seu nome">
    <input type="number" name="idade" placeholder="Sua idade">
    <button type="submit">Enviar</button>
</form>
```

`action` diz para onde os dados vão; `method="POST"` diz como. Cada `name` de um campo (`nome`, `idade`) vira uma **chave** dentro de `$_POST` no arquivo de destino.

```php
<!-- processar.php -->
<?php
$nome = $_POST['nome'] ?? '';
$idade = $_POST['idade'] ?? '';

echo "Olá, $nome! Você tem $idade anos.";
```

Repare no uso do `??` (coalescência nula, visto em [[05-Operadores]]) — protege contra o caso de o campo não existir na requisição (por exemplo, se alguém acessar `processar.php` diretamente, sem passar pelo formulário).

## `$_GET`: dados na própria URL

```php
<!-- saudacao.php, acessado como saudacao.php?nome=Diego -->
<?php
$nome = $_GET['nome'] ?? 'visitante';
echo "Olá, $nome!";
```

Se você abrir `http://localhost:8000/saudacao.php?nome=Diego` no navegador (depois de rodar `php -S localhost:8000`, visto em [[02-Preparando-o-Ambiente]]), verá "Olá, Diego!". Isso é o motivo de URLs com `?algo=valor` funcionarem em sites reais.

## Sempre valide e trate dados vindos de fora

Conectando diretamente com [[../Programacao-Geral/13-Boas-Praticas-de-Codigo]]: **nunca confie em `$_GET`/`$_POST` sem checar**. Qualquer pessoa pode enviar qualquer coisa nesses campos, inclusive tentando quebrar o sistema:

```php
$idade = (int) ($_POST['idade'] ?? 0);   // força para número, evita texto malicioso onde se espera número

if ($idade < 0 || $idade > 120) {
    echo "Idade inválida";
} else {
    echo "Idade registrada: $idade";
}
```

**Nunca insira `$_GET`/`$_POST` direto em uma consulta SQL** sem usar parâmetros — isso é a porta de entrada clássica para SQL injection, já mencionado em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]] e retomado com PDO em [[14-PHP-com-Banco-de-Dados]].

## `$_SESSION`: lembrando o usuário entre páginas

HTTP é, por natureza, **sem estado** — cada requisição é isolada, o servidor não "lembra" sozinho quem fez a requisição anterior. `$_SESSION` resolve isso guardando dados do lado do servidor, associados a um visitante específico através de um cookie automático:

```php
<?php
session_start();   // sempre a primeira coisa no arquivo, antes de qualquer saída

$_SESSION['nome'] = 'Diego';   // guarda um dado na sessão
```

```php
<!-- em outra página, outra requisição -->
<?php
session_start();

echo "Bem-vindo de volta, " . ($_SESSION['nome'] ?? 'visitante');
```

Isso é a base de como um site "lembra" que você está logado entre uma página e outra.

## Exercício

Crie `formulario.html` com campos de nome e idade, e `processar.php` que recebe e exibe os dois, validando que a idade é um número entre 0 e 120. Rode `php -S localhost:8000` na pasta e teste pelo navegador.

---
Veja o exemplo em `PHP/exemplos/11_formulario.html` + `PHP/exemplos/11_processar.php`. Próxima nota: [[12-Tratamento-de-Erros]]
