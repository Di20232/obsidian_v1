---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/lobsters.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/sources/lobsters.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/lobsters.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""Lobsters search. Free, no key."""

from __future__ import annotations

from .. import cache, http
from ..result import Result
from ..source_config import load

ENDPOINT = "https://lobste.rs/search.json"


class LobstersSource:
    name = "lobsters"

    def __init__(self, retries: int = 1) -> None:
        self._session = http.get_session(retries=retries, backoff=1.0)
        self._ttl = load().cache_ttl_hours

    def search(self, query: str, n: int = 10) -> list[Result]:
        cached = cache.get(self.name, query, ttl_hours=self._ttl)
        if cached is not None:
            return [Result(**r) for r in cached]

        params = {"q": query, "what": "stories", "order": "relevance"}
        try:
            r = self._session.get(ENDPOINT, params=params, timeout=http.DEFAULT_TIMEOUT)
            if r.status_code != 200:
                return []
            data = r.json()
            if isinstance(data, list):
                items = data[: min(n, 25)]
            elif isinstance(data, dict) and isinstance(data.get("stories"), list):
                items = data["stories"][: min(n, 25)]
            else:
                items = []
            results = [
                Result(
                    source="lobsters",
                    title=s.get("title") or "",
                    url=s.get("url") or s.get("short_id_url") or "",
                    points=s.get("score"),
                    comments=s.get("comment_count"),
                    posted_at=s.get("created_at"),
                    extra={"tags": s.get("tags")},
                )
                for s in items
            ]
            cache.put(self.name, query, results)
            return results
        except Exception:
            return []


__all__ = ["LobstersSource"]

```
