---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/wikipedia.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/sources/wikipedia.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/wikipedia.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""Wikipedia search + summary. Free; 200 req/s soft cap."""

from __future__ import annotations

import urllib.parse

from .. import cache, http
from ..result import Result
from ..source_config import load

SEARCH = "https://en.wikipedia.org/w/api.php"
SUMMARY = "https://en.wikipedia.org/api/rest_v1/page/summary/"


class WikipediaSource:
    name = "wikipedia"

    def __init__(self, retries: int = 2) -> None:
        self._session = http.get_session(retries=retries, backoff=1.0)
        self._ttl = load().cache_ttl_hours

    def search(self, query: str, n: int = 5) -> list[Result]:
        cached = cache.get(self.name, query, ttl_hours=self._ttl)
        if cached is not None:
            return [Result(**r) for r in cached]

        try:
            r = self._session.get(
                SEARCH,
                params={
                    "action": "query",
                    "list": "search",
                    "srsearch": query,
                    "srlimit": n,
                    "format": "json",
                },
                timeout=http.DEFAULT_TIMEOUT,
            )
            if r.status_code != 200:
                return []
            titles = [h["title"] for h in r.json().get("query", {}).get("search", [])]
            results = []
            for t in titles[:n]:
                summ = self._summary(t)
                if summ:
                    results.append(summ)
            cache.put(self.name, query, results)
            return results
        except Exception:
            return []

    def _summary(self, title: str) -> Result | None:
        try:
            r = self._session.get(
                SUMMARY + urllib.parse.quote(title.replace(" ", "_"), safe=""),
                timeout=http.DEFAULT_TIMEOUT,
            )
            if r.status_code != 200:
                return None
            j = r.json()
            return Result(
                source="wikipedia",
                title=j.get("title") or title,
                url=j.get("content_urls", {}).get("desktop", {}).get("page", ""),
                snippet=j.get("extract"),
            )
        except Exception:
            return None


__all__ = ["WikipediaSource"]

```
