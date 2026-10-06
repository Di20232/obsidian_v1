---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/validate-ai-first.hook.yaml
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# hooks/validate-ai-first.hook.yaml

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/validate-ai-first.hook.yaml). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```yaml
name: validate-ai-first
description: >
  PostToolUse hook on Write/Edit and create_file. Warns when a markdown file
  inside OBSIDIAN_VAULT_PATH fails the AI-first vault rule (missing required
  frontmatter fields, missing 'For future agent' preamble, broken YAML).
  Non-blocking: the file write still succeeds; warning is returned as hook
  JSON (systemMessage / additionalContext) so the host can surface it.
script: validate-ai-first.sh
triggers:
  - event: after-tool-use
    match-tool: [write, edit, create_file]
exclude: []

```
