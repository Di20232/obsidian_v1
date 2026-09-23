---
tags: [mysql, sql]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# WHERE, ORDER BY e LIMIT

## `WHERE`: filtrando resultados

Já visto brevemente em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]] e [[04-CRUD-Insert-Select-Update-Delete]] — aqui, em profundidade.

```sql
SELECT * FROM clientes WHERE idade >= 18;
SELECT * FROM clientes WHERE nome = 'Diego';
SELECT * FROM clientes WHERE idade > 18 AND idade < 65;   -- combinando condições
SELECT * FROM clientes WHERE idade < 18 OR idade > 65;
SELECT * FROM clientes WHERE NOT idade = 25;
```

Mesma lógica de condições vista em [[../Python/07-Condicionais]] e [[../PHP/06-Condicionais]] — `AND`, `OR`, `NOT` funcionam com o mesmo significado.

## Operadores úteis específicos de filtro

```sql
SELECT * FROM clientes WHERE idade BETWEEN 18 AND 65;      -- intervalo, incluindo os limites
SELECT * FROM clientes WHERE nome IN ('Diego', 'Ana', 'Bruno');  -- qualquer um destes valores
SELECT * FROM clientes WHERE email LIKE '%@gmail.com';       -- padrão de texto -> % é qualquer sequência
SELECT * FROM clientes WHERE telefone IS NULL;                 -- checando valor vazio (NÃO use = NULL!)
SELECT * FROM clientes WHERE telefone IS NOT NULL;
```

**Atenção com `NULL`**: em SQL, `NULL` representa "ausência de valor" e tem uma regra especial — `coluna = NULL` **nunca** é verdadeiro, nem para linhas com `NULL` de fato. Sempre use `IS NULL` / `IS NOT NULL` para checar isso, nunca `=`.

`LIKE` com `%` é o operador de busca por padrão de texto — `%` significa "qualquer sequência de caracteres, inclusive vazia". `_` (underscore) significa "exatamente um caractere qualquer".

## `ORDER BY`: ordenando resultados

```sql
SELECT * FROM clientes ORDER BY idade;             -- crescente (padrão)
SELECT * FROM clientes ORDER BY idade DESC;         -- decrescente
SELECT * FROM clientes ORDER BY idade, nome;         -- critério de desempate: se a idade for igual, ordena por nome
```

## `LIMIT`: restringindo a quantidade de resultados

```sql
SELECT * FROM clientes ORDER BY idade DESC LIMIT 5;         -- só os 5 mais velhos
SELECT * FROM clientes ORDER BY idade DESC LIMIT 5 OFFSET 10; -- pula os 10 primeiros, pega os próximos 5
```

`LIMIT` é fundamental em qualquer sistema real: buscar "todos os clientes" de uma tabela com milhões de linhas é, na prática, sempre paginado — o padrão `LIMIT ... OFFSET ...` é o que implementa a paginação ("página 1", "página 2"...) que você vê em qualquer lista longa na web.

## Juntando tudo: um exemplo completo

```sql
SELECT nome, idade, email
FROM clientes
WHERE idade >= 18 AND email LIKE '%@gmail.com'
ORDER BY idade DESC
LIMIT 10;
```

**Ordem de escrita obrigatória**: `SELECT` → `FROM` → `WHERE` → `ORDER BY` → `LIMIT`. Trocar essa ordem gera erro de sintaxe — diferente de Python/JavaScript, SQL exige as cláusulas em uma sequência fixa.

## `DISTINCT`: eliminando duplicatas

```sql
SELECT DISTINCT cidade FROM clientes;   -- lista cada cidade uma única vez, mesmo com vários clientes na mesma cidade
```

## Exercício

Na tabela `livros`, escreva uma consulta que retorne todos os livros publicados depois de 1900, ordenados do mais recente para o mais antigo, trazendo só as 2 primeiras linhas. Depois, escreva uma consulta usando `LIKE` para encontrar livros cujo título contenha a palavra "Sertão".

---
Veja o exemplo em `MySQL/exemplos/05_where_order_limit.sql`. Próxima nota: [[06-Joins]]
