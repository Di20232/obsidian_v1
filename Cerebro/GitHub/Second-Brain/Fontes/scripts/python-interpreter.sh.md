---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/python-interpreter.sh
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/python-interpreter.sh

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/python-interpreter.sh). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```bash
#!/usr/bin/env bash
# =============================================================================
# python-interpreter.sh - find a Python that actually runs
# =============================================================================
# Sourced by scripts that shell out to Python, and copied inline into the two
# hooks (hooks/load_vault_context.sh, hooks/validate-ai-first.sh) because those
# are handed to other harnesses' hook systems by hand and must stay standalone.
# tests/test_python_interpreter.py fails when a copy drifts.
#
# Usage:
#   . "<repo>/scripts/python-interpreter.sh"
#   PYTHON=$(osb_python) || { echo "no python" >&2; exit 1; }
#   $PYTHON script.py          # unquoted: the value may be several words
# =============================================================================

# ── osb_python ───────────────────────────────────────────────────────────────
# Echo a Python that actually runs, or nothing with a non-zero status.
# `command -v python3` is not enough, and on Windows it is actively wrong: the
# python.org installers - the default way to get Python there - ship python.exe
# and py.exe and never python3.exe, so `python3` resolves to the Microsoft Store
# App Execution Alias. That stub exists, prints nothing and exits non-zero, so an
# existence test passes and the caller silently does nothing (#269). Every
# candidate is therefore executed, not looked up. Uses bash 3.2 features only.
osb_python() {
  local candidate
  # Unquoted on purpose: "py -3" is a command plus an argument.
  for candidate in python3 python "py -3"; do
    if $candidate -c "import sys" >/dev/null 2>&1; then
      printf '%s' "$candidate"
      return 0
    fi
  done
  # Last resort: uv, which the toolkit already requires for its research scripts
  # and which brings its own interpreter when the system has none on PATH.
  if uv run --no-project python -c "import sys" >/dev/null 2>&1; then
    printf '%s' "uv run --no-project python"
    return 0
  fi
  return 1
}

```
