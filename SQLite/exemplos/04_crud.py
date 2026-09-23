import sqlite3

conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT,
        ano_publicacao INTEGER
    )
""")
cursor.execute("""
    CREATE TABLE emprestimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER,
        nome_leitor TEXT NOT NULL,
        FOREIGN KEY (livro_id) REFERENCES livros(id)
    )
""")

livros = [
    ("Dom Casmurro", "Machado de Assis", 1899),
    ("Grande Sertão: Veredas", "Guimarães Rosa", 1956),
    ("Capitães da Areia", "Jorge Amado", 1937),
]
cursor.executemany("INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)", livros)

cursor.execute("SELECT * FROM livros WHERE ano_publicacao > 1900 ORDER BY ano_publicacao")
print("Livros após 1900:", cursor.fetchall())

cursor.execute("UPDATE livros SET ano_publicacao = 1900 WHERE titulo = ?", ("Dom Casmurro",))
cursor.execute("INSERT INTO emprestimos (livro_id, nome_leitor) VALUES (1, 'Carla')")

cursor.execute("""
    SELECT livros.titulo, emprestimos.nome_leitor
    FROM emprestimos
    JOIN livros ON emprestimos.livro_id = livros.id
""")
print("Empréstimos:", cursor.fetchall())

cursor.execute("SELECT date('now')")
print("Data atual (SQLite):", cursor.fetchone())

conexao.close()
