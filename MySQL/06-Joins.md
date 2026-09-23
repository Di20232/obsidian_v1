---
tags: [mysql, sql, flashcards]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# Joins

## O problema que isso resolve

Lembrando [[03-Criando-Bancos-e-Tabelas]]: dados relacionados vivem em tabelas **separadas**, ligadas por chave estrangeira, para evitar duplicação (o princípio de **normalização** mencionado em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]]). Um `JOIN` é o comando que **combina** linhas de tabelas diferentes em um único resultado, baseado em como elas se relacionam.

## Tabelas de exemplo para esta nota

```sql
CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100));
CREATE TABLE pedidos (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100));

INSERT INTO clientes VALUES (1, 'Diego'), (2, 'Ana'), (3, 'Bruno');
INSERT INTO pedidos VALUES (1, 1, 'Notebook'), (2, 1, 'Mouse'), (3, 2, 'Teclado');
```

Repare: `Bruno` (id 3) **não tem nenhum pedido** — isso importa para entender a diferença entre os tipos de `JOIN` abaixo.

## `INNER JOIN`: só o que existe nos dois lados

```sql
SELECT clientes.nome, pedidos.produto
FROM pedidos
INNER JOIN clientes ON pedidos.cliente_id = clientes.id;
```

Resultado: `Diego/Notebook`, `Diego/Mouse`, `Ana/Teclado`. **Bruno não aparece**, porque não tem nenhuma linha correspondente em `pedidos` — `INNER JOIN` só traz combinações onde a condição do `ON` é satisfeita **dos dois lados**.

## `LEFT JOIN`: tudo da tabela da esquerda, mesmo sem correspondência

```sql
SELECT clientes.nome, pedidos.produto
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;
```

Resultado: `Diego/Notebook`, `Diego/Mouse`, `Ana/Teclado`, **`Bruno/NULL`**. `LEFT JOIN` traz **todas** as linhas da tabela à esquerda do `JOIN` (`clientes`, porque está no `FROM`), preenchendo com `NULL` onde não há correspondência na tabela da direita. Extremamente útil para perguntas do tipo "quais clientes **nunca** fizeram pedido":

```sql
SELECT clientes.nome
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
WHERE pedidos.id IS NULL;   -- só as linhas onde o LEFT JOIN não achou correspondência
```

## `RIGHT JOIN`: o espelho do `LEFT JOIN`

```sql
SELECT clientes.nome, pedidos.produto
FROM pedidos
RIGHT JOIN clientes ON pedidos.cliente_id = clientes.id;
```

Traz todas as linhas da tabela à **direita** (`clientes`), mesmo sem correspondência à esquerda. Na prática, qualquer `RIGHT JOIN` pode ser reescrito como `LEFT JOIN` trocando a ordem das tabelas — por isso `RIGHT JOIN` é usado bem menos no dia a dia.

## Alias: encurtando nomes de tabela

```sql
SELECT c.nome, p.produto
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id;
```

`clientes c` e `pedidos p` criam **apelidos** (`c`, `p`) para as tabelas, evitando repetir o nome inteiro em cada referência — muito comum em consultas com várias tabelas.

## Juntando 3 ou mais tabelas

```sql
SELECT c.nome, p.produto, i.quantidade
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
JOIN itens_pedido i ON p.id = i.pedido_id;
```

Cada `JOIN` adicional encadeia mais uma tabela ao resultado — comum em sistemas reais, onde dados relevantes costumam estar espalhados em várias tabelas relacionadas.

## Exercício

Usando as tabelas `livros` e `emprestimos` criadas em [[03-Criando-Bancos-e-Tabelas]], insira alguns empréstimos e escreva uma consulta com `JOIN` que mostre o título do livro junto com o nome de quem pegou emprestado. Depois, escreva uma consulta com `LEFT JOIN` que mostre **todos** os livros, incluindo os que nunca foram emprestados.

## Perguntas de revisão

Qual a diferença entre INNER JOIN e LEFT JOIN? :: INNER JOIN traz só as linhas com correspondência nos dois lados; LEFT JOIN traz todas da esquerda, com NULL onde não há correspondência.

Como achar clientes que nunca fizeram pedido? :: LEFT JOIN de clientes com pedidos e WHERE pedidos.id IS NULL.

Por que RIGHT JOIN é pouco usado? :: Porque qualquer RIGHT JOIN pode ser reescrito como LEFT JOIN trocando a ordem das tabelas.

Para que servem alias de tabela como clientes c? :: Para encurtar os nomes nas referências, muito útil com várias tabelas.

Por que dados ficam em tabelas separadas ligadas por chave? :: Por normalização, para evitar duplicação; o JOIN recombina as tabelas na consulta.

---
Veja o exemplo em `MySQL/exemplos/06_joins.sql`. Próxima nota: [[07-Funcoes-de-Agregacao-e-Group-By]]
