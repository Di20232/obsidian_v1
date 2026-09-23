---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_doc_roster.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# tests/test_doc_roster.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_doc_roster.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""SKILL.md and README.md must know every command that exists (fix 22/24).

The audit found six SKILL sections describing removed flows or stale steps,
and README counts that disagreed with the filesystem. The roster fence: every
command file appears in both docs, and the headline count is the file count.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_every_command_is_in_skill_and_readme():
    commands = sorted(p.stem for p in (REPO_ROOT / "commands").glob("*.md"))
    skill = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    missing = [f"SKILL.md lacks {c}" for c in commands if c not in skill]
    missing += [f"README.md lacks {c}" for c in commands if c not in readme]
    assert missing == [], "\n".join(missing)


def test_headline_count_matches_filesystem():
    n = len(list((REPO_ROOT / "commands").glob("*.md")))
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert f"{n} commands" in readme, f"README does not state the real count ({n})"
    assert f"## {n} Commands" in readme, "README's command-table heading disagrees"

```
