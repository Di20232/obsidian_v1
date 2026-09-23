---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-log.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# commands/obsidian-log.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-log.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.


Use the obsidian-second-brain skill. Execute `/obsidian-log`:

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Infer the project from conversation context - search the vault if needed to find the right project note
3. Read `Templates/Dev Log.md` (or `Templates/Work Log.md`) if either exists; if neither does, write the sections directly: Context, What changed, Decisions, Next steps
4. Fill in: date, project, what was worked on, problems encountered, decisions made, next steps - all inferred from the conversation
5. Save to the dev-log folder resolved per `references/folder-map.md` (read the vault's `_CLAUDE.md` Folder Map first; wiki-style `wiki/logs/`, Obsidian-style `Dev Logs/`), named `YYYY-MM-DD - Project Name.md`
6. Inject a link into the project note's Recent Activity section
7. Inject a link into today's daily note Work section

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future agent` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory `<code>[[wikilinks]]</code>` for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. If that path does not resolve from your working directory, search upward for it; if you still cannot read it, say so before writing rather than producing a note that silently skips the rule. The vault is for future agent retrieval - not human reading.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.

## Metadados originais

```yaml
---
description: Log this work or dev session to the vault - infers project from context
category: vault
trigger-mode: proactive
triggers_en: ["log this work", "log this session", "log this dev session", "obsidian log"]
triggers_es: ["registra este trabajo", "registra esta sesión", "registra esta sesión de desarrollo", "obsidian log"]
triggers_pt: ["registre este trabalho", "registre esta sessão", "registre esta sessão de desenvolvimento", "obsidian log"]
triggers_zh: ["记录这次工作", "把这次开发过程写进知识库", "记录当前工作会话", "保存这次开发日志"]
---

```
