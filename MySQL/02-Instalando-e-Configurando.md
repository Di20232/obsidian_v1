---
tags: [mysql, setup, flashcards]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# Instalando e Configurando

## O que você precisa

1. O **servidor MySQL** instalado e rodando.
2. Um **cliente** para enviar comandos a ele — pode ser a linha de comando, ou uma interface gráfica.

## Instalando no Windows

1. Baixe o **MySQL Installer** em `dev.mysql.com/downloads/installer`.
2. Escolha a opção "Server only" (ou o pacote completo, se quiser o Workbench junto — interface gráfica oficial).
3. Durante a instalação, você vai definir uma **senha para o usuário `root`** (o usuário administrador padrão) — guarde essa senha.
4. O instalador já configura o MySQL para iniciar como um serviço do Windows automaticamente.

**Alternativa mais simples**: se você já tem (ou vai instalar) o **XAMPP** ou **Laragon** mencionados em [[../PHP/02-Preparando-o-Ambiente]], o MySQL (ou MariaDB, compatível) já vem incluído e pré-configurado, sem precisar instalar separadamente.

## Conectando pela linha de comando

```bash
mysql -u root -p
```

`-u root` indica o usuário; `-p` faz o cliente pedir a senha antes de conectar. Depois de conectado, seu terminal mostra um prompt `mysql>`, esperando comandos SQL.

```sql
SHOW DATABASES;         -- lista os bancos existentes
exit                     -- sai do cliente
```

## Interfaces gráficas (opcionais, mas úteis)

- **MySQL Workbench**: ferramenta oficial, mostra tabelas, permite montar consultas visualmente.
- **DBeaver**: gratuita, funciona com MySQL e vários outros bancos (inclusive SQLite, [[../SQLite/00-Indice]]) — útil se você vai alternar entre os dois.

Nenhuma delas é obrigatória — todo comando desta trilha funciona igual pela linha de comando, que é o que os exemplos assumem por padrão.

## Criando seu primeiro banco

```sql
CREATE DATABASE loja;
USE loja;
```

`CREATE DATABASE` cria o "container" mencionado em [[01-O-que-e-MySQL]]; `USE` diz "a partir de agora, todo comando seguinte se refere a este banco" — evita precisar prefixar cada tabela com o nome do banco.

## Rodando um arquivo `.sql` inteiro de uma vez

Em vez de digitar comando por comando, é comum guardar vários comandos SQL em um arquivo e rodar tudo de uma vez. Peça ao próprio cliente que leia o arquivo, com o comando `source`. Assim o comando é o mesmo no PowerShell, no Prompt de Comando (cmd) e no bash:

```bash
mysql -u root -p loja -e "source script.sql"
```

Isso executa cada comando do arquivo `script.sql`, em ordem, no banco `loja`. O `-e` manda o cliente rodar um comando e sair. Se você já está conectado, no prompt `mysql>`, o equivalente é `SOURCE script.sql;`.

Muitos tutoriais usam `mysql -u root -p loja < script.sql`. Essa forma só funciona no bash e no cmd: no PowerShell, o `<` é um operador reservado, e o comando para com `ParserError` antes de chamar o `mysql`. Outra forma comum, `Get-Content script.sql | mysql -u root -p loja`, roda no PowerShell 7, mas estraga os acentos no Windows PowerShell 5.1 (`powershell`): lá, o texto que vai pelo pipe para um programa é convertido com `$OutputEncoding`, que por padrão é ASCII, e o `ã` vira `?`. Prefira o `source`.

Os exemplos desta trilha (`MySQL/exemplos/`) não usam o banco `loja`: o `03_criando_tabelas.sql` cria o banco `biblioteca` (`CREATE DATABASE IF NOT EXISTS biblioteca;` e `USE biblioteca;`), e os seguintes começam com `USE biblioteca;`. Por isso, rode-os **sem** nome de banco, de dentro da pasta `MySQL/exemplos/`, em ordem, a partir do 03 — os seguintes dependem do que os anteriores criaram:

```bash
mysql -u root -p --default-character-set=utf8mb4 -e "source 03_criando_tabelas.sql"
```

Passar `loja` nesse comando, sem ter criado esse banco antes, faz o cliente recusar a conexão (`Unknown database 'loja'`).

Depois, troque o nome do arquivo (`04_crud.sql`, `05_where_order_limit.sql` e assim por diante, até o 09). Para digitar a senha uma vez só, conecte com `mysql -u root -p --default-character-set=utf8mb4` e rode, um depois do outro, `SOURCE 03_criando_tabelas.sql;`, `SOURCE 04_crud.sql;` etc.

O `--default-character-set=utf8mb4` cuida dos acentos. Os scripts estão em UTF-8 (`O Cortiço`, `Grande Sertão`). Sem essa opção, o cliente lê o arquivo na codificação do sistema (no Windows, a página de código configurada), e os acentos podem ser gravados trocados: com o cliente em `latin1`, `Sertão` fica gravado como `SertÃ£o`.

**Arquivo em outra pasta.** O `source` usa como nome do arquivo tudo o que vem depois dele, espaços incluídos, e não tira aspas: `source "meu script.sql"` falha com `Failed to open file`. O mais simples é entrar na pasta com `cd` (aí sim com aspas, se o caminho tiver espaço) e passar só o nome do arquivo. Outra saída é o caminho relativo à pasta atual, escrito com `/`, que o Windows aceita. Da raiz do cofre:

```bash
mysql -u root -p --default-character-set=utf8mb4 -e "source MySQL/exemplos/03_criando_tabelas.sql"
```

Para recomeçar do zero, rode o 03 de novo: ele apaga e recria `livros` e `emprestimos`. A tabela `contas`, criada pelo 09, continua lá; antes de rodar o 09 outra vez, apague-a com `DROP TABLE contas;`, porque ele insere as contas com ids fixos (1 e 2) e falharia por chave duplicada.

## Erros comuns nesta etapa

- Esquecer o `USE nome_do_banco;` e receber `No database selected` ao tentar criar uma tabela.
- Confundir a senha do `root` do MySQL com a senha do Windows — são coisas completamente separadas.
- Servidor não iniciado (se instalado manualmente, sem XAMPP/Laragon) — confira nos Serviços do Windows se "MySQL" está rodando.
- Rodar `mysql ... < script.sql` no PowerShell e receber `ParserError` — use `mysql ... -e "source script.sql"`.

## Exercício

Instale o MySQL, conecte com `mysql -u root -p`, rode `SHOW DATABASES;` para ver os bancos padrão que já vêm instalados, crie um banco chamado `estudos`, e confirme com `SHOW DATABASES;` novamente que ele aparece na lista.

## Perguntas de revisão

Como conectar ao MySQL pela linha de comando? :: Com mysql -u root -p, que pede a senha antes de conectar.

Para que serve o comando USE? :: Define o banco usado pelos comandos seguintes, evitando o erro No database selected.

Como rodar um arquivo .sql inteiro no MySQL, em qualquer terminal? :: Com mysql -u root -p nome_do_banco -e "source script.sql" ou, já conectado, com SOURCE script.sql;

Por que mysql -u root -p loja < script.sql não funciona no PowerShell? :: Porque no PowerShell o < é um operador reservado; o comando para com ParserError antes de chamar o mysql.

Para que serve --default-character-set=utf8mb4 ao rodar os scripts? :: Faz o cliente ler o arquivo como UTF-8, para os acentos serem gravados certos.

Pode pôr aspas no caminho depois de source? :: Não; o cliente usa tudo depois de source como nome do arquivo, aspas incluídas, e falha com Failed to open file.

Por que os exemplos desta trilha rodam sem nome de banco no comando mysql? :: Porque o 03 cria o banco biblioteca e cada script já tem USE biblioteca.

A senha do root do MySQL é a mesma do Windows? :: Não; são completamente separadas.

Quais interfaces gráficas servem para o MySQL? :: MySQL Workbench, a oficial, e DBeaver, que também funciona com SQLite.

---
Próxima nota: [[03-Criando-Bancos-e-Tabelas]]
