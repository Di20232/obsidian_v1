---
tags: [pratica, auditoria, engenharia, qualidade]
cssclasses: [cerebro-nota, cerebro-praticas]
---

# Auditoria de projetos antes de grandes mudanças

## Objetivo

Entender o sistema antes de pedir uma grande refatoração ou uma “otimização completa”. Isso reduz o risco de remover algo importante ou introduzir falhas invisíveis.

## Roteiro

1. mapeie linguagem, framework, dependências, scripts e ambiente;
2. leia README, configurações, variáveis de ambiente de exemplo e pontos de entrada;
3. identifique autenticação, banco de dados, integrações e dados sensíveis;
4. liste bugs, TODOs, partes duplicadas e fluxos incompletos;
5. reproduza o projeto e registre uma linha de base de comportamento;
6. proponha um plano com mudanças pequenas, priorizadas por impacto e risco;
7. teste cada etapa e mantenha uma forma de reversão.

## Particularidades de e-commerce

Preço, estoque, pagamento, permissões e dados pessoais devem ser tratados como áreas críticas. O front-end não pode ser a fonte final de verdade para nenhuma delas.

## Links relacionados

- [[../Projetos/04-Planejamento-de-E-commerce|Planejamento de E-commerce]]
- [[../Mapas/03-Mapa-Engenharia|Engenharia de Software]]
- [[../Mapas/04-Mapa-Seguranca|Segurança]]
