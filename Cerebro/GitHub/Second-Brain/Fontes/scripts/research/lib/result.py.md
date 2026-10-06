---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/result.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/result.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/result.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""Typed result returned by every source client. Pure data, no behavior."""

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class Result:
    """A single search result. Sources fill the fields they have; rest stay None."""

    source: str
    title: str
    url: str
    snippet: str | None = None  # web/discourse one-line preview
    abstract: str | None = None  # academic full abstract
    authors: list[str] | None = None  # academic
    year: int | None = None  # academic
    points: int | None = None  # HN score / Reddit upvotes
    comments: int | None = None  # discourse comment count
    posted_at: str | None = None  # ISO 8601 date if known
    extra: dict[str, Any] = field(default_factory=dict)  # per-source extras (doi, etc.)


def encode_results(obj: Any) -> Any:
    """`json.dumps` default= callable. Serializes Result to plain dict."""
    if isinstance(obj, Result):
        return asdict(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

```
