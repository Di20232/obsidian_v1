---
tags: [mysql, php, python, flashcards]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# MySQL com PHP e Python

## Fechando o ciclo: banco de dados + código de aplicação

Você já sabe escrever SQL puro. Na prática, quase sempre esse SQL é disparado **a partir de código**, não digitado manualmente — um usuário preenche um formulário, o código monta e executa a consulta, o resultado vira uma resposta na tela. Esta nota conecta o que você aprendeu aqui com as trilhas de [[../PHP/00-Indice|PHP]] e [[../Python/00-Indice|Python]].

## Conectando a partir de PHP (PDO)

Já visto em profundidade em [[../PHP/14-PHP-com-Banco-de-Dados]] — aqui, especificamente para MySQL:

```php
<?php
$pdo = new PDO("mysql:host=localhost;dbname=biblioteca;charset=utf8mb4", "app_biblioteca", "senha_forte_aqui");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$stmt = $pdo->prepare("SELECT * FROM livros WHERE ano_publicacao > ?");
$stmt->execute([1900]);

foreach ($stmt->fetchAll(PDO::FETCH_ASSOC) as $livro) {
    echo "{$livro['titulo']} ({$livro['ano_publicacao']})\n";
}
```

`charset=utf8mb4` na string de conexão evita problemas de acentuação com texto em português — um detalhe específico de MySQL que vale sempre incluir.

## Conectando a partir de Python

Diferente do `sqlite3`, que já vem embutido no Python ([[../Python/09-Listas-Tuplas-Dicionarios]]), conectar a MySQL exige um pacote de terceiros (conceito de `pip install`, visto em [[../Python/12-Modulos-e-Pacotes]]):

```bash
pip install mysql-connector-python
```

```python
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="app_biblioteca",
    password="senha_forte_aqui",
    database="biblioteca"
)
cursor = conexao.cursor(dictionary=True)  # dictionary=True: cada linha vira um dicionário, não uma tupla

cursor.execute("SELECT * FROM livros WHERE ano_publicacao > %s", (1900,))
for livro in cursor.fetchall():
    print(f"{livro['titulo']} ({livro['ano_publicacao']})")

conexao.close()
```

Repare: PHP/PDO usa `?` como marcador de parâmetro ([[../PHP/14-PHP-com-Banco-de-Dados]]); o conector MySQL de Python usa `%s` — **sempre** um marcador, nunca concatenação direta, pela mesma razão de segurança (SQL injection) já reforçada em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]] e [[../PHP/14-PHP-com-Banco-de-Dados]].

## Encerrando conexões

Tanto em PHP quanto em Python, a conexão com o banco é um recurso que deve ser **liberado** depois de usado — mesmo princípio do `with open(...)` de arquivos em Python ([[../Python/14-Arquivos]]) e do `$pdo` sendo destruído automaticamente ao fim do script em PHP. Em scripts curtos isso acontece sozinho ao terminar o programa; em aplicações de longa duração (um servidor rodando continuamente), fechar conexões explicitamente evita esgotar o limite de conexões simultâneas que o MySQL aceita.

## ORMs: uma camada acima do SQL manual

Em projetos maiores, é comum usar um **ORM** (Object-Relational Mapper) — uma biblioteca que permite trabalhar com tabelas como se fossem classes/objetos, gerando o SQL por trás automaticamente:
- PHP: **Eloquent** (parte do framework Laravel, mencionado em [[../PHP/15-Boas-Praticas-e-Proximos-Passos]]).
- Python: **SQLAlchemy** ou o ORM embutido do **Django**.

```python
# Exemplo conceitual de SQLAlchemy, para reconhecimento
livro = Livro.query.filter(Livro.ano_publicacao > 1900).all()
```

Um ORM não substitui saber SQL — ele só evita escrever manualmente as consultas mais repetitivas; entender o SQL por trás continua essencial para depurar problemas de performance (ver [[08-Subconsultas-e-Indices]]).

## Exercício

Escreva um script em PHP **ou** Python que se conecte ao banco `biblioteca`, insira um novo livro recebido como entrada (`$_POST` em PHP, ou `input()`/argumento de linha de comando em Python), e liste todos os livros depois da inserção.

## Perguntas de revisão

Por que usar charset=utf8mb4 na conexão MySQL? :: Para evitar problemas de acentuação com texto em português.

Qual marcador de parâmetro o conector MySQL do Python usa? :: %s, enquanto o PDO do PHP usa ?; nos dois casos nunca se concatena o valor.

O que faz cursor(dictionary=True) no Python? :: Faz cada linha vir como dicionário em vez de tupla.

O que é um ORM? :: Uma biblioteca que trata tabelas como classes e gera o SQL automaticamente, como Eloquent e SQLAlchemy.

Por que fechar conexões com o banco? :: Para não esgotar o limite de conexões simultâneas em aplicações de longa duração.

---
Próxima nota: [[11-Boas-Praticas-e-Proximos-Passos]]
