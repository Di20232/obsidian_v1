---
tags: [php, banco-de-dados]
cssclasses: [cerebro-nota, cerebro-php]
---

# PHP com Banco de Dados (PDO)

## Fechando o ciclo: servidor + banco de dados

Você já viu como PHP gera páginas dinamicamente ([[01-O-que-e-PHP]]) e recebe dados do usuário ([[11-Formularios-e-Superglobais]]). A peça que falta é **guardar e consultar dados permanentemente** — o papel de um banco de dados, conceito geral visto em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]], com trilhas completas em [[../MySQL/00-Indice]] e [[../SQLite/00-Indice]].

## PDO: uma interface única para vários bancos

PHP tem várias formas históricas de conectar a bancos (`mysqli`, específica do MySQL), mas a recomendada hoje é **PDO** (PHP Data Objects) — uma interface **genérica**, que funciona com MySQL, SQLite, PostgreSQL e outros, trocando só a "string de conexão". Isso é parecido com o papel do `sqlite3` em Python ([[../Python/09-Listas-Tuplas-Dicionarios]] menciona bancos; [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]] aprofunda), mas PDO cobre múltiplos motores com a mesma API.

## Conectando

```php
<?php
// SQLite (arquivo único, sem servidor — ver [[../SQLite/00-Indice]])
$pdo = new PDO("sqlite:banco.db");

// MySQL (precisa de um servidor rodando — ver [[../MySQL/00-Indice]])
$pdo = new PDO("mysql:host=localhost;dbname=meu_banco", "usuario", "senha");

$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);  // faz erros de SQL virarem exceções capturáveis
```

## Criando uma tabela e inserindo dados

```php
$pdo->exec("CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
)");

$stmt = $pdo->prepare("INSERT INTO usuarios (nome, idade) VALUES (?, ?)");
$stmt->execute(["Diego", 25]);
```

**`prepare()` + `execute()` com `?`**: os valores são passados **separadamente** da instrução SQL, nunca coladas diretamente na string. Isso é chamado de **prepared statement**, e é a defesa padrão contra **SQL injection** — o mesmo risco de segurança já mencionado em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]] e [[../Programacao-Geral/13-Boas-Praticas-de-Codigo]]. **Nunca** monte uma query concatenando `$_POST` diretamente:

```php
// NUNCA FAÇA ISSO — vulnerável a SQL injection
$pdo->exec("INSERT INTO usuarios (nome) VALUES ('" . $_POST['nome'] . "')");

// Faça isso: dado sempre passa como parâmetro, nunca colado na string
$stmt = $pdo->prepare("INSERT INTO usuarios (nome) VALUES (?)");
$stmt->execute([$_POST['nome']]);
```

## Consultando dados

```php
$stmt = $pdo->prepare("SELECT * FROM usuarios WHERE idade >= ?");
$stmt->execute([18]);

$usuarios = $stmt->fetchAll(PDO::FETCH_ASSOC);   // devolve um array de arrays associativos

foreach ($usuarios as $usuario) {
    echo "{$usuario['nome']}, {$usuario['idade']} anos\n";
}
```

`PDO::FETCH_ASSOC` faz cada linha do resultado virar um **array associativo** (visto em [[08-Arrays]]) — a mesma forma de representar "uma linha de tabela" já vista em Python ([[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]]) e no formato JSON típico de APIs ([[../Programacao-Geral/10-Como-a-Web-Funciona]]).

## Parâmetros nomeados: mais legível que `?` em queries longas

```php
$stmt = $pdo->prepare("INSERT INTO usuarios (nome, idade) VALUES (:nome, :idade)");
$stmt->execute(["nome" => "Ana", "idade" => 30]);
```

## Juntando com formulário (fechando o ciclo completo)

```php
<?php
// processar_cadastro.php
session_start();
$pdo = new PDO("sqlite:banco.db");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$nome = $_POST['nome'] ?? '';
$idade = (int) ($_POST['idade'] ?? 0);

try {
    $stmt = $pdo->prepare("INSERT INTO usuarios (nome, idade) VALUES (?, ?)");
    $stmt->execute([$nome, $idade]);
    echo "Cadastrado com sucesso!";
} catch (PDOException $erro) {
    echo "Erro ao cadastrar: " . $erro->getMessage();
}
```

Este é o ciclo completo de uma aplicação web tradicional: **formulário** ([[11-Formularios-e-Superglobais]]) → **PHP recebe e valida** → **PDO guarda no banco** → **resposta ao navegador**. É exatamente isso que roda por trás de praticamente qualquer site com cadastro, login ou comentários.

## Exercício

Crie uma tabela `tarefas` (id, descricao, concluida) em um banco SQLite via PDO. Escreva um script que insira 3 tarefas e depois consulte e exiba só as não concluídas.

---
Veja o exemplo em `PHP/exemplos/14_banco_dados.php`. Próxima nota: [[15-Boas-Praticas-e-Proximos-Passos]]
