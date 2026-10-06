---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/platform-home.sh
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/platform-home.sh

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/platform-home.sh). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```bash
#!/bin/bash
# Shared home resolution for the bash half of the toolkit. `source` this file,
# then call osb_platform_home: it sets OSB_WIN (1 on a Windows shell: Git Bash,
# MSYS2, Cygwin; 0 elsewhere) and OSB_HOME.
#
# Home for config and Claude Code state. On Windows shells that is USERPROFILE,
# which is what Python's Path.home() and Claude Code resolve ~ to there; HOME can
# point at another drive (a corporate roaming home) and would split the config
# between the bash and Python halves (#242). Elsewhere HOME is the home.
#
# Sourced by install.sh, update.sh, scripts/setup.sh, scripts/run-command.sh and
# integrations/telegram-journal/setup.sh. Two files carry an inline copy of the
# case block on purpose, because they must stay standalone: hooks/validate-ai-first.sh
# (copied into other harnesses' hook systems by hand) and scripts/quick-install.sh
# (curl | bash, before any checkout exists). tests/test_platform_home.py fails
# when one of the three copies drifts. Uses bash 3.2 features only (macOS ships 3.2).
osb_platform_home() {
  case "$(uname -s 2>/dev/null)" in
    MINGW*|MSYS*|CYGWIN*)
      OSB_WIN=1
      OSB_HOME="${USERPROFILE:-$HOME}"
      OSB_HOME="$(cygpath -u "$OSB_HOME" 2>/dev/null || printf '%s' "${OSB_HOME//\\//}")" ;;
    *) OSB_WIN=0; OSB_HOME="$HOME" ;;
  esac
}

```
