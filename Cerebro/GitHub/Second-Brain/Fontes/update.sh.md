---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/update.sh
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# update.sh

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/update.sh). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```bash
#!/bin/bash

set -e

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Home for config and Claude Code state (OSB_HOME, OSB_WIN): USERPROFILE on
# Windows shells, HOME elsewhere. See scripts/platform-home.sh.
. "$SKILL_DIR/scripts/platform-home.sh"
osb_platform_home
COMMANDS_DIR="$OSB_HOME/.claude/commands"

# Pull latest
if [ -d "$SKILL_DIR/.git" ]; then
  echo "Pulling latest changes..."
  git -C "$SKILL_DIR" pull
else
  echo "Not a git repo - skipping pull. Update the files in $SKILL_DIR manually."
fi

# Symlinked commands pick up git pull automatically.
# Copied commands (Windows without Developer Mode) need an explicit refresh.
echo "Updating slash commands..."
updated=0
for file in "$SKILL_DIR/commands/"*.md; do
  name=$(basename "$file")
  dest="$COMMANDS_DIR/$name"
  if [ -L "$dest" ]; then
    : # symlink - already current after git pull
  else
    cp "$file" "$dest"
    echo "  updated $name"
    updated=$((updated + 1))
  fi
done
[ "$updated" -gt 0 ] && echo "  $updated command(s) refreshed (copied, not symlinked)"

echo ""
echo "Done. Restart Claude Code to pick up the changes."

```
