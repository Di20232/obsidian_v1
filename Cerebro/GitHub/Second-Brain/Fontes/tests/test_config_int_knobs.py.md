---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_config_int_knobs.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# tests/test_config_int_knobs.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_config_int_knobs.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""config.get_optional_int: the TX_LIMIT knobs from #234 must fail with the
variable named, not an int() traceback, when someone writes `480k`."""

from __future__ import annotations

import os

import pytest

os.environ.setdefault("OBSIDIAN_VAULT_PATH", "/nonexistent/vault-for-tests")

from scripts.research.lib import config  # noqa: E402


def test_default_when_unset(monkeypatch):
    monkeypatch.delenv("YOUTUBE_TX_LIMIT", raising=False)
    assert config.get_optional_int("YOUTUBE_TX_LIMIT", 480000) == 480000


def test_integer_value_is_read(monkeypatch):
    monkeypatch.setenv("PODCAST_TX_LIMIT", " 24000 ")
    assert config.get_optional_int("PODCAST_TX_LIMIT", 480000) == 24000


@pytest.mark.parametrize("bad", ["480k", "1e6", "24,000", "lots"])
def test_non_integer_exits_naming_the_variable(monkeypatch, bad):
    monkeypatch.setenv("PODCAST_TX_LIMIT", bad)
    with pytest.raises(SystemExit) as exc:
        config.get_optional_int("PODCAST_TX_LIMIT", 480000)
    assert "PODCAST_TX_LIMIT" in str(exc.value)
    assert bad in str(exc.value)

```
