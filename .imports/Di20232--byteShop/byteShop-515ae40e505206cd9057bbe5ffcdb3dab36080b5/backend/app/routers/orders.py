from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update
from sqlalchemy.orm import Session, joinedload

from app import models, schemas
from app.auth import get_current_user
from app.database import get_db

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=schemas.OrderOut, status_code=201)
def create_order(
    payload: schemas.OrderCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    order_items: list[models.OrderItem] = []
    total = Decimal(0)

    for item in payload.items:
        product = db.get(models.Product, item.product_id)
        if not product:
            raise HTTPException(status_code=404, detail=f"Produto {item.product_id} não encontrado")

        # UPDATE condicional atômico: a checagem "estoque suficiente?" e o
        # decremento acontecem numa única instrução no banco, então dois
        # pedidos simultâneos pela última unidade não conseguem os dois passar
        # (evita estoque negativo por condição de corrida).
        result = db.execute(
            update(models.Product)
            .where(models.Product.id == product.id, models.Product.stock >= item.quantity)
            .values(stock=models.Product.stock - item.quantity)
        )
        if result.rowcount == 0:
            db.rollback()
            raise HTTPException(
                status_code=400,
                detail=f"Estoque insuficiente para '{product.name}' (disponível: {product.stock})",
            )

        total += product.price * item.quantity
        order_items.append(
            models.OrderItem(
                product_id=product.id,
                product_name=product.name,
                quantity=item.quantity,
                unit_price=product.price,
            )
        )

    order = models.Order(
        user_id=current_user.id,
        status="pago",
        total=total,
        shipping_address=payload.shipping_address,
        items=order_items,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.get("", response_model=list[schemas.OrderOut])
def list_my_orders(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    stmt = (
        select(models.Order)
        .options(joinedload(models.Order.items))
        .where(models.Order.user_id == current_user.id)
        .order_by(models.Order.created_at.desc())
    )
    return db.scalars(stmt).unique().all()


@router.get("/{order_id}", response_model=schemas.OrderOut)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    order = db.scalar(
        select(models.Order)
        .options(joinedload(models.Order.items))
        .where(models.Order.id == order_id, models.Order.user_id == current_user.id)
    )
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return order
