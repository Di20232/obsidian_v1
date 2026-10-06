---
tags: [programacao, sql, banco-de-dados, flashcards]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# SQL e Bancos de Dados

> Esta nota é um resumo panorâmico. Para trilhas completas, do zero, com exercícios e exemplos para rodar — igual ao [[../Python/00-Indice|curso de Python]] — veja [[../MySQL/00-Indice|Curso de MySQL do Zero]] (banco com servidor; o índice avisa que os exemplos não foram testados num MySQL) e [[../SQLite/00-Indice|Curso de SQLite do Zero]] (banco sem servidor; exemplos testados).

## O problema que isso resolve

Arquivos de texto (vistos em [[../Python/14-Arquivos]]) funcionam para guardar dados simples, mas não escalam: são lentos para buscar em milhões de registros, não protegem bem contra dados corrompidos por acesso simultâneo, e não têm um jeito padronizado de relacionar dados entre si (um cliente que fez vários pedidos, por exemplo). Um **banco de dados** é um sistema especializado, otimizado especificamente para guardar, buscar, relacionar e proteger grandes volumes de dados de forma confiável.

## Bancos relacionais: a ideia central

Um banco de dados **relacional** organiza dados em **tabelas** — muito parecido com uma planilha: linhas (registros) e colunas (campos/atributos). Exemplos de sistemas relacionais: PostgreSQL, MySQL, SQLite, SQL Server.

```
Tabela: usuarios
| id | nome    | idade | cidade      |
|----|---------|-------|-------------|
| 1  | Diego   | 25    | São Paulo   |
| 2  | Ana     | 30    | Rio de Janeiro |
```

Cada linha tem um identificador único (`id`, chamado de **chave primária**), usado para referenciar aquele registro especificamente de outros lugares do banco.

## SQL: a linguagem para conversar com o banco

**SQL** (Structured Query Language) não é uma linguagem de propósito geral como Python — ela é **declarativa**: você descreve **o que** quer, e o banco decide **como** buscar da forma mais eficiente (diferente de escrever um `for` manualmente percorrendo dados, como em [[../Python/08-Lacos-de-Repeticao]]).

### Criando uma tabela

```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    cidade TEXT
);
```

### Inserindo dados

```sql
INSERT INTO usuarios (nome, idade, cidade) VALUES ('Diego', 25, 'São Paulo');
```

### Consultando dados (`SELECT`)

```sql
SELECT * FROM usuarios;                          -- todas as colunas, todas as linhas
SELECT nome, idade FROM usuarios;                  -- só essas colunas
SELECT * FROM usuarios WHERE idade >= 18;          -- filtro, equivalente a um if em Python
SELECT * FROM usuarios ORDER BY idade DESC;         -- ordena (decrescente)
SELECT * FROM usuarios LIMIT 10;                    -- só os 10 primeiros resultados
```

`WHERE` é o filtro — a mesma ideia lógica de uma condição no `if` visto em [[../Python/07-Condicionais]], só que aplicada a um conjunto de dados inteiro de uma vez.

### Atualizando e removendo

```sql
UPDATE usuarios SET idade = 26 WHERE nome = 'Diego';
DELETE FROM usuarios WHERE id = 2;
```

**Cuidado real**: `UPDATE`/`DELETE` sem `WHERE` afeta **todas** as linhas da tabela — um dos erros mais caros e comuns na carreira de qualquer pessoa que trabalha com bancos de dados.

## Relacionando tabelas: `JOIN`

O poder real de bancos relacionais aparece quando dados de tabelas diferentes se relacionam:

```
Tabela: pedidos
| id | usuario_id | produto     |
|----|------------|-------------|
| 1  | 1          | Notebook    |
| 2  | 1          | Mouse       |
```

`usuario_id` é uma **chave estrangeira**: aponta para o `id` de um registro em `usuarios`. Para buscar "o nome do usuário de cada pedido", você **junta** as duas tabelas:

```sql
SELECT usuarios.nome, pedidos.produto
FROM pedidos
JOIN usuarios ON pedidos.usuario_id = usuarios.id;
```

Isso evita duplicar o nome e a cidade do usuário em cada linha de pedido — um princípio chamado **normalização**: cada dado vive em um único lugar, e é referenciado, não copiado.

## Usando SQL a partir do Python

```python
import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios WHERE idade >= ?", (18,))
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

conexao.close()
```

`sqlite3` é um módulo da biblioteca padrão do Python (mesmo conceito de módulo visto em [[../Python/12-Modulos-e-Pacotes]]) para um banco de dados leve, guardado em um único arquivo — ótimo para aprender e para projetos pequenos, sem precisar instalar um servidor de banco separado.

**Nota de segurança**: o `?` no lugar do valor (em vez de colar o valor diretamente na string do SQL) evita um tipo de ataque chamado **SQL injection** — sempre passe valores como parâmetros, nunca concatenando strings diretamente em uma query.

## Bancos não-relacionais (NoSQL), rapidamente

Nem todo dado se encaixa bem em tabelas rígidas. Bancos **NoSQL** (MongoDB, Redis, entre outros) guardam dados em formatos mais flexíveis — documentos parecidos com dicionários JSON (ver [[10-Como-a-Web-Funciona]]), pares chave-valor, ou grafos. São escolhidos quando os dados são muito variáveis em formato, ou quando a prioridade é velocidade extrema em vez de relações complexas.

## Exercício

Usando `sqlite3` em Python, crie uma tabela `tarefas` com colunas `id`, `descricao` e `concluida`. Insira 3 tarefas, depois escreva uma consulta que retorne só as que ainda não foram concluídas.

## Perguntas de revisão

Como um banco relacional organiza os dados? :: Em tabelas com linhas (registros) e colunas (campos).

O que significa SQL ser declarativa? :: Descreve-se o que se quer e o banco decide como buscar da forma mais eficiente.

O que é normalização? :: Cada dado vive num único lugar e é referenciado por chave, em vez de copiado.

Como evitar SQL injection ao consultar pelo Python? :: Passando os valores como parâmetros com ?, nunca concatenando na string.

O que são bancos NoSQL? :: Bancos com formatos flexíveis, como documentos, chave-valor ou grafos, como MongoDB e Redis.

---
Próxima nota: [[10-Como-a-Web-Funciona]]
