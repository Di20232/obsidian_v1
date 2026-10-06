---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/brave.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/sources/brave.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/brave.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""Brave Search source. Optional keyed extra for the free-mode pool.

Joins the aggregation pool only when BRAVE_API_KEY is set (the caller checks;
see research._free_sources). Brave bills per use: $5/1,000 requests with $5 free
credits monthly (as of 2026-07, api-dashboard.search.brave.com).
Plain requests - no SDK. Design mirrors the fork that first built it
(fork-insights round 2, the brave-source fork).
"""

from __future__ import annotations

import os

from .. import cache, http
from ..result import Result
from ..source_config import load

API_URL = "https://api.search.brave.com/res/v1/web/search"


class BraveSource:
    name = "brave"

    def __init__(self, retries: int = 1) -> None:
        key = os.environ.get("BRAVE_API_KEY", "").strip()
        if not key:
            raise RuntimeError("BraveSource requires BRAVE_API_KEY")
        self._key = key
        self._session = http.get_session(retries=retries, backoff=1.0)
        self._ttl = load().cache_ttl_hours

    def search(self, query: str, n: int = 10) -> list[Result]:
        cached = cache.get(self.name, query, ttl_hours=self._ttl)
        if cached is not None:
            return [Result(**r) for r in cached]

        resp = self._session.get(
            API_URL,
            params={"q": query, "count": min(n, 20)},
            headers={"X-Subscription-Token": self._key, "Accept": "application/json"},
            timeout=http.DEFAULT_TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()

        results = [
            Result(
                source=self.name,
                title=item.get("title") or "",
                url=item.get("url") or "",
                snippet=item.get("description") or None,
                posted_at=item.get("page_age") or None,
            )
            for item in (data.get("web") or {}).get("results", [])
            if item.get("url")
        ]
        if results:
            cache.put(self.name, query, results)
        return results


__all__ = ["BraveSource"]

```
