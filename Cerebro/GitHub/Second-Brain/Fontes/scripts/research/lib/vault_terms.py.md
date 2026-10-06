---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/vault_terms.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/lib/vault_terms.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/lib/vault_terms.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""Topic tokenization for vault scans - delegates to the search tokenizer.

One tokenizer, one fix (#159, #188, #192, #212): `vault_scan` in notebooklm.py
and research_deep.py each kept a private whitespace-split + `len(w) > 2` copy
that returned nothing for CJK topics, and the copies survived three fixes to
the canonical tokenizer because every fix landed in one path and not the
others. This module is the single sanctioned import path to
`vault_ops._query_terms` for the research toolkit; do not re-implement
tokenization here or in a caller.
"""

from __future__ import annotations

import sys
from pathlib import Path

_MCP_DIR = Path(__file__).resolve().parents[3] / "integrations" / "obsidian-mcp-server"


def topic_terms(topic: str) -> list[str]:
    """CJK-aware meaningful terms for a research topic.

    Lowercased, stopwords dropped, CJK runs expanded to bigrams - exactly what
    vault search itself matches on, so a topic that finds notes in search
    finds the same notes in a scan.
    """
    if str(_MCP_DIR) not in sys.path:
        sys.path.insert(0, str(_MCP_DIR))
    import vault_ops
    return vault_ops._query_terms(topic)

```
