---
tags: [pratica, auditoria, engenharia, qualidade, flashcards]
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

## Perguntas de revisão

Por que auditar um projeto antes de uma grande mudança? :: Para entender o sistema antes e não remover algo importante nem introduzir falhas invisíveis.

Qual o roteiro de auditoria de um projeto? :: Mapear stack e ambiente, ler README e configurações, identificar dados sensíveis, listar bugs, reproduzir uma linha de base e propor mudanças pequenas com reversão.

Quais áreas são críticas num e-commerce? :: Preço, estoque, pagamento, permissões e dados pessoais; o front-end nunca é a fonte final de verdade delas.
