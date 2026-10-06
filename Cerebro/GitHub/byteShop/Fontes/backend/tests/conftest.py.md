---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/tests/conftest.py
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# backend/tests/conftest.py

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/tests/conftest.py). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from app import rate_limit
from app.database import Base, get_db
from app.main import app


@pytest.fixture()
def client(tmp_path):
    """TestClient com um banco SQLite isolado (arquivo temporário) por teste,
    para nenhum teste afetar o banco de dados real de desenvolvimento nem
    outro teste."""
    db_path = tmp_path / "test.db"
    engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False})

    @event.listens_for(engine, "connect")
    def _enable_foreign_keys(dbapi_connection, _):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    # raise_server_exceptions=False: queremos testar o comportamento HTTP real
    # (o que um cliente de verdade recebe), não a exceção Python crua — que é
    # o padrão do TestClient e mascara handlers de exceção que funcionam
    # perfeitamente bem contra o servidor real.
    with TestClient(app, raise_server_exceptions=False) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def _reset_rate_limiter():
    """O rate limiter usa um dict em memória a nível de módulo (mesmo entre
    testes, já que a app é importada uma única vez pelo processo do pytest).
    Sem isso, testes que fazem várias tentativas de login/cadastro iriam
    esbarrar no limite um do outro de forma instável."""
    rate_limit._hits.clear()
    yield
    rate_limit._hits.clear()


@pytest.fixture()
def register(client):
    def _register(name="Usuário Teste", email="teste@example.com", password="senha123"):
        res = client.post("/auth/register", json={"name": name, "email": email, "password": password})
        assert res.status_code == 201, res.text
        return res.json()

    return _register


@pytest.fixture()
def auth_headers(register):
    def _headers(**kwargs):
        data = register(**kwargs)
        return {"Authorization": f"Bearer {data['access_token']}"}

    return _headers


@pytest.fixture()
def admin_headers(client, auth_headers):
    from app import models

    headers = auth_headers(email="admin@example.com")
    # Promove o usuário recém-criado a admin diretamente no banco de teste,
    # do mesmo jeito que o script app.make_admin faz em produção.
    db = next(app.dependency_overrides[get_db]())
    user = db.query(models.User).filter_by(email="admin@example.com").first()
    user.is_admin = True
    db.commit()
    db.close()
    return headers


@pytest.fixture()
def category_id(client, admin_headers):
    res = client.post("/admin/categories", json={"name": "Processadores"}, headers=admin_headers)
    assert res.status_code == 201, res.text
    return res.json()["id"]


@pytest.fixture()
def product_id(client, admin_headers, category_id):
    res = client.post(
        "/admin/products",
        json={
            "name": "Ryzen 5 5600",
            "description": "CPU de teste",
            "brand": "AMD",
            "price": 100.0,
            "stock": 5,
            "image_url": "",
            "specs": {},
            "category_id": category_id,
        },
        headers=admin_headers,
    )
    assert res.status_code == 201, res.text
    return res.json()["id"]

```
