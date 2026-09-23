---
tags: [sqlite, sql]
cssclasses: [cerebro-nota, cerebro-sqlite]
---

# CRUD Básico

## A boa notícia: a sintaxe é quase idêntica à do MySQL

Tudo que você aprendeu em [[../MySQL/04-CRUD-Insert-Select-Update-Delete]], [[../MySQL/05-Where-Order-Limit]] e [[../MySQL/06-Joins]] funciona **praticamente sem alteração** em SQLite — porque ambos implementam o mesmo padrão SQL, discutido em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]]. Esta nota é mais curta de propósito: o objetivo é confirmar que você já sabe fazer isso, e destacar só as diferenças reais.

## Create, Read, Update, Delete

```sql
INSERT INTO livros (titulo, autor, ano_publicacao) VALUES ('Dom Casmurro', 'Machado de Assis', 1899);

SELECT * FROM livros WHERE ano_publicacao > 1900;

UPDATE livros SET ano_publicacao = 1900 WHERE titulo = 'Dom Casmurro';

DELETE FROM livros WHERE id = 1;
```

Idêntico ao MySQL. `WHERE`, `ORDER BY`, `LIMIT`, `JOIN`, `GROUP BY` — tudo funciona do mesmo jeito.

## Diferenças reais a notar

- **`AUTOINCREMENT`** (uma palavra só) em vez de `AUTO_INCREMENT` do MySQL.
- **`LIMIT` com `OFFSET`** funciona igual, mas SQLite também aceita uma forma abreviada: `LIMIT 5, 10` (pula 5, pega 10) — evite essa forma abreviada por clareza, prefira sempre `LIMIT 10 OFFSET 5`, mais legível e mais parecida com o padrão usado em MySQL.
- **Não existe `RIGHT JOIN`** em versões mais antigas de SQLite (foi adicionado só recentemente) — historicamente, sempre se usa `LEFT JOIN` trocando a ordem das tabelas, como já era recomendado em [[../MySQL/06-Joins]].
- **Funções de data são diferentes**: SQLite usa `date('now')`, `datetime('now')` — sintaxe própria, sem equivalência direta com `NOW()` do MySQL.

```sql
SELECT date('now');           -- data atual, formato YYYY-MM-DD
SELECT datetime('now');        -- data e hora atual
```

## `INSERT OR REPLACE`: o "upsert" do SQLite

```sql
INSERT OR REPLACE INTO livros (id, titulo, autor, ano_publicacao)
VALUES (1, 'Dom Casmurro', 'Machado de Assis', 1900);
```

Equivalente ao `INSERT ... ON DUPLICATE KEY UPDATE` do MySQL ([[../MySQL/04-CRUD-Insert-Select-Update-Delete]]), mas com sintaxe mais direta — se já existir uma linha com essa chave primária, ela é **substituída inteira**, não só os campos informados.

## Exercício

Recrie a tabela `livros` (id, titulo, autor, ano_publicacao) e a tabela `emprestimos` (id, livro_id, nome_leitor) em SQLite — praticamente copiando o SQL de [[../MySQL/03-Criando-Bancos-e-Tabelas]], ajustando só `AUTOINCREMENT`. Insira alguns dados e refaça o exercício de `JOIN` de [[../MySQL/06-Joins]] aqui, confirmando que o resultado é o mesmo.

---
Veja o exemplo em `SQLite/exemplos/04_crud.py`. Próxima nota: [[05-SQLite-com-Python-e-PHP]]
