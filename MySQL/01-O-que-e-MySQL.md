---
tags: [mysql, sql, conceitos]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# O que é MySQL

## Recapitulando o conceito de banco relacional

Como visto em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]], um banco de dados relacional guarda informação em **tabelas** (linhas e colunas), e você usa **SQL** (Structured Query Language) para criar, consultar, alterar e apagar esses dados. SQL, em si, é um **padrão de linguagem** — MySQL é um **sistema de banco de dados específico** (um programa de verdade, chamado SGBD: Sistema Gerenciador de Banco de Dados) que implementa esse padrão, com algumas particularidades próprias.

## MySQL é um servidor

Assim como PHP roda como um processo esperando requisições HTTP ([[../PHP/02-Preparando-o-Ambiente]]), o **MySQL roda como um servidor próprio**, esperando conexões na porta `3306` por padrão. Qualquer programa (PHP, Python, uma ferramenta de linha de comando) se conecta a esse servidor para enviar comandos SQL e receber resultados — o mesmo modelo cliente-servidor de [[../Programacao-Geral/10-Como-a-Web-Funciona]], só que aqui o "protocolo" é o protocolo do MySQL, não HTTP.

```
Sua aplicação (PHP/Python)  --- conexão MySQL --->  Servidor MySQL  --->  Arquivos em disco
```

## Onde o MySQL se encaixa em relação a outros bancos

- **MySQL**: relacional, servidor próprio, gratuito e open source (com uma versão paga da Oracle também), o mais comum em hospedagens compartilhadas e no ecossistema PHP/WordPress.
- **PostgreSQL**: relacional, servidor próprio, geralmente considerado mais rico em recursos avançados — comum em projetos que lidam com dados mais complexos.
- **SQLite** ([[../SQLite/00-Indice]]): relacional, mas **sem servidor** — o banco inteiro é um único arquivo, sem processo próprio rodando. Ótimo para aprender, apps pequenos, ou dados locais de um único programa.
- **MariaDB**: um "fork" (uma ramificação independente) do MySQL, criado pelos fundadores originais depois que a Oracle comprou o MySQL — compatível na imensa maioria dos casos, comandos SQL desta trilha funcionam nos dois.

## Por que aprender MySQL especificamente, e não só "SQL genérico"

O padrão SQL cobre o essencial (`SELECT`, `WHERE`, `JOIN`), mas cada banco tem funções e comportamentos próprios em detalhes — tipos de dado disponíveis, como definir auto-incremento, funções de data. Esta trilha ensina SQL usando a sintaxe **real** do MySQL, para que você consiga rodar exatamente o que aprender em um servidor de verdade.

## Vocabulário essencial

- **Schema / banco de dados**: o "container" que agrupa tabelas relacionadas (ex.: o banco `loja`, contendo tabelas `produtos`, `pedidos`, `clientes`).
- **Tabela**: a estrutura de linhas e colunas em si.
- **Linha (row) / registro**: uma entrada individual da tabela.
- **Coluna (column) / campo**: um atributo de cada registro.
- **Chave primária (primary key)**: a coluna (ou conjunto de colunas) que identifica **unicamente** cada linha — nunca se repete dentro da tabela.
- **Chave estrangeira (foreign key)**: uma coluna que referencia a chave primária de **outra** tabela, criando um relacionamento entre elas.

## Exercício

Sem escrever SQL ainda: pense em um sistema que você usa (uma rede social, um app de delivery) e imagine 3 tabelas que provavelmente existem por trás dele, e quais colunas cada uma teria. Pense também em como elas se relacionam (por exemplo, um "pedido" está ligado a um "cliente" e a vários "itens").

---
Próxima nota: [[02-Instalando-e-Configurando]]
