---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/_config.yml
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# _config.yml

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/_config.yml). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```yaml
title: obsidian-second-brain
description: >-
  A 45-command cross-CLI skill that turns any Obsidian vault into a living
  AI-first second brain. Runs in Claude Code, OpenAI Codex CLI, Google Gemini
  CLI, OpenCode, Google Antigravity, Nous Research Hermes, and Pi from one
  platform-neutral source. Vault management, thinking tools, scheduled agents,
  key-less web research, Google Calendar commands, and /obsidian-architect -
  which scans a codebase and writes maintained architecture notes into your
  vault. Plus a write-time AI-first validator hook and an interview-driven
  /create-command flow.
theme: jekyll-theme-cayman
plugins:
  - jekyll-seo-tag
  - jekyll-sitemap

# SEO
url: https://eugeniughelbur.github.io
baseurl: /obsidian-second-brain
twitter:
  username: eugeniughelbur
  card: summary_large_image
social:
  name: Eugeniu Ghelbur
  links:
    - https://github.com/eugeniughelbur
    - https://www.linkedin.com/in/eugeniu-ghelbur/

# Don't ship internal docs as pages
exclude:
  - .venv
  - __pycache__
  - scripts
  - .env*
  - install.sh
  - pyproject.toml
  - uv.lock
  - .gitignore
  - CITATION.cff
  - SKILL.md
  - architecture.md
  - hooks
  - commands
  - references

```
