---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/bases/tasks.base.template
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# references/bases/tasks.base.template

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/bases/tasks.base.template). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```text
filters:
  and:
    - file.inFolder("{{TASKS_FOLDER}}")
    - file.ext == "md"
    - note.type == "task"
formulas:
  days_until_due: if(due, (date(due) - today()).days, "")
  overdue: if(due, (today() - date(due)).days > 0, false)
properties:
  formula.days_until_due:
    displayName: Due in (days)
  formula.overdue:
    displayName: Overdue
  status:
    displayName: Status
  priority:
    displayName: Priority
  due:
    displayName: Due
  project:
    displayName: Project
  tags:
    displayName: Tags
views:
  - type: table
    name: Open
    filters:
      and:
        - status != "done"
        - status != "cancelled"
    order:
      - formula.overdue
      - due
      - priority
      - file.basename
      - project
    columnSize:
      file.basename: 200
      project: 150
  - type: table
    name: Done
    filters:
      and:
        - status == "done"
    order:
      - updated
      - file.basename
  - type: table
    name: All
    groupBy:
      property: status
      direction: ASC
    order:
      - priority
      - due
      - file.basename
      - project
      - tags
    columnSize:
      file.basename: 200
      project: 150

```
