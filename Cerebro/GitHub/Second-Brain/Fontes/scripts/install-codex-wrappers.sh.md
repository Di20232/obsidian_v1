---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/install-codex-wrappers.sh
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/install-codex-wrappers.sh

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/install-codex-wrappers.sh). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```bash
#!/usr/bin/env bash
set -euo pipefail

# Install one PATH shim per command so Codex users can run them by name:
#   obsidian-init
#   obsidian-daily
#   research "topic"
# Each shim delegates to scripts/run-command.sh. (Claude Code users do not need
# this - they use the slash commands directly.)

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BIN_DIR="${OBSIDIAN_CODEX_BIN_DIR:-$HOME/.codex/bin}"
mkdir -p "$BIN_DIR"

count=0
for file in "$SKILL_DIR/commands/"*.md; do
  name="$(basename "$file" .md)"
  wrapper="$BIN_DIR/$name"
  cat > "$wrapper" <<EOF
#!/usr/bin/env bash
exec "$SKILL_DIR/scripts/run-command.sh" "$name" "\$@"
EOF
  chmod +x "$wrapper"
  count=$((count + 1))
done

echo "Installed $count command wrappers to $BIN_DIR"
echo "If $BIN_DIR is not on your PATH, add:"
echo "  export PATH=\"$BIN_DIR:\$PATH\""

```
