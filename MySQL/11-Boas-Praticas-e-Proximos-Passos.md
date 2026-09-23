---
tags: [mysql, boas-praticas]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# Boas Práticas e Próximos Passos

## Você terminou o essencial de MySQL

Combinado com [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]], você agora sabe criar estrutura, fazer CRUD completo, combinar tabelas, agregar dados, otimizar com índices, garantir consistência com transações, e conectar tudo isso a partir de PHP e Python. Isso cobre a grande maioria do que um desenvolvedor usa no dia a dia com bancos relacionais.

## Nomenclatura consistente

- Nomes de tabela: plural, minúsculo, `snake_case` (`clientes`, `itens_pedido`) — convenção amplamente adotada, embora não seja imposta pelo MySQL.
- Nomes de coluna: `snake_case` (`data_criacao`, não `dataCriacao`).
- Chave primária: geralmente `id`; chave estrangeira: `tabela_no_singular_id` (`cliente_id`, `livro_id`) — já usado ao longo desta trilha.

## Backup: o hábito que evita desastres

```bash
mysqldump -u root -p biblioteca > backup_biblioteca.sql
```

Gera um arquivo `.sql` com todos os comandos necessários para **recriar** o banco do zero — a defesa real contra o cenário de "rodei um `DELETE` sem `WHERE` sem querer" (mencionado em [[04-CRUD-Insert-Select-Update-Delete]]). Restaurar:

```bash
mysql -u root -p biblioteca < backup_biblioteca.sql
```

Em produção, backups devem ser **automáticos e regulares**, não um hábito manual esporádico.

## Migrations: versionando a estrutura do banco

Assim como o código é versionado com Git ([[../Programacao-Geral/03-Git-e-Controle-de-Versao]]), a **estrutura** do banco (tabelas, colunas) também deveria ser. Uma **migration** é um arquivo que descreve uma mudança incremental na estrutura (`ALTER TABLE clientes ADD COLUMN telefone...`), guardado no controle de versão junto com o código, para que qualquer pessoa (ou servidor novo) consiga recriar o banco exatamente do mesmo jeito, passo a passo. Frameworks como Laravel (PHP) e Django (Python) já têm sistemas de migration embutidos.

## Nunca use `SELECT *` em código de produção

```sql
-- Evite em código real:
SELECT * FROM clientes;

-- Prefira:
SELECT id, nome, email FROM clientes;
```

`SELECT *` traz colunas que você talvez nem use, desperdiçando banda e memória, e **quebra silenciosamente** se alguém adicionar uma coluna nova depois (o código pode passar a receber um campo inesperado). Nomear as colunas explicitamente é mais verboso, mas mais seguro em código que vai durar.

## Revisitando segurança

- **Sempre** prepared statements (`?`/`%s`), nunca concatenação de string em SQL — já reforçado em [[../PHP/14-PHP-com-Banco-de-Dados]] e [[10-MySQL-com-PHP-e-Python]].
- **Usuários com permissão mínima** para cada aplicação, nunca `root` em produção (visto em [[09-Transacoes-e-Usuarios]]).
- **Senhas fortes e não versionadas** — nunca coloque a senha do banco direto no código-fonte; use variáveis de ambiente.

## Monitorando performance

```sql
SHOW PROCESSLIST;   -- mostra consultas rodando agora no servidor
EXPLAIN SELECT ...; -- já visto em [[08-Subconsultas-e-Indices]]
```

Em produção, ferramentas como o **slow query log** do MySQL registram automaticamente consultas que demoram mais que um limite configurado — o primeiro lugar a olhar quando um sistema começa a ficar lento.

## Para onde ir a partir daqui

- **Pratique com um projeto completo**: uma API PHP ([[../PHP/00-Indice]]) ou Python que faça CRUD completo sobre uma tabela MySQL.
- **Compare com SQLite**: veja [[../SQLite/00-Indice]] e, especificamente, [[../SQLite/07-SQLite-vs-MySQL]] para entender quando cada um faz mais sentido.
- **Aprenda sobre réplicas e escalabilidade** quando o volume de dados/tráfego crescer — tópico avançado, mas bom de saber que existe.

---
Fim da trilha de MySQL. Volte ao [[00-Indice|índice deste curso]], ao [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados|resumo geral de SQL]] ou ao [[../SQLite/00-Indice|curso de SQLite]] a qualquer momento.
