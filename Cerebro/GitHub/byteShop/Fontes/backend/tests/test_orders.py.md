---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/tests/test_orders.py
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# backend/tests/test_orders.py

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/tests/test_orders.py). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
def test_create_order_happy_path(client, auth_headers, product_id):
    headers = auth_headers()
    res = client.post(
        "/orders",
        json={"items": [{"product_id": product_id, "quantity": 2}], "shipping_address": "Rua A, 123"},
        headers=headers,
    )
    assert res.status_code == 201
    body = res.json()
    assert body["status"] == "pago"
    assert float(body["total"]) == 200.0  # 2 x R$100
    assert len(body["items"]) == 1


def test_create_order_requires_auth(client, product_id):
    res = client.post(
        "/orders",
        json={"items": [{"product_id": product_id, "quantity": 1}], "shipping_address": "Rua A, 123"},
    )
    assert res.status_code == 401


def test_insufficient_stock_is_rejected_and_stock_unchanged(client, auth_headers, product_id):
    headers = auth_headers()
    res = client.post(
        "/orders",
        json={"items": [{"product_id": product_id, "quantity": 999}], "shipping_address": "Rua A, 123"},
        headers=headers,
    )
    assert res.status_code == 400

    # nenhum pedido deve ter sido criado a partir da tentativa que falhou
    orders = client.get("/orders", headers=headers).json()
    assert orders == []


def test_stock_is_decremented_atomically_across_two_orders(client, auth_headers, product_id):
    """Regressão do bug de condição de corrida: duas compras sequenciais da
    mesma última unidade não podem, juntas, deixar o estoque negativo."""
    headers = auth_headers()

    res1 = client.post(
        "/orders",
        json={"items": [{"product_id": product_id, "quantity": 5}], "shipping_address": "Rua A, 123"},
        headers=headers,
    )
    assert res1.status_code == 201  # esvazia o estoque (era 5)

    res2 = client.post(
        "/orders",
        json={"items": [{"product_id": product_id, "quantity": 1}], "shipping_address": "Rua A, 123"},
        headers=headers,
    )
    assert res2.status_code == 400
    assert "estoque" in res2.json()["detail"].lower()


def test_order_with_nonexistent_product_returns_404(client, auth_headers):
    headers = auth_headers()
    res = client.post(
        "/orders",
        json={"items": [{"product_id": 99999, "quantity": 1}], "shipping_address": "Rua A, 123"},
        headers=headers,
    )
    assert res.status_code == 404


def test_get_order_scoped_to_owner(client, auth_headers, product_id):
    headers_a = auth_headers(email="a@example.com")
    headers_b = auth_headers(email="b@example.com")

    order = client.post(
        "/orders",
        json={"items": [{"product_id": product_id, "quantity": 1}], "shipping_address": "Rua A, 123"},
        headers=headers_a,
    ).json()

    # dono consegue ver
    res = client.get(f"/orders/{order['id']}", headers=headers_a)
    assert res.status_code == 200

    # outro usuário não consegue ver o pedido alheio (sem IDOR)
    res = client.get(f"/orders/{order['id']}", headers=headers_b)
    assert res.status_code == 404


def test_order_with_multiple_items_returns_all_of_them(client, auth_headers, admin_headers, category_id):
    """Regressão: joinedload de coleção sem .unique() pode, em tese, truncar
    itens; garantimos aqui que todos os itens de um pedido multi-produto
    voltam completos tanto na criação quanto na consulta posterior."""
    ids = []
    for name, price in [("Produto 1", 10), ("Produto 2", 20), ("Produto 3", 30)]:
        res = client.post(
            "/admin/products",
            json={
                "name": name,
                "description": "",
                "brand": "X",
                "price": price,
                "stock": 5,
                "image_url": "",
                "specs": {},
                "category_id": category_id,
            },
            headers=admin_headers,
        )
        ids.append(res.json()["id"])

    headers = auth_headers()
    order = client.post(
        "/orders",
        json={
            "items": [{"product_id": pid, "quantity": 1} for pid in ids],
            "shipping_address": "Rua A, 123",
        },
        headers=headers,
    ).json()
    assert len(order["items"]) == 3

    fetched = client.get(f"/orders/{order['id']}", headers=headers).json()
    assert len(fetched["items"]) == 3

```
