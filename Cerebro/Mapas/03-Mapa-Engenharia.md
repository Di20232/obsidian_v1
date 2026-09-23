---
tags: [moc, engenharia-de-software, qualidade, flashcards]
aliases: [Engenharia de Software]
cssclasses: [cerebro-nota, cerebro-engenharia]
---

# ⚙️ Mapa de Engenharia de Software

Engenharia de software é a disciplina de tornar uma solução confiável para evoluir, usar e manter ao longo do tempo.

## Ciclo de entrega

```text
Entender necessidade → planejar → implementar → revisar → testar → publicar → observar → melhorar
```

## Pilares

| Pilar | Pergunta que orienta |
|---|---|
| Requisitos | que problema real será resolvido e para quem? |
| Arquitetura | onde cada responsabilidade deve morar? |
| Git | consigo entender, revisar e recuperar mudanças? |
| Testes | o comportamento importante continua funcionando? |
| Qualidade | o código comunica a intenção e evita repetição perigosa? |
| Entrega | consigo publicar de forma previsível? |
| Observabilidade | se falhar, consigo descobrir o que ocorreu? |
| Documentação | outra pessoa consegue começar sem depender da memória de alguém? |

## Notas do cofre

- [[../../Programacao-Geral/03-Git-e-Controle-de-Versao|Git e Controle de Versão]]
- [[../../Programacao-Geral/12-Debugging-e-Testes|Debugging e Testes]]
- [[../../Programacao-Geral/13-Boas-Praticas-de-Codigo|Boas Práticas de Código]]
- [[../Guias/02-Resolver-Problemas|Resolver Problemas]]
- [[../Guias/03-Criar-Projeto|Criar Projetos]]
- [[../Praticas/00-Indice|Práticas e Padrões]]

## Princípios úteis

- Faça a menor mudança que resolve o problema e confirme o efeito.
- Prefira nomes claros a comentários que tentam explicar nomes confusos.
- Mantenha segredos fora do código e fora do histórico.
- Automatize o que é repetitivo, crítico e verificável.
- Registre decisões que seriam difíceis de redescobrir depois.

## Perguntas de revisão

O que é engenharia de software? :: A disciplina de tornar uma solução confiável para evoluir, usar e manter ao longo do tempo.

Qual o ciclo de entrega de software? :: Entender a necessidade, planejar, implementar, revisar, testar, publicar, observar e melhorar.

O que é observabilidade? :: A capacidade de descobrir o que aconteceu quando o sistema falha, por logs e registros.

O que vale automatizar? :: O que é repetitivo, crítico e verificável.
