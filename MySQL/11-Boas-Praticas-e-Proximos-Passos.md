---
tags: [mysql, boas-praticas, flashcards]
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
mysqldump -u root -p biblioteca --result-file=backup_biblioteca.sql
```

Gera um arquivo `.sql` com todos os comandos necessários para **recriar** as tabelas do banco, com os dados — a defesa real contra o cenário de "rodei um `DELETE` sem `WHERE` sem querer" (mencionado em [[04-CRUD-Insert-Select-Update-Delete]]). O `--result-file` (forma curta: `-r`) faz o próprio `mysqldump` gravar o arquivo, então o resultado é o mesmo no PowerShell, no Prompt de Comando (cmd) e no bash. A documentação do MySQL recomenda essa opção no Windows.

Muitos tutoriais usam `mysqldump -u root -p biblioteca > backup_biblioteca.sql`. No bash e no PowerShell 7.5, isso gera o mesmo arquivo. No Windows PowerShell 5.1 (`powershell`), o `>` grava o arquivo em UTF-16, e o `mysql` recusa esse arquivo na restauração (`ASCII '\0' appeared in the statement`).

Restaurar:

```bash
mysql -u root -p biblioteca -e "source backup_biblioteca.sql"
```

O banco precisa existir: o arquivo recria as tabelas, não o banco. Se você apagou o banco inteiro, crie-o de novo antes, com `mysql -u root -p -e "CREATE DATABASE biblioteca"`. A forma `mysql -u root -p biblioteca < backup_biblioteca.sql` não funciona no PowerShell, pelo motivo visto em [[02-Instalando-e-Configurando]].

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
- **Compare com SQLite**: veja [[../SQLite/00-Indice]] e, especificamente, [[../SQLite/06-SQLite-vs-MySQL]] para entender quando cada um faz mais sentido.
- **Aprenda sobre réplicas e escalabilidade** quando o volume de dados/tráfego crescer — tópico avançado, mas bom de saber que existe.

## Perguntas de revisão

Qual a convenção de nomes de tabelas e colunas? :: Tabelas no plural em snake_case e colunas em snake_case; chave estrangeira como cliente_id.

Como fazer backup de um banco MySQL? :: Com mysqldump -u root -p banco --result-file=backup.sql, restaurando com mysql -u root -p banco -e "source backup.sql".

Por que usar --result-file em vez de > no mysqldump? :: Porque no Windows PowerShell 5.1 o > grava o arquivo em UTF-16, que o mysql recusa ao restaurar; com --result-file, o próprio mysqldump grava o arquivo.

O que fazer antes de restaurar o backup de um banco apagado? :: Criar o banco de novo com CREATE DATABASE, porque o arquivo do mysqldump recria só as tabelas.

O que é uma migration? :: Um arquivo que descreve uma mudança incremental na estrutura do banco, versionado junto com o código.

Por que evitar SELECT * em código de produção? :: Traz colunas desnecessárias e muda silenciosamente quando alguém adiciona uma coluna.

Onde guardar a senha do banco? :: Em variáveis de ambiente, nunca no código-fonte.

O que é o slow query log? :: Um registro automático das consultas que demoram mais que um limite, primeiro lugar a olhar em lentidão.

---
Fim da trilha de MySQL. Volte ao [[00-Indice|índice deste curso]], ao [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados|resumo geral de SQL]] ou ao [[../SQLite/00-Indice|curso de SQLite]] a qualquer momento.
