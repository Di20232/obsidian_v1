---
tags: [mysql, sql, indice]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# Curso de MySQL do Zero

Mesmo formato das outras trilhas: conceito, porquê, sintaxe correta, exercício. Esta trilha aprofunda o que já foi adiantado em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]], focando especificamente no **MySQL** — o sistema de banco de dados relacional mais usado junto com PHP ([[../PHP/14-PHP-com-Banco-de-Dados]]) e um dos mais usados na web em geral.

> **Nota sobre os exemplos**: este ambiente não tem MySQL instalado para testar ao vivo. Os arquivos `.sql` de exemplo foram escritos com cuidado extra na sintaxe — rode-os você mesmo depois de instalar (nota 02) para confirmar. Para praticar sem instalar nada agora, veja [[../SQLite/00-Indice]], que usa a mesma linguagem SQL em um banco sem servidor.

## Trilha

1. [[01-O-que-e-MySQL]] — o que é, onde se encaixa, MySQL vs. outros bancos
2. [[02-Instalando-e-Configurando]] — instalar o servidor e um cliente
3. [[03-Criando-Bancos-e-Tabelas]] — `CREATE DATABASE`, `CREATE TABLE`, tipos de dado
4. [[04-CRUD-Insert-Select-Update-Delete]] — as quatro operações fundamentais
5. [[05-Where-Order-Limit]] — filtrando, ordenando e limitando resultados
6. [[06-Joins]] — combinando dados de várias tabelas
7. [[07-Funcoes-de-Agregacao-e-Group-By]] — somar, contar, agrupar
8. [[08-Subconsultas-e-Indices]] — consultas dentro de consultas, e performance
9. [[09-Transacoes-e-Usuarios]] — garantindo consistência e controlando acesso
10. [[10-MySQL-com-PHP-e-Python]] — conectando a partir de código de verdade
11. [[11-Boas-Praticas-e-Proximos-Passos]] — como continuar depois deste curso

## Onde isto se conecta

- [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]] — a introdução geral que esta trilha aprofunda.
- [[../SQLite/00-Indice]] — outro banco relacional, mais simples, para comparar trade-offs (ver [[../SQLite/06-SQLite-vs-MySQL]]).
- [[../PHP/14-PHP-com-Banco-de-Dados]] e [[../Python/09-Listas-Tuplas-Dicionarios]] — como consumir esses dados a partir de código de aplicação.
