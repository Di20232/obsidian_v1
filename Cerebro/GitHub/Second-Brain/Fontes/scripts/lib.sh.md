---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/lib.sh
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/lib.sh

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/lib.sh). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```bash
#!/usr/bin/env bash
# =============================================================================
# scripts/lib.sh - Shared utility helpers for build orchestration
# =============================================================================
# Sourced by scripts/build.sh. Provides logging primitives and error helpers.
# Do NOT execute directly.
# =============================================================================

# Colour codes for terminal output
if [[ -t 1 ]]; then
  _C_RESET="$(printf '\033[0m')"
  _C_INFO="$(printf '\033[36m')"
  _C_OK="$(printf '\033[32m')"
  _C_WARN="$(printf '\033[33m')"
  _C_ERR="$(printf '\033[31m')"
else
  _C_RESET="" _C_INFO="" _C_OK="" _C_WARN="" _C_ERR=""
fi

info()    { printf '%s[info]%s %s\n' "$_C_INFO" "$_C_RESET" "$*"; }
success() { printf '%s[ok]%s %s\n'   "$_C_OK"   "$_C_RESET" "$*"; }
warn()    { printf '%s[warn]%s %s\n' "$_C_WARN" "$_C_RESET" "$*" >&2; }
die()     { printf '%s[err]%s %s\n'  "$_C_ERR"  "$_C_RESET" "$*" >&2; exit 1; }

```
