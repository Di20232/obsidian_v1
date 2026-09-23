---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.github/workflows/scorecard.yml
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# .github/workflows/scorecard.yml

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/.github/workflows/scorecard.yml). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```yaml
# OpenSSF Scorecard - publishes a public supply-chain security score for this repo.
# Results show on the badge + at https://securityscorecards.dev and feed external
# trust registries. Runs weekly and on push to the default branch.
name: Scorecard supply-chain security

on:
  branch_protection_rule:
  schedule:
    - cron: "20 7 * * 1" # Mondays 07:20 UTC
  push:
    branches: ["main"]

# Read-only by default; the analysis job elevates only what it needs.
permissions: read-all

jobs:
  analysis:
    name: Scorecard analysis
    runs-on: ubuntu-latest
    permissions:
      security-events: write # upload SARIF to the code-scanning dashboard
      id-token: write        # publish results to the OpenSSF API (OIDC)
    steps:
      - name: "Checkout code"
        uses: actions/checkout@v7
        with:
          persist-credentials: false

      - name: "Run analysis"
        uses: ossf/scorecard-action@v2.4.4
        with:
          results_file: results.sarif
          results_format: sarif
          publish_results: true # makes the score publicly checkable

      - name: "Upload artifact"
        uses: actions/upload-artifact@v7
        with:
          name: SARIF file
          path: results.sarif
          retention-days: 5

      - name: "Upload to code-scanning"
        uses: github/codeql-action/upload-sarif@v4.37.9
        with:
          sarif_file: results.sarif

```
