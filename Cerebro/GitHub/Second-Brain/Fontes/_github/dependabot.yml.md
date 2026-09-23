---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.github/dependabot.yml
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# .github/dependabot.yml

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.github/dependabot.yml). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```yaml
# Dependabot keeps dependencies current automatically so the supply chain stays
# patched without manual checking. https://docs.github.com/code-security/dependabot
# Monthly + grouped: at most one PR per ecosystem per month, all bumps batched.
version: 2
updates:
  # Keep GitHub Actions (in .github/workflows) up to date.
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
    commit-message:
      prefix: "ci"
    groups:
      github-actions:
        patterns: ["*"]

  # Keep Python dependencies (pyproject.toml) up to date.
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "monthly"
    commit-message:
      prefix: "deps"
    groups:
      python:
        patterns: ["*"]

```
