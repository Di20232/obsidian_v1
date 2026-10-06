---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_schema_coverage.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# tests/test_schema_coverage.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_schema_coverage.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""Every note type a command mandates must have a schema (fix 20/24).

The audit found five note types that commands create with no schema in
ai-first-rules.md, so every writer improvised its own shape. This fence
cross-references the types commanded against the constitution.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

TYPE_RE = re.compile(r"`type: ([a-z][a-z0-9-]*)`")
# Frontmatter *values* that look like types but are field values, not note types.
NOT_TYPES = {"board"}


def test_every_commanded_type_has_a_schema():
    rules = (REPO_ROOT / "references" / "ai-first-rules.md").read_text(encoding="utf-8")
    missing: list[str] = []
    for md in sorted((REPO_ROOT / "commands").glob("*.md")):
        for t in set(TYPE_RE.findall(md.read_text(encoding="utf-8"))):
            if t in NOT_TYPES:
                continue
            if f"type: {t}" not in rules:
                missing.append(f"{md.name}: `type: {t}` has no schema in ai-first-rules.md")
    assert missing == [], "\n".join(missing)

```
