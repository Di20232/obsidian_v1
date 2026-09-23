---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/rate_limit.py
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# backend/app/rate_limit.py

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/backend/app/rate_limit.py). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""Limitador de taxa simples em memória, para reduzir força bruta em endpoints
sensíveis (login/cadastro). Não substitui um limitador distribuído (ex: Redis)
em produção com múltiplos processos/instâncias, mas é suficiente para um
único processo — que é como este projeto roda."""

import time

from fastapi import HTTPException, Request, status

_hits: dict[str, list[float]] = {}


def _forget_expired_keys(window_seconds: int, now: float) -> None:
    """Remove entradas cujas tentativas já saíram da janela de tempo.

    Sem isto, cada combinação (rota, IP) que já bateu no endpoint uma vez
    ficaria para sempre no dicionário — mesmo muito tempo depois de suas
    tentativas terem expirado — crescendo sem limite pela vida do processo."""
    for key in [k for k, timestamps in _hits.items() if all(now - t >= window_seconds for t in timestamps)]:
        del _hits[key]


def rate_limiter(max_attempts: int, window_seconds: int):
    def dependency(request: Request) -> None:
        client_host = request.client.host if request.client else "unknown"
        key = f"{request.url.path}:{client_host}"
        now = time.time()

        _forget_expired_keys(window_seconds, now)

        attempts = [t for t in _hits.get(key, []) if now - t < window_seconds]
        if len(attempts) >= max_attempts:
            _hits[key] = attempts
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Muitas tentativas. Aguarde um momento antes de tentar novamente.",
            )

        attempts.append(now)
        _hits[key] = attempts

    return dependency

```
