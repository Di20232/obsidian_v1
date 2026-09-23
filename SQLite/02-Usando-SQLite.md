---
tags: [sqlite, setup, flashcards]
cssclasses: [cerebro-nota, cerebro-sqlite]
---

# Usando SQLite

## A forma mais simples: através do Python

Como mencionado em [[01-O-que-e-SQLite]] e em [[../Python/09-Listas-Tuplas-Dicionarios]], Python já vem com suporte a SQLite embutido — **nada para instalar**. Isso é usado nesta trilha inteira para testar os exemplos de verdade:

```bash
python -c "import sqlite3; print(sqlite3.sqlite_version)"
```

Se isso imprimir um número de versão, você já pode seguir todos os exercícios desta trilha sem instalar mais nada.

## Instalando o cliente de linha de comando `sqlite3` (opcional)

Para digitar comandos SQL diretamente, sem passar por Python, existe uma ferramenta de linha de comando própria:

1. Baixe em `sqlite.org/download.html` (seção "Precompiled Binaries for Windows", pacote `sqlite-tools`).
2. Extraia e adicione a pasta ao PATH (mesmo processo de [[../Python/02-Instalando-Python]]).
3. Confirme: `sqlite3 --version`.

```bash
sqlite3 banco.db
```

Isso abre (ou cria, se não existir) o arquivo `banco.db` e entra em um prompt `sqlite>`, esperando comandos.

```sql
.tables              -- lista as tabelas do banco (comando especial do cliente, começa com ponto)
.schema livros         -- mostra a estrutura de uma tabela
.quit                  -- sai
```

Comandos que começam com `.` (ponto) são **específicos do cliente de linha de comando do SQLite**, não são SQL padrão — não funcionam dentro de código Python/PHP, só nesse terminal interativo.

## Rodando um script `.sql` inteiro

```bash
sqlite3 banco.db < script.sql
```

Mesmo padrão de [[../MySQL/02-Instalando-e-Configurando]] — mas repare que aqui **não há usuário nem senha**: quem tem acesso ao arquivo `banco.db` (e ao comando `sqlite3`) já tem acesso completo ao banco.

## Ferramentas gráficas (opcionais)

- **DB Browser for SQLite** (`sqlitebrowser.org`): interface gráfica dedicada, gratuita, ótima para visualizar e editar dados sem escrever SQL toda hora.
- **DBeaver**, já mencionado em [[../MySQL/02-Instalando-e-Configurando]] — funciona com SQLite também, útil se você alterna entre os dois bancos.

## Usando SQLite direto do Python (o caminho usado nesta trilha)

```python
import sqlite3

conexao = sqlite3.connect("banco.db")   # cria o arquivo se não existir
cursor = conexao.cursor()

cursor.execute("SELECT sqlite_version()")
print(cursor.fetchone())

conexao.close()
```

Esse é o padrão que você já viu em [[../Python/09-Listas-Tuplas-Dicionarios]] e [[../PHP/14-PHP-com-Banco-de-Dados]] (via PDO) — a partir daqui, os exemplos desta trilha alternam entre arquivos `.sql` (para rodar com o cliente `sqlite3`) e scripts Python (para rodar sem instalar nada a mais).

## Exercício

Rode `python -c "import sqlite3; print(sqlite3.sqlite_version)"` para confirmar que está tudo pronto. Se quiser, instale também o cliente `sqlite3` de linha de comando e crie um banco `teste.db` vazio, confirmando com `.tables` que ele não tem nenhuma tabela ainda.

## Perguntas de revisão

Como usar SQLite em Python sem instalar nada? :: Com o módulo sqlite3, que já vem embutido no Python.

Para que servem comandos como .tables e .schema? :: São comandos do cliente de linha de comando sqlite3, não SQL; funcionam só nesse terminal.

Como abrir ou criar um banco pelo cliente sqlite3? :: Com sqlite3 banco.db, que cria o arquivo se não existir.

Qual ferramenta gráfica é dedicada ao SQLite? :: O DB Browser for SQLite.

---
Próxima nota: [[03-Tipos-Dinamicos-e-Tabelas]]
