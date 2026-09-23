---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/make_admin.py
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# backend/app/make_admin.py

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/make_admin.py). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
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

```
