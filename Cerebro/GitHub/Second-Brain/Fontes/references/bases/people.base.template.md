---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/bases/people.base.template
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# references/bases/people.base.template

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/bases/people.base.template). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```text
filters:
  and:
    - file.inFolder("{{PEOPLE_FOLDER}}")
    - file.ext == "md"
    - note.type == "person"
formulas:
  days_since_update: if(updated, (today() - date(updated)).days, "")
properties:
  formula.days_since_update:
    displayName: Stale (days)
  role:
    displayName: Role
  company:
    displayName: Company
  tags:
    displayName: Tags
views:
  - type: table
    name: All
    order:
      - file.basename
      - role
      - company
      - tags
      - updated
      - formula.days_since_update
    columnSize:
      file.basename: 180
      role: 150
      company: 150

```
