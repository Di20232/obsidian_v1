---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/postcompact.hook.example.json
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# hooks/postcompact.hook.example.json

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/postcompact.hook.example.json). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```json
// postcompact.hook.example.json - paste-in template for ~/.claude/settings.json
//
// OPT-IN / DISABLED BY DEFAULT. The background agent writes to your vault
// UNATTENDED with --dangerously-skip-permissions, so it ships inert. It does
// nothing until BOTH env vars below are set AND the PostCompact hook is
// registered. Read the trust caveat at the top of hooks/obsidian-bg-agent.sh
// before enabling.
//
// If you ran scripts/setup.sh: it already registered the PostCompact hook and
// set OBSIDIAN_VAULT_PATH. To turn the agent ON, add the second flag to the
// "env" section of ~/.claude/settings.json (this is the only step that arms it):
//      "env": {
//        "OBSIDIAN_VAULT_PATH": "/path/to/your/vault",
//        "OBSIDIAN_BG_AGENT_ENABLED": "1"
//      }
//
// If you are wiring it by hand (no setup.sh):
//   1. Make the script executable (one-time):
//        chmod +x ~/.claude/skills/obsidian-second-brain/hooks/obsidian-bg-agent.sh
//   2. Add BOTH env vars above to the "env" section.
//   3. Merge the "hooks" block below into ~/.claude/settings.json (real JSON -
//      strip these comments), using the absolute path to your installed script.
//
// To DISABLE again: set OBSIDIAN_BG_AGENT_ENABLED to "0" (or remove it). The
// hard gate in the script makes clearing the flag enough to render it inert,
// even if the PostCompact hook stays registered.
{
  "hooks": {
    "PostCompact": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "/absolute/path/to/.claude/skills/obsidian-second-brain/hooks/obsidian-bg-agent.sh",
            "timeout": 10,
            "async": true
          }
        ]
      }
    ]
  }
}

```
