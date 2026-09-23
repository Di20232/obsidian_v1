---
tags: [moc, ambiente, ferramentas]
aliases: [Ambiente]
cssclasses: [cerebro-nota, cerebro-ambiente]
---

# 💻 Ambiente de Trabalho

Configurações locais que economizam tempo na próxima manutenção: ferramentas, versões, portas, serviços e armadilhas conhecidas.

Volta para [[../00-Cerebro|🧠 Cérebro]].

## Notas

| # | Nota | Para quê |
|---|---|---|
| 01 | [[01-Maquina-Windows\|Máquina Windows]] | O que está instalado e as cinco armadilhas do Windows |
| 02 | [[02-Portas-e-Conflitos\|Portas e conflitos]] | Mapa de portas e diagnóstico de conflito |
| 03 | [[03-Contas-Git\|Contas Git]] | Duas contas GitHub e como trocar a autenticada |

> [!problema] Metade dos problemas deste cofre é de ambiente
> Porta ocupada, container parado, dependência ausente, credencial errada. Nenhum desses aparece lendo o código — e todos custaram tempo real. Vale consultar estas três notas **antes** de suspeitar da aplicação.

## O que registrar

- pré-requisitos para executar um projeto;
- versões que realmente importam;
- localização segura de configurações, sem incluir senhas ou tokens;
- como iniciar, testar e parar um serviço;
- como conferir se algo está funcionando;
- problemas recorrentes específicos do ambiente.

## Segurança

Nunca armazene neste cofre senhas, chaves privadas, tokens, arquivos `.env` reais, dados de clientes ou informações pessoais. Anote apenas o nome da variável, o local seguro e o processo de obtenção autorizado.

Conecte cada registro ao [[../Projetos/00-Indice|projeto]] e à [[../Tecnologias/00-Indice|tecnologia]] correspondente.
