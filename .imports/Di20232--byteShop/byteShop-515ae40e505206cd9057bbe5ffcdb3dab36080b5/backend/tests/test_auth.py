def test_register_and_login(client):
    res = client.post(
        "/auth/register", json={"name": "Ana Silva", "email": "ana@example.com", "password": "senha123"}
    )
    assert res.status_code == 201
    body = res.json()
    assert body["user"]["email"] == "ana@example.com"
    assert body["user"]["is_admin"] is False
    assert "access_token" in body

    res = client.post("/auth/login", json={"email": "ana@example.com", "password": "senha123"})
    assert res.status_code == 200


def test_login_wrong_password_is_generic(client, register):
    register(email="bob@example.com", password="senha123")
    res = client.post("/auth/login", json={"email": "bob@example.com", "password": "errada"})
    assert res.status_code == 401
    # Mensagem genérica de propósito: não deve revelar se o e-mail existe ou não.
    assert "inválid" in res.json()["detail"].lower()


def test_duplicate_email_is_rejected_cleanly(client, register):
    register(email="dup@example.com")
    res = client.post(
        "/auth/register", json={"name": "Outro", "email": "dup@example.com", "password": "senha123"}
    )
    assert res.status_code == 400
    assert isinstance(res.json()["detail"], str)


def test_me_requires_valid_token(client, auth_headers):
    res = client.get("/auth/me")
    assert res.status_code == 401

    headers = auth_headers()
    res = client.get("/auth/me", headers=headers)
    assert res.status_code == 200


def test_password_over_72_bytes_is_rejected(client):
    """Regressão: bcrypt trunca em 72 bytes; o schema deve rejeitar senhas
    maiores em vez de aceitar e truncar silenciosamente."""
    res = client.post(
        "/auth/register",
        json={"name": "Teste", "email": "longa@example.com", "password": "x" * 90},
    )
    assert res.status_code == 422


def test_name_with_only_whitespace_is_rejected(client):
    res = client.post(
        "/auth/register",
        json={"name": "   ", "email": "espaco@example.com", "password": "senha123"},
    )
    assert res.status_code == 422
