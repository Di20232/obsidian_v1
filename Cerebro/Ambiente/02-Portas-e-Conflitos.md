---
tags: [ambiente, rede, portas, flashcards]
cssclasses: [cerebro-nota, cerebro-ambiente]
---

# Portas usadas e conflitos conhecidos

Conflito de porta foi a causa mais frequente de problema de ambiente neste cofre. Esta nota é o mapa.

## Mapa de portas

| Porta | Quem usa | Observação |
|---|---|---|
| **3000** | [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] (Reflex) e [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho]] local | ⚠️ Os dois disputam |
| **3100** | Mercadinho em Docker | — |
| **5000** | CTL-TINTA-FL na fase Flask | Histórico |
| **5432** | **PostgreSQL nativo do Windows** | ⚠️ Ocupada por serviço instalado |
| **5433** | PostgreSQL do Mercadinho em Docker | Deslocada de propósito |
| **8501** | [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]] (Streamlit) | — |

## Os três tipos de conflito e como cada um se manifesta

**1. A porta está ocupada e o servidor não sobe.** É o caso mais fácil — a mensagem diz exatamente o que houve. → [[../Problemas-Resolvidos/18-Porta-3000-Presa-por-Processo-Orfao|caso real]]

**2. A porta está ocupada por *outro serviço do mesmo tipo* e tudo "funciona".** O pior de todos: a conexão tem sucesso, contra o alvo errado, sem erro nenhum. Você descobre pelos dados estranhos. → [[../Problemas-Resolvidos/16-PostgreSQL-Nativo-Ocupa-a-Porta-5432|caso real]]

**3. Não há nada na porta.** `ERR_CONNECTION_REFUSED` — o servidor simplesmente não está no ar. → [[../Problemas-Resolvidos/12-Conexao-Recusada-no-Localhost|caso real]]

## Diagnóstico em três passos

```powershell
Get-NetTCPConnection -LocalPort 5432 -State Listen
```

Se houver alguém, descubra quem:

```powershell
Get-CimInstance Win32_Process -Filter "ProcessId = <PID>" | Select-Object CommandLine
```

E só então decida entre encerrar o processo ou deslocar a sua porta.

> [!problema] Prefira deslocar a matar
> Em máquina de desenvolvimento com serviços nativos instalados, adote portas deslocadas para containers por padrão — 5433 para Postgres, 3307 para MySQL, 6380 para Redis. Custa uma linha no compose e elimina a classe inteira de conflito silencioso.

## Distinguir os erros economiza metade do diagnóstico

| Erro | Significa |
|---|---|
| **ERR_CONNECTION_REFUSED** | Nada escutando — servidor fora do ar |
| **404** | Servidor no ar, rota inexistente |
| **500** | Servidor no ar, falhou ao processar — suspeite do banco ([[../Problemas-Resolvidos/19-Docker-Parado-Causa-Erro-500|caso real]]) |

## Sobre expor uma porta na rede

`localhost` significa "esta máquina". Para outra pessoa acessar, é preciso IP alcançável, servidor escutando em `0.0.0.0` e firewall liberado — e, antes disso, pensar em autenticação. → [[../Problemas-Resolvidos/13-Acesso-Externo-ao-Localhost|nota completa]]

## Links relacionados

- Ambiente: [[01-Maquina-Windows|Máquina Windows]]
- Tecnologia: [[../Tecnologias/04-Docker|Docker]]

## Perguntas de revisão

Quais são os três tipos de conflito de porta? :: Porta ocupada e servidor não sobe; porta ocupada por serviço do mesmo tipo e conexão no alvo errado; e nada escutando na porta.

Por que preferir deslocar a porta a matar o processo? :: Porque evita derrubar serviços nativos e elimina a classe inteira de conflito silencioso.

Quais portas deslocadas usar para Postgres, MySQL e Redis em containers? :: 5433, 3307 e 6380.

Em que porta o Streamlit roda por padrão? :: Na 8501.
