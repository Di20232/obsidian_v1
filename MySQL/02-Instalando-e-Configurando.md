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

Em vez de digitar comando por comando, é comum guardar vários comandos SQL em um arquivo e rodar tudo de uma vez:

```bash
mysql -u root -p loja < script.sql
```

Isso executa cada comando do arquivo `script.sql`, em ordem, no banco `loja` — é assim que os exemplos desta trilha devem ser testados.

## Erros comuns nesta etapa

- Esquecer o `USE nome_do_banco;` e receber `No database selected` ao tentar criar uma tabela.
- Confundir a senha do `root` do MySQL com a senha do Windows — são coisas completamente separadas.
- Servidor não iniciado (se instalado manualmente, sem XAMPP/Laragon) — confira nos Serviços do Windows se "MySQL" está rodando.

## Exercício

Instale o MySQL, conecte com `mysql -u root -p`, rode `SHOW DATABASES;` para ver os bancos padrão que já vêm instalados, crie um banco chamado `estudos`, e confirme com `SHOW DATABASES;` novamente que ele aparece na lista.

## Perguntas de revisão

Como conectar ao MySQL pela linha de comando? :: Com mysql -u root -p, que pede a senha antes de conectar.

Para que serve o comando USE? :: Define o banco usado pelos comandos seguintes, evitando o erro No database selected.

Como rodar um arquivo .sql inteiro no MySQL? :: Com mysql -u root -p nome_do_banco < script.sql.

A senha do root do MySQL é a mesma do Windows? :: Não; são completamente separadas.

Quais interfaces gráficas servem para o MySQL? :: MySQL Workbench, a oficial, e DBeaver, que também funciona com SQLite.

---
Próxima nota: [[03-Criando-Bancos-e-Tabelas]]
