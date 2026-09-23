---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/arxiv.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/sources/arxiv.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/sources/arxiv.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""arXiv search via the official Atom API. Free, no key, 1 req/3s polite limit."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET

from .. import cache, http
from ..result import Result
from ..source_config import load

ENDPOINT = "http://export.arxiv.org/api/query"
NS = {
    "atom": "http://www.w3.org/2005/Atom",
}


class ArxivSource:
    name = "arxiv"

    def __init__(self, retries: int = 3) -> None:
        self._session = http.get_session(retries=retries, backoff=1.0)
        self._ttl = load().cache_ttl_hours

    def search(self, query: str, n: int = 10) -> list[Result]:
        cached = cache.get(self.name, query, ttl_hours=self._ttl)
        if cached is not None:
            return [Result(**r) for r in cached]

        params = {"search_query": f"all:{query}", "start": 0, "max_results": n}
        try:
            r = self._session.get(ENDPOINT, params=params, timeout=http.DEFAULT_TIMEOUT)
            if r.status_code != 200:
                return []
            results = _parse(r.text)
            cache.put(self.name, query, results)
            return results
        except Exception:
            return []


def _parse(atom_xml: str) -> list[Result]:
    try:
        root = ET.fromstring(atom_xml)
    except ET.ParseError:
        return []

    out: list[Result] = []
    for entry in root.findall("atom:entry", NS):
        title = _text(entry.find("atom:title", NS))
        summary = _text(entry.find("atom:summary", NS))
        link_el = entry.find("atom:link[@rel='alternate']", NS)
        url = link_el.attrib.get("href", "") if link_el is not None else ""
        published = _text(entry.find("atom:published", NS))
        year = _year(published)
        authors = [
            _text(a.find("atom:name", NS))
            for a in entry.findall("atom:author", NS)
            if a.find("atom:name", NS) is not None
        ]
        out.append(
            Result(
                source="arxiv",
                title=title,
                url=url,
                abstract=summary,
                authors=[a for a in authors if a],
                year=year,
                posted_at=published or None,
            )
        )
    return out


def _text(el) -> str:
    return (el.text or "").strip() if el is not None else ""


def _year(iso_date: str) -> int | None:
    m = re.match(r"^(\d{4})", iso_date or "")
    return int(m.group(1)) if m else None


__all__ = ["ArxivSource"]

```
