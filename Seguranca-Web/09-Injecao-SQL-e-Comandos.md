---
tags: [seguranca, web, sql-injection, injecao, flashcards]
aliases: [SQL Injection, Injeção de SQL]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# Injeção de SQL e de comandos

Injeção acontece quando **texto do usuário vira parte de um comando**: uma consulta SQL, uma linha de shell, uma expressão. O interpretador não sabe onde termina o dado e começa a instrução — e executa o que o atacante escreveu.

## SQL injection

```python
# ERRADO: o texto do usuário é colado na consulta
email = request.form["email"]
db.execute(f"SELECT * FROM usuarios WHERE email = '{email}'")
```

Se o usuário digitar `' OR '1'='1`, a consulta vira:

```sql
SELECT * FROM usuarios WHERE email = '' OR '1'='1'
```

que devolve **todos** os usuários. Com outras entradas dá para ler tabelas inteiras (`UNION SELECT`), apagar dados ou, em alguns bancos, executar comandos no servidor.

### A defesa: consulta parametrizada

O comando e os dados viajam **separados**; o banco nunca interpreta o dado como SQL.

| Ferramenta | Forma segura |
|---|---|
| `sqlite3` (Python) | `db.execute("... WHERE email = ?", (email,))` |
| `psycopg` / `mysql-connector` | `cur.execute("... WHERE email = %s", (email,))` — o `%s` aqui é marcador do driver, **não** formatação de string |
| SQLAlchemy | `text("... WHERE email = :email")` com `{"email": email}` |
| `better-sqlite3` / `pg` (Node) | `db.prepare("... WHERE email = ?").get(email)` / `pool.query("... $1", [email])` |
| Prisma | métodos normais (`findMany`) ou `` $queryRaw`... ${email}` `` (template tag parametriza) |

> [!danger] Armadilhas que parecem seguras
> - `cur.execute("... = '%s'" % email)` — isso é formatação de string do Python, **não** parâmetro.
> - Prisma `$queryRawUnsafe` e `$executeRawUnsafe` com texto concatenado.
> - "Escapar aspas" à mão: sempre sobra um caso (codificação, barra invertida, número sem aspas).

### Nome de tabela e coluna: allowlist

Parâmetros só funcionam para **valores**. Nome de tabela, coluna ou direção de ordenação (`ASC`/`DESC`) não podem ser parametrizados — então vêm de uma **lista fechada**:

```python
COLUNAS_ORDEM = {"nome", "preco", "criado_em"}
coluna = request.args.get("ordem", "nome")
if coluna not in COLUNAS_ORDEM:
    abort(400)
db.execute(f"SELECT * FROM produtos ORDER BY {coluna}")   # seguro: coluna veio da lista
```

Os dois casos reais do cofre são exatamente isso: [[Cerebro/Problemas-Resolvidos/09-Nome-de-Tabela-em-F-String-no-SQL|nome de tabela em f-string]] e [[Cerebro/Problemas-Resolvidos/21-SQL-Injection-por-Token-de-URL|token de URL virando SQL]].

### ORM não é imunidade

ORMs parametrizam os métodos normais, mas quase todos têm uma porta para SQL cru (`raw`, `text`, `$queryRawUnsafe`, `.extra()`). É ali que a injeção aparece.

### Camadas extras

- **Usuário de banco com menor privilégio:** a aplicação não precisa de `DROP TABLE` nem acesso a outras bases.
- **Erros genéricos:** mensagem de erro com o SQL ajuda o atacante a montar a próxima tentativa.
- **Validação de entrada** (formato de e-mail, número inteiro, tamanho máximo) reduz a superfície — mas é camada extra, **nunca** substitui o parâmetro.

## Injeção de comandos do sistema

```python
# ERRADO: shell=True com texto do usuário
subprocess.run(f"convert {nome_arquivo} saida.png", shell=True)
# nome_arquivo = "foto.jpg; rm -rf ~"  → executa os dois comandos
```

```python
# CERTO: lista de argumentos, sem shell
subprocess.run(["convert", nome_arquivo, "saida.png"], check=True)
```

Em Node, a mesma diferença existe entre `exec` (passa por um shell) e `execFile`/`spawn` com lista de argumentos. Cuidados extras:

- Um argumento que começa com `-` pode ser lido como opção (`--output=/etc/...`). Use `--` antes dos arquivos quando o programa aceitar, ou valide o formato.
- Melhor ainda: usar uma **biblioteca** (Pillow, sharp) em vez de chamar um programa externo.

## Outras injeções do mesmo tipo

| Tipo | Como aparece | Defesa |
|---|---|---|
| **NoSQL** (MongoDB) | o JSON `{"senha": {"$ne": null}}` faz a consulta aceitar qualquer senha | validar o tipo (a senha tem de ser string) e usar esquema |
| **Template** (SSTI) | `render_template_string("Olá " + nome)` no Flask executa `{{ ... }}` digitado pelo usuário | passar o dado como variável do template, nunca montar o template com ele |
| **`eval`/`exec`** | calculadora que faz `eval(expressao)` | nunca avaliar texto do usuário; usar um parser próprio |
| **Cabeçalho/e-mail** | quebra de linha no campo "assunto" injeta cabeçalhos | recusar `\r` e `\n` nesses campos |
| **XSS** | HTML do usuário executado no navegador | → [[10-XSS-e-CSP\|XSS e CSP]] |
| **Prompt** | texto que manda a IA ignorar as instruções | → [[IA-Aplicada/09-Riscos-Seguranca-e-LGPD-na-IA\|riscos na IA]] |

## Perguntas de revisão

O que é injeção? :: Quando texto do usuário vira parte de um comando interpretado, como SQL ou shell, e o interpretador executa o que o atacante escreveu.

Como a entrada ' OR '1'='1 afeta uma consulta montada com texto? :: A condição vira sempre verdadeira e a consulta devolve todos os registros, por exemplo todos os usuários.

Qual a defesa principal contra SQL injection? :: Consulta parametrizada: o comando e os dados vão separados e o banco nunca interpreta o dado como SQL.

Por que cur.execute("... = '%s'" % email) é inseguro mesmo usando %s? :: Porque o operador % faz formatação de string do Python antes de chegar ao driver; o seguro é passar os valores como segundo argumento do execute.

Como tratar nome de tabela ou coluna vindo do usuário? :: Com lista fechada de valores permitidos (allowlist), porque parâmetros só funcionam para valores.

Usar ORM elimina o risco de SQL injection? :: Não; os métodos normais parametrizam, mas as funções de SQL cru, como $queryRawUnsafe ou text com concatenação, continuam vulneráveis.

Validação de entrada substitui a consulta parametrizada? :: Não; é uma camada extra que reduz a superfície, mas o parâmetro continua obrigatório.

Como evitar injeção de comandos com subprocess? :: Passar os argumentos como lista, sem shell=True, e de preferência usar uma biblioteca em vez de programa externo.

Qual a diferença entre exec e execFile no Node? :: O exec passa a string por um shell, que interpreta ; e |; o execFile executa o programa com a lista de argumentos, sem shell.

O que é injeção de template (SSTI)? :: Montar o template com texto do usuário, como render_template_string("Olá " + nome), fazendo o motor executar expressões digitadas por ele.

---
Anterior: [[08-Controle-de-Acesso|Controle de acesso]] · Próxima: [[10-XSS-e-CSP|XSS e CSP]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
