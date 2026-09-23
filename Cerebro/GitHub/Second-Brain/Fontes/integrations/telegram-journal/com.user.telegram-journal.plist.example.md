---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/integrations/telegram-journal/com.user.telegram-journal.plist.example
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# integrations/telegram-journal/com.user.telegram-journal.plist.example

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/integrations/telegram-journal/com.user.telegram-journal.plist.example). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<!--
  macOS launchd template. To use it:
    1. Replace HOME_DIR with your home path (e.g. /Users/you).
    2. Replace UV_PATH with the output of `which uv` (e.g. /opt/homebrew/bin/uv).
    3. Replace SCRIPT_PATH with the absolute path to telegram_journal.py.
    4. Copy to ~/Library/LaunchAgents/com.user.telegram-journal.plist
    5. Load it:  launchctl load -w ~/Library/LaunchAgents/com.user.telegram-journal.plist
  On Linux, run the script from cron every minute instead:
    * * * * * UV_PATH run SCRIPT_PATH >> HOME_DIR/telegram-journal.log 2>&1
-->
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.telegram-journal</string>

    <key>ProgramArguments</key>
    <array>
        <string>UV_PATH</string>
        <string>run</string>
        <string>SCRIPT_PATH</string>
    </array>

    <!-- Poll the bot every 60 seconds. -->
    <key>StartInterval</key>
    <integer>60</integer>

    <key>RunAtLoad</key>
    <true/>

    <key>StandardOutPath</key>
    <string>HOME_DIR/Library/Logs/telegram-journal.out.log</string>

    <key>StandardErrorPath</key>
    <string>HOME_DIR/Library/Logs/telegram-journal.err.log</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
    </dict>
</dict>
</plist>

```
