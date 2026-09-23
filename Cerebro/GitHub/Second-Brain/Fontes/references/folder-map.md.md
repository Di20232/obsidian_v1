---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/folder-map.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# references/folder-map.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/folder-map.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

# Folder Map Resolution

How every command decides **which folder** a note belongs in. Never hardcode a folder name in a command body - resolve it through this spec so the same command works on a wiki-style vault, an Obsidian-style vault, or any custom layout.

## The rule

1. **Read the vault's `_CLAUDE.md` first.** If it has a `## Folder Map` (or `## Naming Conventions`) table, that table is authoritative - use the folder it names for the note type, even if it differs from the defaults below.
2. **If `_CLAUDE.md` is absent or silent on a type,** fall back to the wiki-style default (column 2). If the vault clearly uses Obsidian-style folders (they exist on disk), use column 3 instead.
3. **If neither folder exists yet,** create the wiki-style one, unless `_CLAUDE.md` says the vault is Obsidian-style.
4. **Never invent a third name.** If you cannot resolve a folder, ask the user rather than guessing a new one.

## Note-type to folder

| Note type | Wiki-style default | Obsidian-style alias |
|-----------|--------------------|----------------------|
| Person / company / tool (entity) | `wiki/entities/` | `People/` |
| Idea / concept / framework / synthesis | `wiki/concepts/` | `Ideas/` (ideas), `Knowledge/` (reference) |
| Project | `wiki/projects/` | `Projects/` |
| Daily note | `wiki/daily/` | `Daily/` |
| Dev / work log | `wiki/logs/` | `Dev Logs/` |
| Weekly / monthly review | `wiki/reviews/` | `Reviews/` |
| Standalone task | `wiki/tasks/` | `Tasks/` |
| Decision record (ADR) | `wiki/decisions/` | `Knowledge/` (as `ADR-YYYY-MM-DD - Title.md`) |
| Meeting note | `wiki/meetings/` | `Meetings/` |
| Raw source (immutable) | `raw/` (articles, transcripts, pdfs, videos subfolders) | `raw/` |
| Research output | `Research/` (Web, Deep, X-pulse, X-reads, YouTube, NotebookLM subfolders) | `Research/` |
| Kanban board | `boards/` | `Boards/` |
| Agenda snapshot | `wiki/agenda/` | `Agenda/` |
| Recurring obligation (recurring-task) | `wiki/tasks/` | `Tasks/` |

## Notes

- **Ideas vs concepts:** in a wiki-style vault there is no separate `Ideas/` folder - ideas, concepts, frameworks, and synthesis notes all live in `wiki/concepts/`. Only use `Ideas/` if the vault actually has that folder (Obsidian-style). A note tagged `#idea` is found by tag/status, not by folder.
- **ADRs:** wiki-style keeps decision records in `wiki/decisions/`; Obsidian-style keeps them in `Knowledge/` with an `ADR-` filename prefix. Resolve per `_CLAUDE.md`.
- **Searching across types:** when a command greps "everywhere" (e.g. synthesis, find), enumerate whatever top-level note folders actually exist in the vault rather than a fixed list - read the vault root once and match the folders present.
