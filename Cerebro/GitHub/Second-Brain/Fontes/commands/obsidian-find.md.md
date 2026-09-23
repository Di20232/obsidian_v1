---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-find.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# commands/obsidian-find.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-find.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.


Use the obsidian-second-brain skill. Execute `/obsidian-find $ARGUMENTS`:

The argument is the search query.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Search the vault for the query using the ranked keyword search where it is available: the `obsidian_search` MCP tool, or `vault_ops.search` directly (`integrations/obsidian-mcp-server/`). It applies stopword filtering and length-normalized ranking, so a short note with the term in its title outranks a long note that merely repeats it. In Claude Code (where no search tool is bound), grep the vault and read the top matches directly, applying the same judgement: ignore filler words, and do not let long `raw/` transcripts or `log.md` outrank a canonical `wiki/` note.
3. Also try variations if results are sparse (synonyms, related terms)
4. Return results with context: note title, folder, a relevant excerpt, and what type of note it is
5. If results are ambiguous, group them by type (people, projects, tasks, etc.)
6. Offer to open, update, or link any of the found notes

Do not just return filenames - return enough context for the user to act on the results.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future agent` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory `<code>[[wikilinks]]</code>` for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. If that path does not resolve from your working directory, search upward for it; if you still cannot read it, say so before writing rather than producing a note that silently skips the rule. The vault is for future agent retrieval - not human reading.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.

## Metadados originais

```yaml
---
description: Smart vault search - returns results with context, not just filenames
category: vault
triggers_en: ["find in vault", "search my notes", "where is", "what did I write about"]
triggers_es: ["busca en el vault", "busca en mis notas", "dónde está", "qué escribí sobre", "tengo algo sobre"]
triggers_pt: ["encontre no vault", "pesquise minhas notas", "onde está", "o que eu escrevi sobre"]
triggers_zh: ["在知识库里找一下", "搜索我的笔记", "我之前在哪篇笔记里写过", "我写过关于这个吗"]
---

```
