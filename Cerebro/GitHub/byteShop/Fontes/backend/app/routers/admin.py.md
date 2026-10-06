---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/routers/admin.py
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# backend/app/routers/admin.py

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/routers/admin.py). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload

from app import models, schemas
from app.auth import get_current_admin_user
from app.database import get_db
from app.utils import unique_slug

router = APIRouter(prefix="/admin", tags=["admin"], dependencies=[Depends(get_current_admin_user)])


# ---------- Products ----------
@router.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.scalar(
        select(models.Product).options(joinedload(models.Product.category)).where(models.Product.id == product_id)
    )
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product


@router.post("/products", response_model=schemas.ProductOut, status_code=201)
def create_product(payload: schemas.ProductCreate, db: Session = Depends(get_db)):
    if not db.get(models.Category, payload.category_id):
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    product = models.Product(**payload.model_dump(), slug=unique_slug(db, models.Product, payload.name))
    db.add(product)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Já existe um produto com dados conflitantes") from None
    db.refresh(product)
    return db.scalar(
        select(models.Product).options(joinedload(models.Product.category)).where(models.Product.id == product.id)
    )


@router.put("/products/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, payload: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product = db.get(models.Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if not db.get(models.Category, payload.category_id):
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    if payload.name != product.name:
        product.slug = unique_slug(db, models.Product, payload.name, ignore_id=product.id)

    for field, value in payload.model_dump(exclude={"name"}).items():
        setattr(product, field, value)
    product.name = payload.name

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Já existe um produto com dados conflitantes") from None
    db.refresh(product)
    return db.scalar(
        select(models.Product).options(joinedload(models.Product.category)).where(models.Product.id == product.id)
    )


@router.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(models.Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if db.scalar(select(models.OrderItem).where(models.OrderItem.product_id == product_id)):
        raise HTTPException(
            status_code=400, detail="Não é possível excluir: existem pedidos associados a este produto"
        )
    db.delete(product)
    db.commit()


# ---------- Categories ----------
@router.post("/categories", response_model=schemas.CategoryOut, status_code=201)
def create_category(payload: schemas.CategoryCreate, db: Session = Depends(get_db)):
    category = models.Category(name=payload.name, slug=unique_slug(db, models.Category, payload.name))
    db.add(category)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Já existe uma categoria com esse nome") from None
    db.refresh(category)
    return category


@router.put("/categories/{category_id}", response_model=schemas.CategoryOut)
def update_category(category_id: int, payload: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    category = db.get(models.Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    if payload.name != category.name:
        category.slug = unique_slug(db, models.Category, payload.name, ignore_id=category.id)
    category.name = payload.name
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Já existe uma categoria com esse nome") from None
    db.refresh(category)
    return category


@router.delete("/categories/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.get(models.Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    if db.scalar(select(models.Product).where(models.Product.category_id == category_id)):
        raise HTTPException(status_code=400, detail="Não é possível excluir: existem produtos nessa categoria")
    db.delete(category)
    db.commit()

```
