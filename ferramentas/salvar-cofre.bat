@echo off
chcp 65001 >nul
node "%~dp0salvar-cofre.js" %*
pause
