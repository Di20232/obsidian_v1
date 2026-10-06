---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.gitignore
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# .gitignore

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.gitignore). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```text
# Python / uv
.venv/
__pycache__/
*.pyc
*.pyo
.python-version

# Local config (never commit)
.env
*.local
.claude/

# macOS
.DS_Store

# IDE
.vscode/
.idea/

# Logs
*.log

# Build output (regenerate with `bash scripts/build.sh`)
dist/

# Node / npm scratch. The rule is repo-wide because stray package.json files
# used to appear from tooling experiments and none of them belonged here.
node_modules/
.next/
package.json
package-lock.json
yarn.lock
pnpm-lock.yaml

# ...except the Obsidian plugin, which is a real npm package and cannot build
# from a checkout without its manifest and lockfile. The blanket rule above
# silently excluded both, so CI would have run `npm ci` against nothing.
!integrations/obsidian-plugin/package.json
!integrations/obsidian-plugin/package-lock.json

# Per-vault retrieval eval cases (contain private note paths; generate locally)
scripts/eval/retrieval_cases*.jsonl
scripts/eval/behavior_cases.jsonl

```
