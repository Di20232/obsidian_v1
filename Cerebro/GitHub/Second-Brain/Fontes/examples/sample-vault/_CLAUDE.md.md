---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/examples/sample-vault/_CLAUDE.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# examples/sample-vault/_CLAUDE.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/examples/sample-vault/_CLAUDE.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

# _CLAUDE.md

Operating manual for this vault. Loaded by Claude Code on every session that touches it.

This is a sample vault belonging to the fictional **Alex Rivera**. The structure shown here is what `/obsidian-init` produces, lightly edited to feel lived-in. Treat every name, project, and URL inside as fictional.

## Section 0 - AI-first rule (non-negotiable)

This vault is for **future agent**, not human reading. Every note Claude writes or updates must follow [`references/ai-first-rules.md`](https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/references/ai-first-rules.md):

1. Self-contained context (no "see above")
2. `## For future agent` preamble after frontmatter
3. Rich frontmatter with `type`, `date`, `tags`, `ai-first: true`
4. Recency markers per external claim
5. Source URLs preserved verbatim
6. `<code>[[wikilinks]]</code>` for every person, project, idea, decision
7. Confidence levels (`stated | high | medium | speculation`) where applicable

If a note Claude is about to write would not pass this rule, fix the note before saving. No exceptions for "small" or "quick" entries.

## Section 1 - Identity

- **Owner:** Alex Rivera, indie hacker building <code>[[Projects/Tide]]</code>
- **Location:** Lisbon, Portugal
- **Working hours:** roughly 09:00 to 18:00 WET, hard stop on weekends
- **Time zone:** Europe/Lisbon

## Section 2 - Folder structure

- `Daily/` - one file per day, `YYYY-MM-DD.md`
- `Projects/` - one file per active project, status-tagged
- `people/` - one file per person worth remembering
- `Ideas/` - fragment captures, dated filenames
- `Decisions/` - standalone decision records (most decisions live inside project notes)
- `Knowledge/` - synthesis, ADRs, learning notes
- `Research/` - outputs from `/research`, `/research-deep`, `/x-read`, `/x-pulse`, `/youtube`
- `wiki/logs/` - dev logs and session logs
- `social-media/` - content pipeline (ideas, swipe file, data points)
- `Boards/` - kanban boards for tasks per project
- `Archive/` - archived notes, never deleted

## Section 3 - Active projects (as of 2026-04-27)

- <code>[[Projects/Tide]]</code> - habit-tracking SaaS, status: active, retention rebuild in progress

## Section 4 - Key relationships

- <code>[[people/Alex Rivera]]</code> - vault owner
- <code>[[people/Sam Patel]]</code> - co-founder of Tide, technical lead

## Section 5 - Defaults Claude should follow

- Always search before creating a new note (duplicates are vault rot)
- Always update boards and the daily note when adding a task
- Never create an orphaned note (every note links to at least one other)
- Confidence levels are mandatory for any external claim
- When in doubt about a fact, mark it `TBD` rather than guessing
