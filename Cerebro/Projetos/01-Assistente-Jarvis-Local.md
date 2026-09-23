---
tags: [projeto, ia, automacao, javascript, node]
status: entregue-localmente
cssclasses: [cerebro-nota, cerebro-projetos]
---

# Assistente JARVIS Local

> [!projeto] Registro de contexto
> Projeto criado em uma conversa anterior. O estado abaixo descreve o que foi confirmado naquela entrega; a execução atual deve ser validada antes de qualquer nova alteração.

## Objetivo

Criar uma assistente pessoal local em português, com painel de foco e tarefas, rotinas, memória no navegador e uma experiência de comando por texto e voz.

## Entrega confirmada

- interface web responsiva;
- painel de prioridades, missões, rotinas e Pomodoro;
- conversa em português e resposta por voz no navegador;
- memória e backup em JSON guardados localmente no navegador;
- projeto sem dependências externas, executável com Node.

## Arquitetura registrada

| Parte | Responsabilidade |
|---|---|
| `index.html` | estrutura da interface |
| `styles.css` | aparência e responsividade |
| `app.js` | interações, estado no navegador e comandos |
| `server.mjs` | servidor local |
| `README.md` | instruções de uso |

## Como retomar com segurança

1. Abra a pasta do projeto e leia o README atualizado.
2. Confirme a versão do Node e execute localmente.
3. Teste painel, tarefas, rotinas, foco, conversa e backup antes de refatorar.
4. Verifique onde os dados locais estão guardados antes de limpar o navegador.
5. Registre qualquer erro em [[../Problemas-Resolvidos/00-Indice|Problemas Resolvidos]].

## Limites conhecidos

- dados persistem somente no navegador, portanto dependem do perfil e das configurações locais;
- voz e notificações variam conforme o navegador e suas permissões;
- o painel não substitui uma integração real com IA, calendário ou automações externas.

## Links relacionados

- [[../Mapas/05-Mapa-IA|IA e Automação]]
- [[../Mapas/03-Mapa-Engenharia|Engenharia de Software]]
- [[../Guias/03-Criar-Projeto|Guia para Criar Projetos]]
