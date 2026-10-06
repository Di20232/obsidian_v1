---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/hermes-hooks.config.example.yaml
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# hooks/hermes-hooks.config.example.yaml

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/hooks/hermes-hooks.config.example.yaml). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```yaml
# hermes-hooks.config.example.yaml
#
# Paste-in template for the `hooks:` block of your ~/.hermes/config.yaml.
# Registers the vault maintenance hook on the on_session_end lifecycle event -
# the Hermes analog of the Claude PostCompact hook.
#
# OPT-IN / SHIPS INERT. Registering the hook is not enough: the script no-ops
# unless BOTH OBSIDIAN_VAULT_PATH and OBSIDIAN_HERMES_HOOK_ENABLED=1 are in the
# environment (it writes to the vault unattended). See the script header for the
# trust caveat. To disable later, clear OBSIDIAN_HERMES_HOOK_ENABLED.
#
# session lifecycle events take no matcher (matchers apply only to
# pre_tool_call / post_tool_call). The script receives the on_session_end JSON
# payload on stdin and must print JSON on stdout; this one prints `{}`.

hooks:
  on_session_end:
    - command: "~/.hermes/agent-hooks/obsidian-hermes-session-end.sh"
      timeout: 30

```
