---
tags: [problema-resolvido, ambiente, windows, servidor]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Porta 3000 presa por processo órfão

## Contexto

[[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] · servidor de desenvolvimento local.

## Sintoma e impacto

O servidor se recusava a subir:

```
Port 3000 is in use by "node.exe" (PID 11240) (not a preview server)
```

## Causa-raiz

Um servidor de desenvolvimento de uma sessão anterior **sobreviveu ao comando de parada** e continuou segurando a porta. O processo ficou órfão: sem terminal associado, sem ninguém monitorando, mas vivo e com a porta reservada.

## Correção aplicada

Primeiro **confirmar de quem é o processo** antes de matar qualquer coisa — esse passo importa, porque a porta 3000 é usada por muitos projetos:

```powershell
$p = Get-CimInstance Win32_Process -Filter "ProcessId = 11240"
$p.CommandLine
```

Só depois de ver que a linha de comando apontava para o servidor deste projeto:

```powershell
Stop-Process -Id 11240 -Force
```

E, para o problema não voltar, `autoPort: true` no `.claude/launch.json` — assim, se a porta estiver ocupada, o servidor escolhe outra em vez de falhar. O app já lia `PORT` do ambiente, e o `dotenv` não sobrescreve variável já definida, então funcionou sem outras mudanças.

## Prevenção

> [!problema] Nunca mate um PID sem olhar a linha de comando
> Ver a porta ocupada não diz de quem ela é. `Get-CimInstance Win32_Process` mostra o comando completo — é a diferença entre encerrar seu servidor esquecido e derrubar outra coisa da máquina.
>
> Para descobrir quem está na porta:
> ```powershell
> Get-NetTCPConnection -LocalPort 3000 -State Listen | Select-Object OwningProcess
> ```

## Links relacionados

- Projeto: [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]]
- Ambiente: [[../Ambiente/02-Portas-e-Conflitos|Portas e conflitos]]
- Relacionado: [[12-Conexao-Recusada-no-Localhost|Conexão recusada]]
