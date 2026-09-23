---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/routers/products.py
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# backend/app/routers/products.py

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/routers/products.py). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
import math

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, joinedload

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=schemas.ProductListOut)
def list_products(
    db: Session = Depends(get_db),
    category: str | None = Query(None, description="slug da categoria"),
    brand: str | None = None,
    q: str | None = Query(None, description="busca por nome"),
    min_price: float | None = None,
    max_price: float | None = None,
    sort: str = Query("relevance", pattern="^(relevance|price_asc|price_desc|newest)$"),
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=60),
):
    stmt = select(models.Product).options(joinedload(models.Product.category))

    if category:
        stmt = stmt.join(models.Category).where(models.Category.slug == category)
    if brand:
        stmt = stmt.where(models.Product.brand.ilike(brand))
    if q:
        like = f"%{q}%"
        stmt = stmt.where(or_(models.Product.name.ilike(like), models.Product.description.ilike(like)))
    if min_price is not None:
        stmt = stmt.where(models.Product.price >= min_price)
    if max_price is not None:
        stmt = stmt.where(models.Product.price <= max_price)

    if sort == "price_asc":
        stmt = stmt.order_by(models.Product.price.asc())
    elif sort == "price_desc":
        stmt = stmt.order_by(models.Product.price.desc())
    elif sort == "newest":
        stmt = stmt.order_by(models.Product.created_at.desc())
    else:
        stmt = stmt.order_by(models.Product.id.asc())

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(stmt.offset((page - 1) * page_size).limit(page_size)).all()

    return schemas.ProductListOut(
        items=items,
        total=total or 0,
        page=page,
        page_size=page_size,
        pages=max(1, math.ceil((total or 0) / page_size)),
    )


@router.get("/{slug}", response_model=schemas.ProductOut)
def get_product(slug: str, db: Session = Depends(get_db)):
    product = db.scalar(
        select(models.Product)
        .options(joinedload(models.Product.category))
        .where(models.Product.slug == slug)
    )
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product

```
