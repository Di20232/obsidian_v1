---
tags: [ambiente, windows, ferramentas]
cssclasses: [cerebro-nota, cerebro-ambiente]
---

# Máquina Windows — o que está instalado e o que morde

Registro do ambiente em que os projetos deste cofre rodam.

## Ferramentas confirmadas

| Ferramenta | Observação |
|---|---|
| **Python** | Invocado por `py` (o launcher do Windows), não por `python` |
| **Node.js** | v22 |
| **Docker Desktop** | Precisa estar **aberto** — fechá-lo derruba os containers |
| **Git + Git Bash** | Com Git Credential Manager |
| **GitHub CLI** (`gh`) | Autenticado |
| **PostgreSQL nativo** | Instalado no Windows, ocupando a 5432 |
| **Claude CLI** | Instalado |

## As armadilhas específicas do Windows

**1. `py` em vez de `python`.** O alias `python` pode cair no atalho da Microsoft Store e falhar com uma mensagem confusa sobre instalar da loja. Use `py`:

```bash
py -m reflex run
```

**2. Git Bash converte caminhos.** Um caminho `/tmp/x.py` destinado a um container Linux vira `C:/Program Files/Git/tmp/x.py`. Prefixe com `MSYS_NO_PATHCONV=1`. → [[../Problemas-Resolvidos/23-Docker-Exec-no-Git-Bash-do-Windows|caso real]]

**3. Terminal abrindo em System32.** Alguns atalhos abrem com `C:\Windows\System32` como diretório atual. Comandos relativos criam arquivos ali — e no caso do Docker Compose, containers inteiros. → [[../Problemas-Resolvidos/17-Containers-Orfaos-em-System32|caso real]]

**4. Serviços nativos disputam portas com containers.** O PostgreSQL do Windows na 5432 fez o app conectar no banco errado **sem dar erro**. → [[../Problemas-Resolvidos/16-PostgreSQL-Nativo-Ocupa-a-Porta-5432|caso real]]

**5. Processos órfãos seguram portas.** Servidor de desenvolvimento que sobrevive ao comando de parada. → [[../Problemas-Resolvidos/18-Porta-3000-Presa-por-Processo-Orfao|caso real]]

## Comandos PowerShell que resolvem a maioria dos casos

Quem está numa porta:

```powershell
Get-NetTCPConnection -LocalPort 3000 -State Listen | Select-Object OwningProcess
```

Qual é o comando desse processo (**sempre antes de encerrar**):

```powershell
Get-CimInstance Win32_Process -Filter "ProcessId = 11240" | Select-Object CommandLine
```

Encerrar, depois de confirmar:

```powershell
Stop-Process -Id 11240 -Force
```

## Links relacionados

- Ambiente: [[02-Portas-e-Conflitos|Portas e conflitos]] · [[03-Contas-Git|Contas Git]]
- Tecnologia: [[../Tecnologias/04-Docker|Docker]]
