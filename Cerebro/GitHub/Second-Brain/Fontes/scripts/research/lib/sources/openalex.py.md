---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/openalex.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/sources/openalex.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/openalex.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""OpenAlex Works API. Free; polite pool when User-Agent has mailto."""

from __future__ import annotations

from .. import cache, http
from ..result import Result
from ..source_config import load

ENDPOINT = "https://api.openalex.org/works"


class OpenAlexSource:
    name = "openalex"

    def __init__(self, retries: int = 2) -> None:
        self._session = http.get_session(retries=retries, backoff=1.0)
        self._ttl = load().cache_ttl_hours

    def search(self, query: str, n: int = 10) -> list[Result]:
        cached = cache.get(self.name, query, ttl_hours=self._ttl)
        if cached is not None:
            return [Result(**r) for r in cached]

        params = {"search": query, "per-page": min(n, 25)}
        try:
            r = self._session.get(ENDPOINT, params=params, timeout=http.DEFAULT_TIMEOUT)
            if r.status_code != 200:
                return []
            results = _parse(r.json())
            cache.put(self.name, query, results)
            return results
        except Exception:
            return []


def _parse(payload: dict) -> list[Result]:
    out: list[Result] = []
    for w in payload.get("results", []):
        title = w.get("display_name") or w.get("title") or ""
        doi = w.get("doi")
        url = doi or w.get("id") or ""
        abstract = _reconstruct_abstract(w.get("abstract_inverted_index"))
        authors = [
            a.get("author", {}).get("display_name", "")
            for a in w.get("authorships", [])
        ]
        out.append(Result(
            source="openalex",
            title=title,
            url=url,
            abstract=abstract,
            authors=[a for a in authors if a],
            year=w.get("publication_year"),
            extra={"doi": doi, "cited_by_count": w.get("cited_by_count")},
        ))
    return out


def _reconstruct_abstract(inv: dict | None) -> str | None:
    """OpenAlex stores abstracts as inverted index {word: [positions]}. Reconstruct."""
    if not inv:
        return None
    pairs = []
    for word, positions in inv.items():
        for p in positions:
            pairs.append((p, word))
    pairs.sort()
    return " ".join(w for _, w in pairs) or None


__all__ = ["OpenAlexSource"]

```
