---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/tests/test_security.py
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# backend/tests/test_security.py

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/tests/test_security.py). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
import base64
import hashlib
import hmac
import json

import pytest

from app.config import Settings, settings


@pytest.mark.parametrize(
    "weak_key",
    ["dev-secret-key", "troque-esta-chave-por-uma-string-aleatoria-segura", "changeme", "curta-demais"],
)
def test_weak_secret_key_is_rejected_at_startup(weak_key):
    """Regressão crítica: o servidor não pode subir com a chave-modelo (ou
    qualquer chave curta/previsível), pois isso permite forjar tokens JWT
    válidos para qualquer usuário sem saber a senha."""
    bad_settings = Settings(secret_key=weak_key)
    with pytest.raises(RuntimeError):
        bad_settings.validate_secret_key()


def test_current_configured_secret_key_is_strong():
    settings.validate_secret_key()  # não deve levantar exceção


def _forge_token(payload: dict, secret: str = settings.secret_key) -> str:
    def b64(data: bytes) -> bytes:
        return base64.urlsafe_b64encode(data).rstrip(b"=")

    header = b64(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    body = b64(json.dumps(payload, separators=(",", ":")).encode())
    msg = header + b"." + body
    sig = b64(hmac.new(secret.encode(), msg, hashlib.sha256).digest())
    return (msg + b"." + sig).decode()


def test_token_with_non_numeric_sub_is_rejected_not_crashed(client):
    """Regressão: int(user_id) ficava fora do try/except e derrubava a API
    com 500 quando o token tinha uma claim 'sub' não numérica."""
    token = _forge_token({"sub": "abc", "exp": 9999999999})
    res = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 401
    assert res.json()["detail"] != "Internal Server Error"


def test_token_signed_with_wrong_secret_is_rejected(client):
    token = _forge_token({"sub": "1", "exp": 9999999999}, secret="chave-errada-qualquer")
    res = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 401


def test_garbage_token_does_not_crash(client):
    res = client.get("/auth/me", headers={"Authorization": "Bearer isso-nao-eh-um-jwt"})
    assert res.status_code == 401


def test_login_is_rate_limited_after_repeated_failures(client, register):
    register(email="alvo@example.com", password="senha123")

    statuses = []
    for _ in range(15):
        res = client.post("/auth/login", json={"email": "alvo@example.com", "password": "errada"})
        statuses.append(res.status_code)

    assert 401 in statuses
    assert 429 in statuses, "esperava bloqueio (429) após várias tentativas de login"


def test_security_headers_present(client):
    res = client.get("/")
    assert res.headers.get("x-content-type-options") == "nosniff"
    assert res.headers.get("x-frame-options") == "DENY"


def test_unhandled_exception_returns_generic_500_json(client):
    """O handler global não deve deixar uma exceção verdadeiramente
    inesperada vazar como um erro cru sem corpo JSON seguro. Simulamos a
    falha substituindo a dependência de banco por uma que sempre quebra."""
    from app.database import get_db
    from app.main import app

    def _broken_db():
        raise RuntimeError("falha simulada de conexão com o banco")
        yield  # pragma: no cover - torna esta função um generator, como get_db exige

    app.dependency_overrides[get_db] = _broken_db
    try:
        res = client.get("/categories")
    finally:
        del app.dependency_overrides[get_db]

    assert res.status_code == 500
    assert res.json()["detail"] == "Erro interno no servidor. Tente novamente mais tarde."

```
