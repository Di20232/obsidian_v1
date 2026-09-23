---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_folder_map_compliance.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# tests/test_folder_map_compliance.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_folder_map_compliance.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""The folder-map rule is a fence now, not a sign (stress-test fix 18/24).

references/folder-map.md has said "never hardcode a folder name in a command
body" since it existed; sixteen commands violated it anyway, so on the skill's
own default-bootstrapped (Obsidian-style) vault /obsidian-export produced an
empty snapshot and /obsidian-learn scanned folders that don't exist. This lint
fails CI when a swept command mentions a bare vault folder outside a
folder-map resolution context.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# The commands the stress-test sweep fixed. New commands should be born
# compliant and can be added here as they are reviewed.
SWEPT = [
    "idea-discovery.md", "obsidian-architect.md", "obsidian-board.md",
    "obsidian-calendar.md", "obsidian-daily.md", "obsidian-emerge.md",
    "obsidian-export.md", "obsidian-ingest.md", "obsidian-learn.md", "obsidian-panel.md",
    "obsidian-person.md", "obsidian-project.md", "obsidian-projects.md",
    "obsidian-recap.md", "obsidian-reconcile.md", "obsidian-recurring.md",
    "obsidian-synthesize.md", "obsidian-task.md", "vault-deep-synthesis.md",
]

# A hardcoded vault folder: wiki-style subfolders or the Obsidian-style roots,
# used as a path. Lines that carry their own folder-map context are exempt -
# naming both styles next to the resolution reference is exactly the idiom the
# sweep introduced.
HARDCODED = re.compile(
    r"`(wiki/(entities|concepts|projects|daily|decisions|logs|reviews|tasks|meetings|agenda)/"
    r"|(People|Projects|Ideas|Knowledge|Boards|Tasks|Daily|Reviews|Meetings|Agenda)/)"
)
EXEMPT = ("folder-map", "wiki-style", "Obsidian-style", "resolved in step")


def test_swept_commands_resolve_folders_via_the_map():
    offenders: list[str] = []
    for name in SWEPT:
        path = REPO_ROOT / "commands" / name
        text = path.read_text(encoding="utf-8")
        assert "folder-map" in text, f"{name}: never references folder-map.md"
        for i, line in enumerate(text.splitlines(), start=1):
            if HARDCODED.search(line) and not any(e in line for e in EXEMPT):
                offenders.append(f"{name}:{i}: {line.strip()[:90]}")
    assert offenders == [], (
        "hardcoded vault folders outside a folder-map context:\n" + "\n".join(offenders)
    )


def test_folder_map_covers_every_type_commands_write():
    """The two dead-ends the audit found: agenda snapshots and recurring tasks
    had no row, so 'resolve per folder-map' had nothing to resolve to."""
    table = (REPO_ROOT / "references" / "folder-map.md").read_text(encoding="utf-8")
    assert "Agenda snapshot" in table
    assert "Recurring obligation" in table

```
