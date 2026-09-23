import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.config import settings
from app.routers import admin, auth, categories, orders, products

logger = logging.getLogger("uvicorn.error")

app = FastAPI(title="PC Store API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response


app.add_middleware(SecurityHeadersMiddleware)


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    # Rede de segurança: qualquer erro não previsto vira um 500 genérico para o
    # cliente (sem vazar stack trace/detalhes internos), mas o erro real é
    # registrado no log do servidor para investigação.
    logger.exception("Erro não tratado em %s %s", request.method, request.url.path)
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno no servidor. Tente novamente mais tarde."},
    )


app.include_router(categories.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(orders.router)
app.include_router(admin.router)


@app.get("/")
def root():
    return {"status": "ok", "service": "PC Store API"}
