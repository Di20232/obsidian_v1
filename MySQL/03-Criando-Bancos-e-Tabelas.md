---
tags: [mysql, sql]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# Criando Bancos e Tabelas

## `CREATE TABLE`: definindo a estrutura

```sql
CREATE DATABASE IF NOT EXISTS loja;
USE loja;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    idade INT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Desmontando cada parte:
- `id INT AUTO_INCREMENT PRIMARY KEY` — a chave primária (visto em [[01-O-que-e-MySQL]]), um número que o próprio MySQL gera e incrementa automaticamente a cada novo registro.
- `VARCHAR(100)` — texto de tamanho **variável**, até 100 caracteres — o tipo mais comum para texto curto (nomes, e-mails).
- `NOT NULL` — essa coluna **não pode** ficar vazia; tentar inserir sem valor gera erro.
- `UNIQUE` — não pode haver dois registros com o mesmo valor nessa coluna (dois clientes com o mesmo e-mail, por exemplo).
- `DEFAULT CURRENT_TIMESTAMP` — se nenhum valor for informado, usa a data/hora atual automaticamente.

## Tipos de dado mais usados no MySQL

| Tipo | Uso |
|---|---|
| `INT` | números inteiros |
| `DECIMAL(10,2)` | números com casas decimais **exatas** — sempre use para dinheiro, nunca `FLOAT` |
| `FLOAT` / `DOUBLE` | números decimais aproximados — ok para medições, não para dinheiro |
| `VARCHAR(n)` | texto curto, tamanho máximo `n` |
| `TEXT` | texto longo, sem limite prático curto |
| `DATE` | só data (`2026-08-28`) |
| `DATETIME` / `TIMESTAMP` | data e hora |
| `BOOLEAN` | verdadeiro/falso (internamente, o MySQL guarda como `TINYINT(1)`) |

**Por que `DECIMAL` para dinheiro**: `FLOAT`/`DOUBLE` guardam números de ponto flutuante de forma aproximada (o mesmo tipo `float` visto em [[../Python/04-Variaveis-e-Tipos]]), o que pode gerar erros minúsculos de arredondamento — inaceitável ao lidar com valores financeiros. `DECIMAL(10,2)` guarda exatamente o número de casas decimais especificado, sem essa imprecisão.

## Relacionando tabelas: chave estrangeira

```sql
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    produto VARCHAR(100),
    valor DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

`FOREIGN KEY (cliente_id) REFERENCES clientes(id)` diz ao MySQL: "todo valor de `cliente_id` nesta tabela precisa existir como `id` na tabela `clientes`". Isso é chamado de **integridade referencial** — o banco **recusa** inserir um pedido apontando para um cliente que não existe, prevenindo dados inconsistentes automaticamente, sem depender de checagem manual no código da aplicação.

## Alterando uma tabela já existente

```sql
ALTER TABLE clientes ADD COLUMN telefone VARCHAR(20);
ALTER TABLE clientes DROP COLUMN telefone;
ALTER TABLE clientes MODIFY COLUMN nome VARCHAR(150);
```

## Apagando

```sql
DROP TABLE pedidos;        -- apaga a tabela inteira, estrutura e dados
DROP DATABASE loja;         -- apaga o banco inteiro — extremamente destrutivo, use com cautela
```

**Atenção real**: `DROP` não pede confirmação e não tem "lixeira" — é permanente. Sempre confira em qual banco você está conectado antes de rodar `DROP`.

## Vendo a estrutura de uma tabela

```sql
DESCRIBE clientes;
SHOW TABLES;
```

## Exercício

Crie um banco `biblioteca` com duas tabelas: `livros` (id, titulo, autor, ano_publicacao) e `emprestimos` (id, livro_id como chave estrangeira, nome_leitor, data_emprestimo). Confira a estrutura com `DESCRIBE`.

---
Veja o exemplo em `MySQL/exemplos/03_criando_tabelas.sql`. Próxima nota: [[04-CRUD-Insert-Select-Update-Delete]]
