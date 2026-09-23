---
tags: [mysql, sql, performance, flashcards]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# Subconsultas e Índices

## Subconsultas: um `SELECT` dentro de outro

Uma **subconsulta** (subquery) é um `SELECT` usado como parte de outra consulta — útil quando o filtro depende de um resultado que precisa ser calculado primeiro.

```sql
SELECT nome FROM clientes
WHERE id IN (SELECT cliente_id FROM pedidos WHERE valor > 1000);
```

Lê-se de dentro para fora: primeiro, `(SELECT cliente_id FROM pedidos WHERE valor > 1000)` roda e devolve uma lista de ids; depois, a consulta externa busca os clientes cujo `id` está nessa lista.

## Subconsulta que devolve um único valor

```sql
SELECT nome, valor FROM pedidos
WHERE valor > (SELECT AVG(valor) FROM pedidos);
```

Aqui a subconsulta devolve **um único número** (a média), usado diretamente na comparação — equivalente a "todos os pedidos com valor acima da média".

## Subconsulta correlacionada: referencia a consulta externa

```sql
SELECT c.nome FROM clientes c
WHERE EXISTS (
    SELECT 1 FROM pedidos p WHERE p.cliente_id = c.id
);
```

`EXISTS` checa só se a subconsulta **encontra alguma linha**, sem se importar com o valor em si — geralmente mais eficiente que `IN` para essa pergunta ("este cliente tem algum pedido?"). Isso é frequentemente reescrito como `JOIN` (visto em [[06-Joins]]) — ambos resolvem o mesmo problema, e a escolha entre eles costuma ser sobre legibilidade e performance.

## Índices: por que consultas ficam lentas em tabelas grandes

Sem um índice, o MySQL precisa examinar **linha por linha** para achar o que um `WHERE` pede — chamado de **full table scan**, equivalente conceitual à busca linear vista em [[../Programacao-Geral/05-Algoritmos-e-Complexidade]]. Em uma tabela de 10 mil linhas isso é rápido; em uma de 50 milhões, pode levar segundos ou minutos.

Um **índice** é uma estrutura extra (internamente parecida com a árvore vista em [[../Programacao-Geral/04-Estruturas-de-Dados]]) que o MySQL mantém para localizar linhas rapidamente por uma coluna específica, sem precisar examinar a tabela inteira — o mesmo salto de performance da busca binária sobre a busca linear, discutido em [[../Programacao-Geral/05-Algoritmos-e-Complexidade]].

```sql
CREATE INDEX idx_clientes_email ON clientes(email);

CREATE INDEX idx_pedidos_cliente ON pedidos(cliente_id);   -- acelera JOINs e filtros por esta coluna
```

**Chaves primárias e colunas `UNIQUE` já ganham índice automaticamente** — você só precisa criar índices manualmente para colunas usadas com frequência em `WHERE`, `JOIN` ou `ORDER BY` que não sejam a chave primária.

## O trade-off dos índices

Índices aceleram leitura (`SELECT`), mas **desaceleram escrita** (`INSERT`/`UPDATE`/`DELETE`), porque o MySQL precisa atualizar o índice a cada mudança nos dados, além dos dados em si. Por isso, criar índice em **toda** coluna não é a estratégia certa — reserve para colunas realmente consultadas com frequência.

## Vendo se uma consulta está usando índice

```sql
EXPLAIN SELECT * FROM clientes WHERE email = 'diego@exemplo.com';
```

`EXPLAIN` mostra como o MySQL **planeja** executar a consulta — incluindo se ela usa um índice ou faz um full table scan. É a ferramenta principal para diagnosticar consultas lentas em um sistema real.

## Exercício

Escreva uma subconsulta que encontre livros (tabela de [[03-Criando-Bancos-e-Tabelas]]) que **nunca** foram emprestados, usando `NOT IN` com uma subconsulta em vez do `LEFT JOIN` do exercício de [[06-Joins]] — compare as duas abordagens para o mesmo resultado.

## Perguntas de revisão

O que é uma subconsulta? :: Um SELECT dentro de outra consulta, usado quando o filtro depende de um resultado calculado antes.

O que faz EXISTS? :: Verifica se a subconsulta encontra alguma linha, sem se importar com o valor.

O que é full table scan? :: Examinar a tabela linha por linha para achar o que o WHERE pede, por falta de índice.

Qual o custo de criar índices? :: Aceleram leituras mas deixam INSERT, UPDATE e DELETE mais lentos, porque o índice precisa ser atualizado.

Quais colunas já têm índice automático? :: Chaves primárias e colunas UNIQUE.

Como saber se uma consulta usa índice? :: Com EXPLAIN antes do SELECT.

---
Veja o exemplo em `MySQL/exemplos/08_subconsultas_indices.sql`. Próxima nota: [[09-Transacoes-e-Usuarios]]
