---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/semantic_scholar.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/sources/semantic_scholar.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/semantic_scholar.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""Semantic Scholar Graph API. Free; 100 req/5min unauth, polite to throttle."""

from __future__ import annotations

import json

from .. import cache, http
from ..result import Result
from ..source_config import load

ENDPOINT = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = "title,abstract,authors,year,url,externalIds"


class SemanticScholarSource:
    name = "semantic_scholar"

    def __init__(self, retries: int = 2) -> None:
        self._session = http.get_session(retries=retries, backoff=2.0)
        self._ttl = load().cache_ttl_hours

    def search(self, query: str, n: int = 10) -> list[Result]:
        cached = cache.get(self.name, query, ttl_hours=self._ttl)
        if cached is not None:
            return [Result(**r) for r in cached]

        params = {"query": query, "limit": min(n, 100), "fields": FIELDS}
        try:
            r = self._session.get(ENDPOINT, params=params, timeout=http.DEFAULT_TIMEOUT)
            if r.status_code != 200:
                return []
            results = _parse(r.json())
            cache.put(self.name, query, results)
            return results
        except (json.JSONDecodeError, Exception):
            return []


def _parse(payload: dict) -> list[Result]:
    out: list[Result] = []
    for paper in payload.get("data", []):
        authors = [a.get("name", "") for a in paper.get("authors") or []]
        doi = (paper.get("externalIds") or {}).get("DOI")
        url = paper.get("url") or (f"https://doi.org/{doi}" if doi else "")
        out.append(
            Result(
                source="semantic_scholar",
                title=paper.get("title") or "",
                url=url,
                abstract=paper.get("abstract"),
                authors=[a for a in authors if a],
                year=paper.get("year"),
                extra={"doi": doi} if doi else {},
            )
        )
    return out


__all__ = ["SemanticScholarSource"]

```
