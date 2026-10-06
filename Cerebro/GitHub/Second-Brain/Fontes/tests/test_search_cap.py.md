---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_search_cap.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# tests/test_search_cap.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_search_cap.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""The lexical scan cap must be big, deterministic, and loud (fix 12/24).

The old cap silently scanned 2,000 files in arbitrary filesystem order, making
~342 of a 2,342-note vault randomly unsearchable. Now: notes iterate
newest-first (a cap that bites drops the OLDEST notes), the default cap covers
real vaults with an env knob, and truncation warns on stderr.
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "integrations" / "obsidian-mcp-server"))

import vault_ops  # noqa: E402


@pytest.fixture()
def vault(tmp_path, monkeypatch):
    v = tmp_path / "vault"
    v.mkdir()
    monkeypatch.setenv(vault_ops._VAULT_ENV, str(v))
    return v


def _note(vault: Path, name: str, body: str, age_days: int) -> Path:
    p = vault / name
    p.write_text(f"---\ntype: note\n---\n\n{body}\n", encoding="utf-8")
    stamp = time.time() - age_days * 86400
    os.utime(p, (stamp, stamp))
    return p


def test_iter_notes_is_newest_first(vault):
    _note(vault, "old.md", "ancient", age_days=30)
    _note(vault, "mid.md", "middling", age_days=10)
    _note(vault, "new.md", "fresh", age_days=1)

    order = [p.name for p in vault_ops._iter_notes(vault)]
    assert order == ["new.md", "mid.md", "old.md"]


def test_cap_bites_oldest_first_and_warns(vault, monkeypatch, capsys):
    for i in range(5):
        _note(vault, f"note-{i}.md", f"filler text number {i}", age_days=i + 2)
    _note(vault, "newest.md", "zebra fact lives here", age_days=0)
    _note(vault, "oldest.md", "yeti fact lives here", age_days=60)

    monkeypatch.setattr(vault_ops, "_MAX_FILES_SCANNED", 3)

    hits = vault_ops.search("zebra", limit=5, semantic=False)
    assert [r["path"] for r in hits] == ["newest.md"]

    misses = vault_ops.search("yeti", limit=5, semantic=False)
    assert misses == []
    err = capsys.readouterr().err
    assert "scanned only the newest 3 notes" in err
    assert "OBSIDIAN_SEARCH_MAX_FILES" in err


def test_default_cap_covers_real_vaults(vault, capsys):
    _note(vault, "a.md", "zebra here", age_days=1)
    assert vault_ops._MAX_FILES_SCANNED >= 10000
    vault_ops.search("zebra", limit=5, semantic=False)
    assert "scanned only" not in capsys.readouterr().err

```
