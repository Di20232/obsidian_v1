---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-panel.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# commands/obsidian-panel.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/commands/obsidian-panel.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.


Use the obsidian-second-brain skill. Execute `/obsidian-panel [decision or question]`:

Pressure-tests a decision from several independent angles at once. Where `/obsidian-challenge` red-teams from one adversarial stance, this gathers a panel of distinct lenses and makes each argue on its own before you see a synthesis.

1. Resolve the decision/question from the argument. If none, ask what to put to the panel.
2. Choose the panel:
   - If the vault has an `Advisors/` folder, read those persona notes and use each as a panelist (each verdict reflects that advisor's stated lens and priorities).
   - Otherwise, use 4 generic lenses: the skeptic (what breaks this), the user/customer (who is served or hurt), the operator (can this actually be run/maintained), and the long-game (what does this look like in a year).
3. For EACH panelist, write an independent verdict: their position, the strongest reason behind it, and what would change their mind. Keep them genuinely distinct - do not let them converge prematurely.
4. Write a synthesis: where the panel agreed, where it split, and a recommended decision with its main risk. Do not hide the disagreement - the split is the most useful output.
5. Save to the concepts folder (resolved per `references/folder-map.md` - wiki-style `wiki/concepts/`, Obsidian-style `Ideas/`) as `YYYY-MM-DD - panel - <slug>.md` (`type: synthesis`, tagged `[synthesis, thinking, panel]`), linking any `<code>[[Advisors/...]]</code>` notes and `<code>[[entities/projects]]</code>` the decision touches. Cross-link from today's daily note.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future agent` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory `<code>[[wikilinks]]</code>` for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. If that path does not resolve from your working directory, search upward for it; if you still cannot read it, say so before writing rather than producing a note that silently skips the rule. The vault is for future agent retrieval - not human reading.

**Anti-fabrication:** If you use `Advisors/` notes, base each verdict on what that note actually says - do not invent an advisor's position or attribute views to a real person they have not expressed. Never fabricate a consensus; report the real split. See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.

## Metadados originais

```yaml
---
description: Convene a panel of distinct perspectives on a decision - one independent verdict per lens, then a synthesis. A multi-persona complement to /obsidian-challenge
category: thinking
triggers_en: ["convene a panel", "advisor panel", "get multiple perspectives on", "panel review", "what would the experts say about"]
triggers_es: ["convoca un panel", "panel de asesores", "dame varias perspectivas sobre esto", "revisión en panel", "qué dirían los expertos sobre esto"]
triggers_pt: ["convoque um painel", "painel de especialistas", "obtenha múltiplas perspectivas sobre", "revisão em painel", "o que os especialistas diriam sobre"]
triggers_zh: ["找几个不同视角来评审", "让多个专家分析这个决定", "从几个角度评价这个方案", "开个顾问评审会", "不同专家会怎么看"]
---

```
