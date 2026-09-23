---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/obsidian-bg-agent.hook.yaml
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# hooks/obsidian-bg-agent.hook.yaml

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/obsidian-bg-agent.hook.yaml). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```yaml
name: obsidian-bg-agent
description: >
  PostCompact hook (OPT-IN, DISABLED BY DEFAULT). After Claude compacts the
  conversation context, spawns a headless Claude subprocess that propagates
  vault-worthy items from the compaction summary into the vault. TRUST-GATED:
  it writes UNATTENDED with --dangerously-skip-permissions, so it ships inert.
  It requires BOTH OBSIDIAN_VAULT_PATH and OBSIDIAN_BG_AGENT_ENABLED=1, plus a
  PostCompact registration in ~/.claude/settings.json (see
  hooks/postcompact.hook.example.json), before it does anything. setup.sh sets
  OBSIDIAN_VAULT_PATH but never the enable flag, so a normal install leaves it
  inert. Add/update only - it never deletes, moves, or archives notes.
script: obsidian-bg-agent.sh
enabled: false
triggers:
  - event: post-compact
exclude: []

```
