import sqlite3
import os

CAMINHO_DB = os.path.join(os.path.dirname(__file__), "tarefas.db")

# Primeira "execução": cria e grava
conexao1 = sqlite3.connect(CAMINHO_DB)
conexao1.row_factory = sqlite3.Row
cursor1 = conexao1.cursor()
cursor1.execute("DROP TABLE IF EXISTS tarefas")
cursor1.execute("CREATE TABLE tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT)")
cursor1.executemany(
    "INSERT INTO tarefas (descricao) VALUES (?)",
    [("Estudar SQLite",), ("Revisar PHP",), ("Praticar MySQL",)],
)
conexao1.commit()  # obrigatório para persistir de verdade
conexao1.close()

# Segunda "execução": abre de novo, em uma conexão nova, e confirma que os dados persistiram
conexao2 = sqlite3.connect(CAMINHO_DB)
conexao2.row_factory = sqlite3.Row
cursor2 = conexao2.cursor()
cursor2.execute("SELECT * FROM tarefas")
for linha in cursor2.fetchall():
    print(linha["id"], linha["descricao"])
conexao2.close()
