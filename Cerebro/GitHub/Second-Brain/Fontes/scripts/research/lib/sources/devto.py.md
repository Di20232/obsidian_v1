---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/devto.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/sources/devto.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/devto.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""dev.to articles by tag. Free, no key. Best-effort: query slugified as tag."""

from __future__ import annotations

import re

from .. import cache, http
from ..result import Result
from ..source_config import load

ENDPOINT = "https://dev.to/api/articles"


class DevToSource:
    name = "devto"

    def __init__(self, retries: int = 1) -> None:
        self._session = http.get_session(retries=retries, backoff=1.0)
        self._ttl = load().cache_ttl_hours

    def search(self, query: str, n: int = 10) -> list[Result]:
        cached = cache.get(self.name, query, ttl_hours=self._ttl)
        if cached is not None:
            return [Result(**r) for r in cached]

        tag = _query_to_tag(query)
        params = {"per_page": min(n, 30), "tag": tag} if tag else {"per_page": min(n, 30)}
        try:
            r = self._session.get(ENDPOINT, params=params, timeout=http.DEFAULT_TIMEOUT)
            if r.status_code != 200:
                return []
            results = [
                Result(
                    source="devto",
                    title=a.get("title") or "",
                    url=a.get("url") or "",
                    snippet=a.get("description"),
                    points=a.get("public_reactions_count"),
                    comments=a.get("comments_count"),
                    posted_at=a.get("published_at"),
                    extra={"tag_list": a.get("tag_list")},
                )
                for a in r.json()
            ]
            cache.put(self.name, query, results)
            return results
        except Exception:
            return []


def _query_to_tag(q: str) -> str | None:
    # Strip non-alphanum, take first word >= 3 chars
    words = re.findall(r"[a-z0-9]+", q.lower())
    return next((w for w in words if len(w) >= 3), None)


__all__ = ["DevToSource"]

```
