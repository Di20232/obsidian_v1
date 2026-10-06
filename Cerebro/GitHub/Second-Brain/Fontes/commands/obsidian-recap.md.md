---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-recap.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# commands/obsidian-recap.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-recap.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.


Use the obsidian-second-brain skill. Execute `/obsidian-recap $ARGUMENTS`:

The argument is the period: `today`, `week`, or `month`. Default to `week` if not specified.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Determine the date range from the argument
3. List all daily notes in the range from the daily folder, resolved per `references/folder-map.md` (wiki-style `wiki/daily/`, Obsidian-style `Daily/`)
4. Spawn parallel subagents - one per daily note - to read and extract key points from each simultaneously
5. Also spawn parallel agents to read dev logs and completed kanban tasks from the same period
6. Synthesize all agent results: what was worked on, decisions made, people interacted with, tasks completed, ideas captured
7. Present as a clean narrative summary - not a raw dump of note content
8. End the recap with a **Suggested questions for future agent** section: 4 to 5 questions this period's vault content is uniquely positioned to answer that the user has not asked yet. Each question must cite at least one specific note (with `<code>[[wikilink]]</code>`) so future agent can resolve it without re-scanning. Prefer questions that:
   - Surface tensions across notes (e.g., "Why does the X decision in <code>[[note A]]</code> contradict the rationale in <code>[[note B]]</code>?")
   - Connect entities that co-appeared but were never explicitly linked
   - Identify unstated next actions implied by the period's work
   Avoid generic prompts ("What did I work on?") - the recap already answers those.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future agent` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory `<code>[[wikilinks]]</code>` for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. If that path does not resolve from your working directory, search upward for it; if you still cannot read it, say so before writing rather than producing a note that silently skips the rule. The vault is for future agent retrieval - not human reading.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.

## Metadados originais

```yaml
---
description: Summarize a time period from the vault - today, week, or month
category: vault
triggers_en: ["recap today", "recap the week", "summarize the week", "month recap"]
triggers_es: ["resumen de hoy", "resumen de la semana", "resume la semana", "resumen del mes"]
triggers_pt: ["recapitule hoje", "recapitule a semana", "resuma a semana", "recap do mês"]
triggers_zh: ["总结今天发生的事", "汇总本周记录", "总结这一周发生了什么", "生成本月摘要"]
---

```
