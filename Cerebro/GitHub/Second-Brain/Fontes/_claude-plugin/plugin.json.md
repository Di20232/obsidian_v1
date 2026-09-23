---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.claude-plugin/plugin.json
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# .claude-plugin/plugin.json

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.claude-plugin/plugin.json). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```json
{
  "name": "obsidian-second-brain",
  "description": "Stop re-explaining your notes to Claude. Turns your Obsidian vault into memory Claude can actually search, and keeps it true: new sources rewrite existing pages, contradictions reconcile, and stale facts get flagged. AI note-taking and PKM for Claude Code.",
  "version": "0.16.0",
  "author": {
    "name": "Eugeniu Ghelbur",
    "email": "e.ghelbur@gmail.com"
  },
  "homepage": "https://github.com/eugeniughelbur/obsidian-second-brain",
  "license": "MIT",
  "commands": "./commands/",
  "mcpServers": {
    "vault": {
      "command": "uv",
      "args": [
        "run",
        "--no-project",
        "--with",
        "mcp<2",
        "python",
        "${CLAUDE_PLUGIN_ROOT}/integrations/obsidian-mcp-server/server.py"
      ]
    }
  }
}

```
