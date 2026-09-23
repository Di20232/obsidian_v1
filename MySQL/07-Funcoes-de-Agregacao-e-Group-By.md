---
tags: [mysql, sql, flashcards]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# Funções de Agregação e GROUP BY

## O problema que isso resolve

Até aqui, todo `SELECT` devolveu linhas individuais. Frequentemente você quer um **resumo**: quantos clientes existem, qual o valor total de vendas, a média de idade. **Funções de agregação** calculam um único valor a partir de várias linhas.

## As funções principais

```sql
SELECT COUNT(*) FROM clientes;              -- quantas linhas existem
SELECT SUM(valor) FROM pedidos;                -- soma de uma coluna
SELECT AVG(idade) FROM clientes;                -- média
SELECT MIN(idade) FROM clientes;                -- menor valor
SELECT MAX(idade) FROM clientes;                -- maior valor
```

`COUNT(*)` conta **linhas**; `COUNT(coluna)` conta linhas onde aquela coluna **não é `NULL`** — uma diferença sutil, mas real, entre os dois usos.

## `GROUP BY`: agregando **por grupo**, não a tabela inteira

```sql
SELECT cliente_id, COUNT(*) AS total_pedidos
FROM pedidos
GROUP BY cliente_id;
```

Sem `GROUP BY`, `COUNT(*)` conta a tabela inteira, dando um único número. Com `GROUP BY cliente_id`, o MySQL **separa as linhas em grupos** (um grupo por valor distinto de `cliente_id`) e aplica a função de agregação **dentro de cada grupo**, devolvendo uma linha de resultado por grupo. É o equivalente SQL de "para cada X, quantos Y existem".

`AS total_pedidos` cria um **alias** para a coluna resultante — sem ele, a coluna apareceria com um nome pouco legível como `COUNT(*)`.

## Exemplo mais completo

```sql
SELECT c.nome, COUNT(p.id) AS quantidade_pedidos, SUM(p.valor) AS total_gasto
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome
ORDER BY total_gasto DESC;
```

Isso responde, de uma vez: "para cada cliente, quantos pedidos ele fez e quanto gastou no total, do que mais gastou para o que menos gastou" — o tipo de pergunta que aparece o tempo todo em relatórios e painéis administrativos reais. Repare no `LEFT JOIN` (visto em [[06-Joins]]): garante que clientes **sem nenhum pedido** também apareçam, com `quantidade_pedidos = 0`.

## `HAVING`: filtrando **depois** de agregar

```sql
SELECT cliente_id, COUNT(*) AS total_pedidos
FROM pedidos
GROUP BY cliente_id
HAVING total_pedidos > 1;
```

**Por que não usar `WHERE` aqui**: `WHERE` filtra linhas **antes** de agrupar, e não pode referenciar o resultado de uma função de agregação (`COUNT(*)` ainda não existe nesse ponto da execução). `HAVING` filtra **depois** do `GROUP BY`, quando os totais já foram calculados — por isso existe uma cláusula separada só para esse caso.

## Ordem completa de execução lógica de uma consulta

Vale entender a ordem real, mesmo escrevendo na ordem sintática de [[05-Where-Order-Limit]]:

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

`WHERE` age antes de agrupar (linha a linha); `HAVING` age depois (grupo a grupo). Essa distinção é a fonte mais comum de confusão para quem está aprendendo `GROUP BY`.

## Exercício

Na tabela `emprestimos` criada em [[06-Joins]], escreva uma consulta que mostre quantos empréstimos cada `nome_leitor` fez, ordenado do maior para o menor número de empréstimos, usando `GROUP BY`. Depois, adicione um `HAVING` para mostrar só leitores com mais de 1 empréstimo.

## Perguntas de revisão

Quais são as funções de agregação principais? :: COUNT, SUM, AVG, MIN e MAX.

Qual a diferença entre COUNT(*) e COUNT(coluna)? :: COUNT(*) conta linhas; COUNT(coluna) conta só as linhas em que a coluna não é NULL.

O que faz GROUP BY? :: Separa as linhas em grupos por valor e aplica a agregação dentro de cada grupo, devolvendo uma linha por grupo.

Qual a diferença entre WHERE e HAVING? :: WHERE filtra linhas antes de agrupar; HAVING filtra grupos depois da agregação.

Qual a ordem lógica de execução de uma consulta SQL? :: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY e LIMIT.

---
Veja o exemplo em `MySQL/exemplos/07_agregacao.sql`. Próxima nota: [[08-Subconsultas-e-Indices]]
