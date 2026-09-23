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
