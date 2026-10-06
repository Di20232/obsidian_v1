---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/tests/test_admin.py
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# backend/tests/test_admin.py

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/tests/test_admin.py). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
def test_non_admin_cannot_access_admin_routes(client, auth_headers):
    headers = auth_headers()
    res = client.post("/admin/categories", json={"name": "Nova"}, headers=headers)
    assert res.status_code == 403


def test_admin_routes_require_auth_at_all(client):
    res = client.get("/admin/products/1")
    assert res.status_code == 401


def test_category_crud(client, admin_headers):
    res = client.post("/admin/categories", json={"name": "Coolers"}, headers=admin_headers)
    assert res.status_code == 201
    cat = res.json()
    assert cat["slug"] == "coolers"

    res = client.put(f"/admin/categories/{cat['id']}", json={"name": "Coolers e Fans"}, headers=admin_headers)
    assert res.status_code == 200
    assert res.json()["slug"] == "coolers-e-fans"

    res = client.delete(f"/admin/categories/{cat['id']}", headers=admin_headers)
    assert res.status_code == 204


def test_duplicate_category_name_returns_409_not_500(client, admin_headers):
    client.post("/admin/categories", json={"name": "Gabinetes"}, headers=admin_headers)
    res = client.post("/admin/categories", json={"name": "Gabinetes"}, headers=admin_headers)
    assert res.status_code == 409


def test_whitespace_only_category_name_is_rejected(client, admin_headers):
    res = client.post("/admin/categories", json={"name": "   "}, headers=admin_headers)
    assert res.status_code == 422


def test_cannot_delete_category_with_products(client, admin_headers, category_id, product_id):
    res = client.delete(f"/admin/categories/{category_id}", headers=admin_headers)
    assert res.status_code == 400


def test_product_crud_and_slug_update(client, admin_headers, category_id):
    payload = {
        "name": "Fonte 650W",
        "description": "80 Plus Bronze",
        "brand": "Corsair",
        "price": 399.9,
        "stock": 10,
        "image_url": "",
        "specs": {"potencia": "650W"},
        "category_id": category_id,
    }
    res = client.post("/admin/products", json=payload, headers=admin_headers)
    assert res.status_code == 201
    product = res.json()

    payload["name"] = "Fonte 650W Bronze V2"
    payload["stock"] = 20
    res = client.put(f"/admin/products/{product['id']}", json=payload, headers=admin_headers)
    assert res.status_code == 200
    assert res.json()["stock"] == 20
    assert res.json()["slug"] != product["slug"]


def test_cannot_delete_product_with_orders(client, admin_headers, auth_headers, product_id):
    headers = auth_headers()
    client.post(
        "/orders",
        json={"items": [{"product_id": product_id, "quantity": 1}], "shipping_address": "Rua A, 123"},
        headers=headers,
    )
    res = client.delete(f"/admin/products/{product_id}", headers=admin_headers)
    assert res.status_code == 400


def test_price_above_column_limit_is_rejected(client, admin_headers, category_id):
    res = client.post(
        "/admin/products",
        json={
            "name": "Produto Caro Demais",
            "description": "",
            "brand": "X",
            "price": 999999999999,
            "stock": 1,
            "image_url": "",
            "specs": {},
            "category_id": category_id,
        },
        headers=admin_headers,
    )
    assert res.status_code == 422


def test_oversized_specs_payload_is_rejected(client, admin_headers, category_id):
    huge_specs = {f"campo_{i}": "x" * 200 for i in range(60)}
    res = client.post(
        "/admin/products",
        json={
            "name": "Produto Specs Grandes",
            "description": "",
            "brand": "X",
            "price": 10,
            "stock": 1,
            "image_url": "",
            "specs": huge_specs,
            "category_id": category_id,
        },
        headers=admin_headers,
    )
    assert res.status_code == 422

```
