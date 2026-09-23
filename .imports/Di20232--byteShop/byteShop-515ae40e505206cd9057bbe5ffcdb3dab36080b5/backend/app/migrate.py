"""Migração leve para SQLite: adiciona colunas novas sem apagar dados existentes.

Rodar com:  python -m app.migrate
"""

from sqlalchemy import text

from app.database import engine


def run():
    with engine.begin() as conn:
        cols = [row[1] for row in conn.execute(text("PRAGMA table_info(users)")).fetchall()]
        if "is_admin" not in cols:
            conn.execute(text("ALTER TABLE users ADD COLUMN is_admin BOOLEAN DEFAULT 0"))
            print("Coluna 'is_admin' adicionada em 'users'.")
        else:
            print("Coluna 'is_admin' já existe.")


if __name__ == "__main__":
    run()
