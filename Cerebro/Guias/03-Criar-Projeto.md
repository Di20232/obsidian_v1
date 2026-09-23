---
tags: [guia, projeto, planejamento, flashcards]
aliases: [Criar Projetos]
cssclasses: [cerebro-nota, cerebro-geral]
---

# Guia para Criar Projetos

Comece com um resultado pequeno, verificável e útil. A arquitetura deve servir ao problema, não ao entusiasmo por uma ferramenta.

## Antes de escrever código

1. **Problema:** quem tem qual dificuldade?
2. **Resultado mínimo:** qual ação a pessoa conseguirá concluir na primeira versão?
3. **Dados:** quais informações existem, de onde vêm e quem pode vê-las?
4. **Fluxo:** desenhe o caminho principal do início ao fim.
5. **Riscos:** o que pode causar perda de dados, exposição ou bloqueio?
6. **Critério de pronto:** como confirmar que a versão funciona?

## Estrutura da nota de projeto

Crie uma nota em [[../Projetos/00-Indice|Projetos]] a partir de [[../Templates/Template-Projeto|Template de Projeto]]. Mantenha nela links para decisões, problemas e tecnologias usadas.

## Durante a construção

- avance em fatias verticais: tela + regra + dado de uma função pequena;
- mantenha o projeto executável com frequência;
- faça commits com mudanças coerentes;
- teste o caminho principal antes de adicionar extras;
- anote decisões que tenham alternativas relevantes;
- trate configurações e segredos como informação separada do código.

## Antes de chamar de pronto

- [ ] O fluxo principal atende ao critério de pronto?
- [ ] Erros comuns têm feedback compreensível?
- [ ] Dados inválidos não são aceitos?
- [ ] Dados importantes têm backup ou plano de recuperação?
- [ ] README explica como iniciar e testar?
- [ ] Próximas melhorias estão priorizadas, não perdidas na cabeça?

## Perguntas de revisão

O que definir antes de escrever código num projeto? :: Problema, resultado mínimo, dados, fluxo principal, riscos e critério de pronto.

O que é avançar em fatias verticais? :: Entregar tela, regra e dado de uma função pequena de ponta a ponta, em vez de uma camada inteira por vez.

O que conferir antes de chamar um projeto de pronto? :: Fluxo principal, feedback de erros, rejeição de dados inválidos, backup, README e próximas melhorias priorizadas.
