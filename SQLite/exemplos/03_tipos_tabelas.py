import sqlite3

conexao = sqlite3.connect(":memory:")  # banco temporário só na memória, ótimo para testar
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL
    )
""")

cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Caderno", 15.90))

# SQLite aceita texto numa coluna REAL (tipagem dinâmica, diferente do MySQL)
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Caneta", "trinta e cinco centavos"))

cursor.execute("SELECT id, nome, preco, typeof(preco) FROM produtos")
for linha in cursor.fetchall():
    print(linha)

conexao.close()
