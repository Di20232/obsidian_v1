---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.github/ISSUE_TEMPLATE/bug_report.yml
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# .github/ISSUE_TEMPLATE/bug_report.yml

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.github/ISSUE_TEMPLATE/bug_report.yml). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```yaml
name: 🐛 Bug report
description: Something is broken or behaves wrong
title: "[Bug] "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to file a bug. Before you continue, please:
        - Check the [FAQ](https://github.com/eugeniughelbur/obsidian-second-brain#faq) - many issues are answered there.
        - Search [open + closed issues](https://github.com/eugeniughelbur/obsidian-second-brain/issues?q=is%3Aissue) - someone may have hit the same bug.

  - type: dropdown
    id: command
    attributes:
      label: Which command broke?
      description: If multiple, file separate issues.
      options:
        - "/obsidian-save"
        - "/obsidian-daily"
        - "/obsidian-log"
        - "/obsidian-task"
        - "/obsidian-person"
        - "/obsidian-decide"
        - "/obsidian-capture"
        - "/obsidian-find"
        - "/obsidian-recap"
        - "/obsidian-review"
        - "/obsidian-board"
        - "/obsidian-project"
        - "/obsidian-health"
        - "/obsidian-init"
        - "/obsidian-ingest"
        - "/obsidian-synthesize"
        - "/obsidian-reconcile"
        - "/obsidian-export"
        - "/obsidian-adr"
        - "/obsidian-visualize"
        - "/obsidian-learn"
        - "/obsidian-challenge"
        - "/obsidian-emerge"
        - "/obsidian-connect"
        - "/obsidian-graduate"
        - "/obsidian-world"
        - "/x-read"
        - "/x-pulse"
        - "/research"
        - "/research-deep"
        - "/youtube"
        - Background agent (PostCompact hook)
        - Scheduled agent (morning / nightly / weekly / health)
        - install.sh
        - Other / not sure
    validations:
      required: true

  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: What did you run, and what went wrong?
      placeholder: |
        I ran `/research-deep "AI memory tools"`. The script said Phase 4 failed with:
        "Perplexity API error 400: model not found"
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: What did you expect to happen?
      placeholder: A research note saved to Research/Deep/ and Obsidian opening at the new note.
    validations:
      required: true

  - type: textarea
    id: reproduce
    attributes:
      label: Steps to reproduce
      description: Exact commands and inputs. The more specific, the faster the fix.
      placeholder: |
        1. Pull latest main (commit hash)
        2. Run `uv sync`
        3. Run `/research-deep "topic name"`
        4. See error
    validations:
      required: true

  - type: input
    id: version
    attributes:
      label: Skill version (release tag or commit SHA)
      placeholder: "v0.10.0 or 3d748cf"
    validations:
      required: true

  - type: dropdown
    id: os
    attributes:
      label: Operating system
      options:
        - macOS
        - Linux
        - Windows
        - Other
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Relevant logs / error output
      description: Paste error messages, stack traces, or `~/.research-toolkit/usage.log` entries if relevant.
      render: shell

  - type: checkboxes
    id: confirm
    attributes:
      label: Confirmation
      options:
        - label: I checked the FAQ in the README
          required: true
        - label: I searched existing issues
          required: true
        - label: I'm running the latest release or main branch
          required: true

```
