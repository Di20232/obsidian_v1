---
tags: [sqlite, sql, flashcards]
cssclasses: [cerebro-nota, cerebro-sqlite]
---

# Tipos Dinâmicos e Tabelas

## A diferença mais importante em relação ao MySQL

Em [[../MySQL/03-Criando-Bancos-e-Tabelas]], cada coluna tem um tipo **rígido** (`VARCHAR(100)`, `INT`, `DECIMAL(10,2)`) — o MySQL recusa (ou converte à força) um valor que não bate com o tipo declarado. **SQLite funciona diferente**: ele usa **tipagem dinâmica por valor**, parecido com o que você já viu em variáveis de Python ([[../Python/04-Variaveis-e-Tipos]]) — uma coluna pode, tecnicamente, guardar qualquer tipo de dado, independente do que foi declarado na criação da tabela.

```sql
CREATE TABLE exemplo (
    id INTEGER PRIMARY KEY,
    valor TEXT
);

INSERT INTO exemplo (valor) VALUES ('um texto');
INSERT INTO exemplo (valor) VALUES (123);         -- SQLite aceita, mesmo a coluna sendo TEXT
```

**Isso não significa que tipos não importam** — o tipo declarado ainda serve como uma "sugestão forte" (chamada de **type affinity**) que orienta como o SQLite armazena e compara os dados; só não é uma trava absoluta como no MySQL.

## As 5 classes de armazenamento do SQLite

Diferente da lista longa de tipos do MySQL ([[../MySQL/03-Criando-Bancos-e-Tabelas]]), SQLite tem só 5 categorias internas:

| Classe | Equivalente aproximado |
|---|---|
| `NULL` | ausência de valor |
| `INTEGER` | números inteiros |
| `REAL` | números de ponto flutuante |
| `TEXT` | texto |
| `BLOB` | dados binários (imagens, arquivos) |

Você ainda pode escrever `VARCHAR(100)`, `DECIMAL(10,2)` etc. ao criar uma tabela (por compatibilidade e clareza para quem lê) — o SQLite aceita a sintaxe, mas internamente mapeia tudo para uma dessas 5 classes.

## Criando uma tabela

```sql
CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT,
    ano_publicacao INTEGER
);
```

Quase idêntico a [[../MySQL/03-Criando-Bancos-e-Tabelas]] — a diferença mais visível é `INTEGER PRIMARY KEY AUTOINCREMENT` no lugar de `INT AUTO_INCREMENT PRIMARY KEY` (ordem das palavras e nome ligeiramente diferentes).

## Chaves estrangeiras: precisam ser ativadas manualmente

```sql
PRAGMA foreign_keys = ON;   -- precisa rodar isso a cada conexão! não é o padrão

CREATE TABLE emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro_id INTEGER,
    nome_leitor TEXT NOT NULL,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

**Diferença importante em relação ao MySQL**: por razões históricas, SQLite **não verifica** chaves estrangeiras por padrão — `PRAGMA foreign_keys = ON;` precisa ser executado em **cada conexão** para ativar essa checagem (o `PRAGMA` é um comando específico de configuração do SQLite, sem equivalente direto no padrão SQL).

## Exercício

Crie uma tabela `produtos` (id, nome, preco) no SQLite. Tente inserir um valor de texto na coluna `preco` (que você declarou como `REAL`) e observe que o SQLite aceita, diferente do que aconteceria em MySQL — reflita sobre por que essa flexibilidade pode ser útil, e também por que pode ser perigosa se você não validar os dados na aplicação.

## Perguntas de revisão

Como funciona a tipagem de colunas no SQLite? :: É dinâmica por valor: a coluna aceita qualquer tipo, e o tipo declarado é só uma afinidade que orienta o armazenamento.

Quais são as 5 classes de armazenamento do SQLite? :: NULL, INTEGER, REAL, TEXT e BLOB.

Como se escreve a chave primária autoincrementada no SQLite? :: INTEGER PRIMARY KEY AUTOINCREMENT.

O SQLite verifica chaves estrangeiras por padrão? :: Não; é preciso rodar PRAGMA foreign_keys = ON a cada conexão.

Por que a tipagem flexível do SQLite pode ser perigosa? :: Porque aceita, por exemplo, texto numa coluna de preço; a aplicação precisa validar os dados.

---
Veja o exemplo em `SQLite/exemplos/03_tipos_tabelas.py`. Próxima nota: [[04-CRUD-Basico]]
