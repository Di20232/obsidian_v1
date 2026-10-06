---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/recall.hook.example.json
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# hooks/recall.hook.example.json

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/recall.hook.example.json). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```json
// recall.hook.example.json - paste-in template for ~/.claude/settings.json
//
// OPT-IN / DISABLED BY DEFAULT. Bounded vault recall: on every prompt, inject
// a small brief (max 4 notes, ~900 chars) of the most relevant vault notes -
// or nothing at all when confidence is low (abstention). Read-only; it never
// writes to the vault. It does nothing until BOTH env vars are set AND the
// UserPromptSubmit hook is registered:
//      "env": {
//        "OBSIDIAN_VAULT_PATH": "/path/to/your/vault",
//        "OBSIDIAN_RECALL_ENABLED": "1"
//      }
//
// Every inject/abstain decision is logged to <vault>/.claude-runs/
// recall-YYYY-MM-DD.jsonl so you can audit what got recalled and why.
//
// To DISABLE again: set OBSIDIAN_RECALL_ENABLED to "0" (or remove it). The
// hard gate in the script makes clearing the flag enough, even if the hook
// stays registered.
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /absolute/path/to/.claude/skills/obsidian-second-brain/hooks/obsidian-recall.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}

```
