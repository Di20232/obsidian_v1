---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/schemas.py
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# backend/app/schemas.py

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/schemas.py). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
import json
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from app.utils import slugify


def _validate_name(value: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError("Nome não pode ser vazio ou conter apenas espaços")
    if not slugify(value):
        raise ValueError("Nome deve conter ao menos uma letra ou número")
    return value


# ---------- Category ----------
class CategoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    slug: str


class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)

    _validate_name = field_validator("name")(_validate_name)


class CategoryUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=80)

    _validate_name = field_validator("name")(_validate_name)


# ---------- Product ----------
class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    slug: str
    description: str
    brand: str
    price: Decimal
    stock: int
    image_url: str
    specs: dict
    category: CategoryOut


class ProductListOut(BaseModel):
    items: list[ProductOut]
    total: int
    page: int
    page_size: int
    pages: int


def _validate_specs(value: dict) -> dict:
    if len(value) > 50:
        raise ValueError("Especificações não podem ter mais de 50 campos")
    if len(json.dumps(value)) > 5000:
        raise ValueError("Especificações excedem o tamanho máximo permitido (5000 caracteres em JSON)")
    return value


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=200)
    description: str = Field(default="", max_length=2000)
    brand: str = Field(default="", max_length=80)
    price: Decimal = Field(gt=0, le=Decimal("99999999.99"))
    stock: int = Field(ge=0, le=1_000_000)
    image_url: str = Field(default="", max_length=500)
    specs: dict = Field(default_factory=dict)
    category_id: int

    _validate_name = field_validator("name")(_validate_name)
    _validate_specs = field_validator("specs")(_validate_specs)


class ProductUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=200)
    description: str = Field(default="", max_length=2000)
    brand: str = Field(default="", max_length=80)
    price: Decimal = Field(gt=0, le=Decimal("99999999.99"))
    stock: int = Field(ge=0, le=1_000_000)
    image_url: str = Field(default="", max_length=500)
    specs: dict = Field(default_factory=dict)
    category_id: int

    _validate_name = field_validator("name")(_validate_name)
    _validate_specs = field_validator("specs")(_validate_specs)


# ---------- Auth / User ----------
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)

    _validate_name = field_validator("name")(_validate_name)


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: EmailStr
    is_admin: bool
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut


# ---------- Orders ----------
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0, le=10_000)


class OrderCreate(BaseModel):
    items: list[OrderItemCreate] = Field(min_length=1, max_length=100)
    shipping_address: str = Field(min_length=5, max_length=500)


class OrderItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    product_name: str
    quantity: int
    unit_price: Decimal


class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: str
    total: Decimal
    shipping_address: str
    created_at: datetime
    items: list[OrderItemOut]

```
