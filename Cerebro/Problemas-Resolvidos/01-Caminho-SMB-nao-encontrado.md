---
tags: [problema-resolvido, rede, windows, smb]
status: roteiro-validado
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Erro 0x80070035: caminho de rede não encontrado

> [!problema] Sintoma
> O Windows não consegue abrir um compartilhamento de rede e informa que o caminho não foi encontrado.

## Causa provável

O erro indica que a máquina não alcança o compartilhamento SMB ou que o caminho informado está incompleto/incorreto. Ao acessar por IP, DNS geralmente não é a primeira hipótese; rede, porta 445, nome do compartilhamento, serviço e permissões são mais prováveis.

## Diagnóstico seguro, na ordem certa

1. Confirme o formato: `\\servidor\\nome-do-compartilhamento` — o nome da pasta compartilhada é obrigatório.
2. Verifique se a máquina está na rede ou VPN correta e se o servidor está ligado.
3. Teste conectividade básica e depois a porta SMB (445), sem alterar configurações ainda.
4. Se a porta responder, confira o nome do compartilhamento e as permissões da conta.
5. No servidor, confirme serviço **Servidor**, compartilhamento existente e regra de firewall para SMB.

## Interpretação

| Resultado | Próxima hipótese |
|---|---|
| servidor inacessível | rede, VPN, cabo, Wi-Fi, rota ou equipamento desligado |
| servidor acessível, porta 445 bloqueada | firewall, segmentação de rede ou política de VPN |
| porta 445 acessível, caminho falha | nome do compartilhamento ou permissões |

## Prevenção

- documentar o nome dos compartilhamentos e responsáveis;
- usar SMB moderno e evitar habilitar SMBv1 como tentativa genérica;
- registrar mudanças de VPN, firewall e rede que afetem servidores;
- manter um teste simples de acesso após manutenção.

## Links relacionados

- [[../Ambiente/00-Indice|Ambiente]]
- [[../Guias/02-Resolver-Problemas|Resolver Problemas]]
