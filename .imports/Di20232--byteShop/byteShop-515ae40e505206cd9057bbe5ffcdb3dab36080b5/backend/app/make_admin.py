"""Promove um usuário existente a administrador.

Rodar com:  python -m app.make_admin email@exemplo.com
"""

import sys

from sqlalchemy import select

from app import models
from app.database import SessionLocal


def run(email: str):
    db = SessionLocal()
    try:
        user = db.scalar(select(models.User).where(models.User.email == email))
        if not user:
            print(f"Usuário '{email}' não encontrado.")
            return
        user.is_admin = True
        db.commit()
        print(f"Usuário '{email}' agora é administrador.")
    finally:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python -m app.make_admin email@exemplo.com")
        sys.exit(1)
    run(sys.argv[1])
