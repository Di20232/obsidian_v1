---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/aggregator.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/aggregator.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/aggregator.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
# scripts/research/lib/aggregator.py
"""Run multiple source clients in parallel, aggregate, never crash on per-source failure."""

from __future__ import annotations

import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import TimeoutError as FuturesTimeout
from dataclasses import asdict
from typing import Any, Protocol

from .result import Result

OVERALL_TIMEOUT_SECONDS = 30


class SourceClient(Protocol):
    name: str

    def search(self, query: str, n: int = 10) -> list[Result]: ...


def aggregate(
    query: str,
    sources: list[SourceClient],
    n_per_source: int = 10,
    timeout: float = OVERALL_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    """Run all sources in parallel. Return JSON-serializable dict."""

    results: list[Result] = []
    warnings: list[str] = []
    succeeded: set[str] = set()

    # Deliberately NOT a `with` block. Exiting the context manager calls
    # shutdown(wait=True), which blocks until every submitted future finishes -
    # so after the declared timeout elapsed and the warning was logged, the call
    # still sat waiting for the slow source. Each source retries up to 3 times at
    # 15s, so a slow-but-responding source could hold the caller for another
    # 60-70s past a bound advertised as OVERALL_TIMEOUT_SECONDS.
    ex = ThreadPoolExecutor(max_workers=len(sources))
    try:
        future_to_source = {
            ex.submit(_safe_search, s, query, n_per_source): s for s in sources
        }
        try:
            for future in as_completed(future_to_source, timeout=timeout):
                src = future_to_source[future]
                got, err = future.result()
                if err:
                    warnings.append(f"{src.name}: {err}")
                if got:
                    results.extend(got)
                    succeeded.add(src.name)
        except FuturesTimeout:
            for f, s in future_to_source.items():
                if not f.done():
                    warnings.append(f"{s.name}: timeout")
    finally:
        # Return as soon as the bound elapses; abandon anything still running.
        ex.shutdown(wait=False, cancel_futures=True)

    return {
        "topic": query,
        "results": [asdict(r) for r in results],
        "stats": {
            "sources_attempted": len(sources),
            "sources_succeeded": len(succeeded),
            "results_total": len(results),
            "success": len(succeeded) >= 3,
        },
        "warnings": warnings,
    }


def _safe_search(source: SourceClient, query: str, n: int) -> tuple[list[Result], str | None]:
    try:
        return source.search(query, n=n), None
    except Exception as e:
        print(f"[{source.name}] {type(e).__name__}: {e}", file=sys.stderr)
        return [], str(e)


__all__ = ["aggregate", "SourceClient", "OVERALL_TIMEOUT_SECONDS"]

```
