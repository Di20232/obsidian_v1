---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_setup_settings_hook.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# tests/test_setup_settings_hook.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_setup_settings_hook.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""The skill installer must register the SessionStart context hook idempotently, so a
skill-installed command can locate the skill root the same way a plugin-installed one
does. Guards scripts/setup_settings_hook.py's pure register() (no real settings.json is
touched here)."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import setup_settings_hook as sh  # noqa: E402


def _commands(settings: dict) -> list[str]:
    return [
        h.get("command", "")
        for group in settings.get("hooks", {}).get("SessionStart", [])
        for h in group.get("hooks", [])
    ]


def test_adds_hook_to_empty_settings():
    settings, action = sh.register({})
    assert action == "added"
    assert sh.HOOK_CMD in _commands(settings)


def test_is_idempotent():
    settings, _ = sh.register({})
    settings, action = sh.register(settings)
    assert action == "unchanged"
    # Registered exactly once, never duplicated.
    assert _commands(settings).count(sh.HOOK_CMD) == 1


def test_refreshes_a_stale_path_without_duplicating():
    settings = {
        "hooks": {
            "SessionStart": [
                {"matcher": "", "hooks": [
                    {"type": "command", "command": "python3 /old/path/hooks/load_vault_context.py"}
                ]}
            ]
        }
    }
    settings, action = sh.register(settings)
    assert action == "refreshed"
    assert _commands(settings) == [sh.HOOK_CMD]


def test_preserves_unrelated_settings_and_hooks():
    settings = {
        "model": "claude-fable-5",
        "hooks": {
            "SessionStart": [
                {"matcher": "", "hooks": [{"type": "command", "command": "/other/peon.sh"}]}
            ],
            "Stop": [{"matcher": "", "hooks": [{"type": "command", "command": "/other/peon.sh"}]}],
        },
    }
    settings, action = sh.register(settings)
    assert action == "added"
    assert settings["model"] == "claude-fable-5"
    assert "Stop" in settings["hooks"]
    # The pre-existing SessionStart hook survives alongside ours.
    assert "/other/peon.sh" in _commands(settings)
    assert sh.HOOK_CMD in _commands(settings)

```
