---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/run-command.sh
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/run-command.sh

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/run-command.sh). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```bash
#!/usr/bin/env bash
set -euo pipefail

# Run an obsidian-second-brain command on Codex CLI (or any non-slash client).
#
# Codex/Gemini/OpenCode have no native slash-command runtime, so the command
# markdown under commands/ is inert on those platforms. This wraps a command
# file into a prompt and hands it to `codex exec`, so the same commands run
# everywhere. (On Claude Code, just use the slash command directly.)
#
# Usage:
#   run-command.sh /obsidian-init
#   run-command.sh obsidian-daily
#   run-command.sh research "state of MCP servers"
#   run-command.sh --print /obsidian-health      # print the assembled prompt, do not run
#
# Environment:
#   OBSIDIAN_SECOND_BRAIN_HOME   skill root override (default: parent of this script)
#   OBSIDIAN_VAULT_PATH          vault path (default: current directory)
#   CODEX_BIN                    codex binary (default: codex)

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="${OBSIDIAN_SECOND_BRAIN_HOME:-$(cd "$SELF_DIR/.." && pwd)}"
CODEX_BIN="${CODEX_BIN:-codex}"
# Home for config and Claude Code state (OSB_HOME, OSB_WIN): USERPROFILE on
# Windows shells, HOME elsewhere. See platform-home.sh beside this script.
. "$SELF_DIR/platform-home.sh"
osb_platform_home
CONFIG_FILE="$OSB_HOME/.config/obsidian-second-brain/config.env"
[[ -f "$CONFIG_FILE" ]] && source "$CONFIG_FILE"

PRINT_ONLY=0
if [[ "${1:-}" == "--print" ]]; then
  PRINT_ONLY=1
  shift || true
fi

usage() {
  cat >&2 <<EOF
Usage: $(basename "$0") [--print] <command> [args...]
  $(basename "$0") /obsidian-init
  $(basename "$0") research "state of MCP servers"
  OBSIDIAN_VAULT_PATH=~/vault $(basename "$0") /obsidian-health
EOF
}

[[ $# -ge 1 ]] || { usage; exit 2; }

RAW_CMD="$1"; shift || true
ARGS=("$@")

# Normalize: strip a leading / or $ and a trailing .md
CMD="${RAW_CMD#/}"; CMD="${CMD#\$}"; CMD="${CMD%.md}"

COMMAND_FILE="$SKILL_DIR/commands/$CMD.md"
if [[ ! -f "$COMMAND_FILE" ]]; then
  echo "Unknown command: $RAW_CMD (expected $COMMAND_FILE)" >&2
  exit 1
fi

# Resolve the vault. Use bash parameter expansion for the tilde (never `eval`,
# which mis-parses paths containing apostrophes/metacharacters).
VAULT="${OBSIDIAN_VAULT_PATH:-$PWD}"
VAULT="${VAULT/#\~/$HOME}"
if [[ ! -d "$VAULT" ]]; then
  echo "Vault directory not found: $VAULT" >&2
  exit 1
fi

# Assemble the prompt: framing + any args + the command spec verbatim.
ARGS_TEXT="(none)"
[[ ${#ARGS[@]} -gt 0 ]] && ARGS_TEXT="${ARGS[*]}"

PROMPT="$(cat <<EOF
You are executing an installed obsidian-second-brain command in a non-slash client.

Command: /$CMD
Skill root: $SKILL_DIR
Vault root: $VAULT

Rules:
- Treat this exactly as if the user invoked /$CMD in a slash-command client.
- Read AGENTS.md at the vault root first if it exists; otherwise read _CLAUDE.md.
- Follow the command spec below exactly. If it references a skill path under
  ~/.codex/skills or ~/.claude/skills, use $SKILL_DIR instead.

User-supplied arguments: $ARGS_TEXT

Command spec:
$(cat "$COMMAND_FILE")
EOF
)"

if [[ "$PRINT_ONLY" -eq 1 ]]; then
  printf '%s\n' "$PROMPT"
  exit 0
fi

if ! command -v "$CODEX_BIN" >/dev/null 2>&1; then
  echo "codex CLI not found (looked for: $CODEX_BIN). Use --print to see the prompt." >&2
  exit 1
fi

echo "[obsidian-second-brain] Running /$CMD in $VAULT" >&2
exec "$CODEX_BIN" exec --skip-git-repo-check --cd "$VAULT" "$PROMPT"

```
