---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/README.md
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# README.md

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/README.md). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

# ByteShop — E-commerce de Peças e Periféricos

Projeto de estudo/portfólio inspirado em lojas como a KaBuM, focado em peças de computador e periféricos.

## Stack

- **Backend:** Python + FastAPI + SQLAlchemy + SQLite + JWT (autenticação)
- **Frontend:** React + TypeScript + Vite + Tailwind CSS v4 + React Router
- **Pagamento:** simulado (sem gateway real) — pensado para portfólio/estudo

## Estrutura

```
backend/    API FastAPI (produtos, categorias, auth, pedidos)
frontend/   SPA React (catálogo, carrinho, checkout, login, pedidos)
```

## Como rodar

### 1. Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
copy .env.example .env       # edite SECRET_KEY se quiser
python -m app.seed           # cria o arquivo ecommerce.db e popula produtos de exemplo
uvicorn app.main:app --reload --port 8000
```

O banco é um arquivo SQLite (`backend/ecommerce.db`), criado automaticamente pelo seed. Para inspecionar os dados no DBeaver: **Nova Conexão → SQLite** e aponte para esse arquivo.

API disponível em `http://localhost:8000` (docs interativas em `/docs`).

### 2. Frontend

```bash
cd frontend
npm install
copy .env.example .env       # confirme VITE_API_URL=http://localhost:8000
npm run dev
```

App disponível em `http://localhost:5173`.

## Funcionalidades (MVP)

- Catálogo de produtos com filtro por categoria, busca, ordenação e paginação
- Página de detalhes do produto com especificações técnicas
- Carrinho de compras (persistido no navegador)
- Cadastro/login de usuário (JWT)
- Checkout com endereço de entrega e pagamento simulado
- Histórico de pedidos do usuário
- Painel administrativo (CRUD de produtos/estoque e categorias)

## Testes e qualidade (backend)

```bash
cd backend
venv\Scripts\activate
pip install -r requirements-dev.txt
pytest              # 38 testes: auth, produtos, pedidos, admin e segurança
ruff check app/     # lint
pip-audit           # vulnerabilidades conhecidas nas dependências
```

## Painel administrativo

Acessível em `/admin` para usuários com `is_admin = true`. Por padrão, todo usuário cadastrado é comum.

Para promover um usuário a administrador:

```bash
cd backend
venv\Scripts\activate
python -m app.make_admin email@do-usuario.com
```

O link "Painel Admin" aparece na navbar assim que o usuário logado for admin.

## Próximos passos sugeridos

- Avaliações de produtos
- Cupons de desconto
- Integração de pagamento real (Mercado Pago/Stripe)
- Upload de imagens (hoje o painel aceita apenas URL de imagem)
