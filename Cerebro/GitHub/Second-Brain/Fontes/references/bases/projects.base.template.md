---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/bases/projects.base.template
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# references/bases/projects.base.template

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/bases/projects.base.template). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```text
filters:
  and:
    - file.inFolder("{{PROJECTS_FOLDER}}")
    - file.ext == "md"
    - note.type == "project"
formulas:
  status_icon: if(status == "active", "🟢", if(status == "blocked", "🔴", if(status == "stalled", "🟡", if(status == "idle", "💤", if(status == "planning", "⚪", if(status == "on-hold", "⏸️", if(status == "completed", "✅", if(status == "archived", "📦", "❔"))))))))
  days_since_update: if(updated, (today() - date(updated)).days, "")
properties:
  formula.status_icon:
    displayName: " "
  formula.days_since_update:
    displayName: Stale (days)
  status:
    displayName: Status
  tags:
    displayName: Tags
  repo:
    displayName: Repo
views:
  - type: table
    name: Active
    filters:
      and:
        - status == "active"
    order:
      - formula.status_icon
      - file.basename
      - tags
      - updated
    columnSize:
      formula.status_icon: 40
      file.basename: 183
  - type: table
    name: Stalled
    filters:
      and:
        - status == "stalled"
    order:
      - file.basename
      - tags
      - updated
      - formula.days_since_update
  - type: table
    name: Planning
    filters:
      and:
        - status == "planning"
    order:
      - file.basename
      - tags
      - created
      - repo
  - type: table
    name: On Hold
    filters:
      or:
        - status == "on-hold"
    order:
      - file.basename
      - tags
      - updated
      - formula.days_since_update
  - type: table
    name: Archived
    filters:
      and:
        - status == "archived"
    order:
      - file.basename
      - tags
      - updated
  - type: table
    name: All
    groupBy:
      property: status
      direction: ASC
    order:
      - formula.status_icon
      - file.basename
      - status
      - tags
      - updated
      - formula.days_since_update
    columnSize:
      formula.status_icon: 70
      file.basename: 165

```
