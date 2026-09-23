---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-capture.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# commands/obsidian-capture.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-capture.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.


Use the obsidian-second-brain skill. Execute `/obsidian-capture $ARGUMENTS`:

The optional argument is the idea text. If not provided, pull the most recent idea or thought from the conversation.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Take the argument as the idea, or pull from recent conversation context
3. Resolve the idea folder per `references/folder-map.md` (read the vault's `_CLAUDE.md` Folder Map first; wiki-style ideas live in `wiki/concepts/`, Obsidian-style in `Ideas/`). Search it for a related existing note - if found, append to it
4. If new: create `<idea-folder>/Title.md` with the capture schema (`type: idea`, `date`, `tags: [idea]`, `ai-first: true`, `status: captured`, one-line body) - the documented capture exception in `references/ai-first-rules.md`: enrichment happens at graduation
5. Write the idea with any supporting context from the conversation
6. Add a brief mention in today's daily note under an Ideas or Captures section

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future agent` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory `<code>[[wikilinks]]</code>` for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. If that path does not resolve from your working directory, search upward for it; if you still cannot read it, say so before writing rather than producing a note that silently skips the rule. The vault is for future agent retrieval - not human reading. (The capture exception applies: minimal schema at capture, full enrichment at graduation.)

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.

## Metadados originais

```yaml
---
description: Quick idea capture - zero friction, saves to your ideas folder and mentions in daily note
category: vault
trigger-mode: proactive
triggers_en: ["capture this idea", "save this idea", "quick note", "drop a thought"]
triggers_es: ["captura esta idea", "guarda esta idea", "nota rápida", "apunta esto"]
triggers_pt: ["capture esta ideia", "salve esta ideia", "anotação rápida", "registre um pensamento"]
triggers_zh: ["记下这个想法", "帮我快速记一笔", "先把这个灵感存下来", "随手记一下"]
---

```
