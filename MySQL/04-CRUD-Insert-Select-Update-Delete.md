---
tags: [mysql, sql]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# CRUD: Insert, Select, Update, Delete

## O que é CRUD

**CRUD** é um acrônimo para as quatro operações fundamentais que qualquer sistema faz com dados: **C**reate (criar), **R**ead (ler), **U**pdate (atualizar), **D**elete (apagar). Em SQL, cada uma tem seu próprio comando — e são, de longe, os comandos mais usados no dia a dia.

## Create: `INSERT`

```sql
INSERT INTO clientes (nome, email, idade) VALUES ('Diego', 'diego@exemplo.com', 25);

-- Inserindo várias linhas de uma vez
INSERT INTO clientes (nome, email, idade) VALUES
    ('Ana', 'ana@exemplo.com', 30),
    ('Bruno', 'bruno@exemplo.com', 22);
```

Repare que `id` **não** foi informado — como ele é `AUTO_INCREMENT` (visto em [[03-Criando-Bancos-e-Tabelas]]), o MySQL gera esse valor sozinho.

## Read: `SELECT`

```sql
SELECT * FROM clientes;                    -- todas as colunas, todas as linhas
SELECT nome, email FROM clientes;            -- só essas colunas
SELECT * FROM clientes WHERE idade >= 18;    -- com filtro (aprofundado em [[05-Where-Order-Limit]])
```

## Update: `UPDATE`

```sql
UPDATE clientes SET idade = 26 WHERE nome = 'Diego';

UPDATE clientes SET idade = idade + 1 WHERE id = 1;  -- pode usar o valor atual no cálculo
```

**O `WHERE` não é opcional na prática, mesmo sendo opcional na sintaxe**: `UPDATE clientes SET idade = 0;` sem `WHERE` altera **todas** as linhas da tabela de uma vez — um dos erros mais caros e mais citados na carreira de qualquer pessoa que mexe com bancos de dados, já alertado em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]].

## Delete: `DELETE`

```sql
DELETE FROM clientes WHERE id = 3;

DELETE FROM clientes;    -- apaga TODAS as linhas, mas mantém a tabela (estrutura intacta)
```

Mesmo alerta do `UPDATE`: `DELETE` sem `WHERE` apaga tudo. Diferente de `DROP TABLE` ([[03-Criando-Bancos-e-Tabelas]]), a tabela em si continua existindo, só fica vazia.

## Um hábito de segurança: teste o filtro com `SELECT` antes

Antes de rodar um `UPDATE`/`DELETE` com um `WHERE` que você não tem 100% de certeza, rode o **mesmo filtro** com `SELECT` primeiro, para conferir exatamente quais linhas seriam afetadas:

```sql
-- Primeiro, confira:
SELECT * FROM clientes WHERE idade < 18;

-- Só depois de confirmar que é isso mesmo, rode:
DELETE FROM clientes WHERE idade < 18;
```

## `REPLACE` e `INSERT ... ON DUPLICATE KEY UPDATE`: inserir ou atualizar

```sql
INSERT INTO clientes (id, nome, email, idade) VALUES (1, 'Diego Souza', 'diego@exemplo.com', 26)
ON DUPLICATE KEY UPDATE nome = 'Diego Souza', idade = 26;
```

Se já existir uma linha com esse `id` (ou outra coluna `UNIQUE`), atualiza em vez de tentar inserir duplicado e falhar. Útil para operações de "criar se não existir, senão atualizar" — um padrão comum chamado **upsert**.

## Exercício

Na tabela `livros` criada em [[03-Criando-Bancos-e-Tabelas]], insira 4 livros. Atualize o ano de publicação de um deles. Apague um livro específico pelo `id`. Confira o resultado final com `SELECT * FROM livros;` depois de cada passo.

---
Veja o exemplo em `MySQL/exemplos/04_crud.sql`. Próxima nota: [[05-Where-Order-Limit]]
