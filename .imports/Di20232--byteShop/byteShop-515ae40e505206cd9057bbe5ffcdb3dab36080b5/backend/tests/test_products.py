def test_list_products_empty(client):
    res = client.get("/products")
    assert res.status_code == 200
    body = res.json()
    assert body["items"] == []
    assert body["total"] == 0
    assert body["pages"] == 1


def test_public_product_list_and_detail(client, admin_headers, category_id):
    client.post(
        "/admin/products",
        json={
            "name": "Placa de Vídeo RTX 4060",
            "description": "",
            "brand": "NVIDIA",
            "price": 2000,
            "stock": 3,
            "image_url": "",
            "specs": {"memoria": "8GB"},
            "category_id": category_id,
        },
        headers=admin_headers,
    )

    res = client.get("/products")
    assert res.status_code == 200
    assert res.json()["total"] == 1

    slug = res.json()["items"][0]["slug"]
    res = client.get(f"/products/{slug}")
    assert res.status_code == 200
    assert res.json()["specs"]["memoria"] == "8GB"


def test_get_unknown_slug_returns_404(client):
    res = client.get("/products/nao-existe")
    assert res.status_code == 404


def test_filter_by_category(client, admin_headers, category_id):
    other_category = client.post(
        "/admin/categories", json={"name": "Memória RAM"}, headers=admin_headers
    ).json()

    client.post(
        "/admin/products",
        json={
            "name": "CPU X",
            "description": "",
            "brand": "AMD",
            "price": 100,
            "stock": 1,
            "image_url": "",
            "specs": {},
            "category_id": category_id,
        },
        headers=admin_headers,
    )
    client.post(
        "/admin/products",
        json={
            "name": "RAM Y",
            "description": "",
            "brand": "Corsair",
            "price": 200,
            "stock": 1,
            "image_url": "",
            "specs": {},
            "category_id": other_category["id"],
        },
        headers=admin_headers,
    )

    res = client.get("/products", params={"category": other_category["slug"]})
    assert res.status_code == 200
    assert res.json()["total"] == 1
    assert res.json()["items"][0]["name"] == "RAM Y"
