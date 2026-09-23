---
tags: [sqlite, boas-praticas, flashcards]
cssclasses: [cerebro-nota, cerebro-sqlite]
---

# Boas Práticas e Próximos Passos

## Você terminou o essencial de SQLite

Com esta trilha, você fecha o panorama de bancos de dados relacionais desta sequência: o conceito geral ([[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]]), um banco com servidor completo ([[../MySQL/00-Indice]]), e um banco sem servidor. O SQL em si é praticamente o mesmo conhecimento reaproveitado nos dois — o que muda é o contexto de uso, resumido em [[06-SQLite-vs-MySQL]].

## Sempre feche a conexão (ou use context managers)

Em Python, prefira o padrão `with`, o mesmo já usado para arquivos em [[../Python/14-Arquivos]]:

```python
import sqlite3

with sqlite3.connect("banco.db") as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    print(cursor.fetchall())
# a conexão faz commit automático ao sair do bloco (mas não fecha sozinha — feche explicitamente se for o caso)
```

## Sempre ative `foreign_keys`

Já mencionado em [[03-Tipos-Dinamicos-e-Tabelas]], vale repetir por ser um detalhe fácil de esquecer e que causa bugs silenciosos: sem `PRAGMA foreign_keys = ON;`, SQLite **aceita** inserir uma chave estrangeira apontando para um registro que não existe, sem avisar nada.

## Cuidado com escrita concorrente

Se dois processos tentam escrever no mesmo arquivo SQLite ao mesmo tempo, um deles pode receber o erro `database is locked`. Isso é esperado, dado o que foi discutido em [[06-SQLite-vs-MySQL]] — SQLite não foi desenhado para alta concorrência de escrita. Se isso começar a acontecer com frequência no seu projeto, é um sinal de que talvez seja hora de migrar para MySQL/PostgreSQL.

## Vacuum: compactando o arquivo

```sql
VACUUM;
```

Depois de muitas exclusões (`DELETE`), o arquivo `.db` pode ficar maior do que precisa (o espaço não é sempre devolvido ao sistema operacional automaticamente). `VACUUM` reconstrói o arquivo, compactando-o — equivalente, em espírito, a uma "desfragmentação" do banco.

## Testando seu código que usa banco

Retomando [[../Programacao-Geral/12-Debugging-e-Testes]]: SQLite com `:memory:` (visto em [[05-SQLite-com-Python-e-PHP]]) é a ferramenta ideal para testes automatizados que envolvem banco de dados — cada teste pode criar um banco limpo do zero, extremamente rápido, sem sujar um banco real nem depender de um servidor MySQL rodando durante os testes.

```python
import sqlite3

def test_insercao_de_livro():
    conexao = sqlite3.connect(":memory:")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE livros (id INTEGER PRIMARY KEY, titulo TEXT)")
    cursor.execute("INSERT INTO livros (titulo) VALUES (?)", ("Dom Casmurro",))
    cursor.execute("SELECT COUNT(*) FROM livros")
    assert cursor.fetchone()[0] == 1
    conexao.close()

test_insercao_de_livro()
print("Teste passou!")
```

## Para onde ir a partir daqui

- **Pratique com um projeto pequeno completo**: um app de linha de comando (Python, [[../Python/00-Indice]]) ou um site simples (PHP, [[../PHP/00-Indice]]) que guarde dados em SQLite.
- Volte para [[06-SQLite-vs-MySQL]] sempre que precisar decidir qual banco usar em um projeto novo.
- Se o projeto crescer e precisar de mais concorrência/usuários, migre para [[../MySQL/00-Indice]] — o SQL que você aprendeu aqui transfere quase direto.

## Perguntas de revisão

O que o erro database is locked indica no SQLite? :: Escrita concorrente no mesmo arquivo; se for frequente, é sinal para migrar para um banco com servidor.

Para que serve o VACUUM? :: Reconstrói e compacta o arquivo do banco depois de muitas exclusões.

O with sqlite3.connect() fecha a conexão sozinho? :: Não; faz commit ao sair do bloco, mas a conexão precisa ser fechada explicitamente.

Por que SQLite é ideal para testes automatizados? :: Com :memory:, cada teste cria um banco limpo, rápido e sem depender de servidor.

---
Fim da trilha de SQLite. Volte ao [[00-Indice|índice deste curso]], ao [[../MySQL/00-Indice|curso de MySQL]] ou ao [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados|resumo geral de SQL]] a qualquer momento.
