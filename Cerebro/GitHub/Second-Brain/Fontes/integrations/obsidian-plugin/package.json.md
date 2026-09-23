---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/integrations/obsidian-plugin/package.json
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# integrations/obsidian-plugin/package.json

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/integrations/obsidian-plugin/package.json). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```json
{
  "name": "ai-first-lint",
  "version": "0.1.0",
  "description": "Check an Obsidian vault against the AI-First note spec.",
  "private": true,
  "type": "module",
  "scripts": {
    "build": "tsc --noEmit && node esbuild.config.mjs production",
    "dev": "node esbuild.config.mjs",
    "typecheck": "tsc --noEmit",
    "test": "node --test test/",
    "pretest": "esbuild src/lint.ts --bundle --format=esm --outfile=test/.lint.mjs --log-level=warning"
  },
  "devDependencies": {
    "@types/node": "^20.11.0",
    "esbuild": "^0.21.0",
    "obsidian": "^1.5.7",
    "typescript": "^5.4.0"
  }
}

```
