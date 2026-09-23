---
tags: [sqlite, python, php]
cssclasses: [cerebro-nota, cerebro-sqlite]
---

# SQLite com Python e PHP

## Com Python: já embutido, sem instalar nada

Você já usou isso em todos os exemplos desta trilha — vale consolidar o padrão completo:

```python
import sqlite3

conexao = sqlite3.connect("biblioteca.db")   # cria o arquivo se não existir
conexao.row_factory = sqlite3.Row              # faz cada linha se comportar como um dicionário
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY, titulo TEXT)")
cursor.execute("INSERT INTO livros (titulo) VALUES (?)", ("Dom Casmurro",))
conexao.commit()   # necessário para gravar mudanças no arquivo — SQLite também usa transações!

cursor.execute("SELECT * FROM livros")
for linha in cursor.fetchall():
    print(linha["titulo"])   # acesso por nome de coluna, graças ao row_factory

conexao.close()
```

**`conexao.commit()` é obrigatório**: assim como MySQL ([[../MySQL/09-Transacoes-e-Usuarios]]), o Python agrupa operações em uma transação implícita — sem `commit()`, as mudanças **não são salvas** no arquivo `.db` de verdade (embora sejam visíveis dentro da mesma conexão, antes de fechar).

## Com PHP: através de PDO, mesma interface do MySQL

Já visto em [[../PHP/14-PHP-com-Banco-de-Dados]] — a vantagem de usar PDO é que a **mesma API** funciona tanto para SQLite quanto para MySQL, mudando só a string de conexão:

```php
<?php
$pdo = new PDO("sqlite:biblioteca.db");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$pdo->exec("CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY, titulo TEXT)");

$stmt = $pdo->prepare("INSERT INTO livros (titulo) VALUES (?)");
$stmt->execute(["Dom Casmurro"]);

$stmt = $pdo->query("SELECT * FROM livros");
foreach ($stmt->fetchAll(PDO::FETCH_ASSOC) as $livro) {
    echo $livro['titulo'] . "\n";
}
```

Repare: **PDO não exige `commit()` explícito** por padrão (diferente do `sqlite3` do Python) — cada `execute()` já é confirmado automaticamente, a menos que você use `beginTransaction()` explicitamente (visto em [[../MySQL/09-Transacoes-e-Usuarios]]) para agrupar várias operações.

## Onde o arquivo `.db` deve morar

Diferente de MySQL, onde os dados vivem "dentro" do servidor, o arquivo SQLite é só um arquivo comum — e isso traz uma responsabilidade: escolha o caminho com cuidado.
- Em desenvolvimento, é comum manter na própria pasta do projeto.
- Em produção, o arquivo deve ficar **fora** de qualquer pasta acessível publicamente pelo navegador (nunca dentro de uma pasta servida como `public/`) — do contrário, alguém poderia baixar o banco inteiro digitando a URL certa. Mesmo princípio de proteção de dados discutido em [[../Programacao-Geral/13-Boas-Praticas-de-Codigo]].
- O arquivo também deve constar no `.gitignore` ([[../Programacao-Geral/03-Git-e-Controle-de-Versao]]) se contiver dados reais — só a **estrutura** (schema), não os dados, geralmente é versionada, através de migrations (mencionadas em [[../MySQL/11-Boas-Praticas-e-Proximos-Passos]]).

## Banco em memória: útil para testes

```python
conexao = sqlite3.connect(":memory:")   # usado em todos os exemplos desta trilha
```

`:memory:` cria um banco que existe só enquanto o programa roda, sem nunca tocar o disco — extremamente rápido, e ideal para testes automatizados (ver [[../Programacao-Geral/12-Debugging-e-Testes]]), onde você quer um banco "limpo" a cada execução, sem deixar arquivos para trás.

## Exercício

Escreva um script em Python (ou PHP) que crie um arquivo `tarefas.db` real (não `:memory:`), insira 3 tarefas, feche a conexão, e depois **abra de novo** em um segundo script separado para confirmar que os dados persistiram no arquivo entre as duas execuções.

---
Veja o exemplo em `SQLite/exemplos/05_persistencia.py`. Próxima nota: [[06-SQLite-vs-MySQL]]
