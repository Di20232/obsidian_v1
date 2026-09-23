---
tags: [guia, debugging, problemas, flashcards]
aliases: [Resolver Problemas]
cssclasses: [cerebro-nota, cerebro-geral]
---

# Guia para Resolver Problemas

## Ciclo de depuração

```text
Observar → reproduzir → reduzir → formular hipótese → testar → corrigir → prevenir → registrar
```

## Roteiro

1. **Descreva o fato.** O que era esperado? O que ocorreu? Onde e quando?
2. **Reproduza.** Encontre a menor sequência que provoca o comportamento.
3. **Guarde evidências.** Mensagem de erro, entrada usada, versão, horário, logs seguros e captura relevante.
4. **Reduza.** Remova partes até restar um caso pequeno que ainda falha.
5. **Crie uma hipótese por vez.** Mude uma variável e observe o resultado; não faça várias alterações às cegas.
6. **Corrija a causa, não o sintoma.** Confirme que os casos vizinhos continuam funcionando.
7. **Previna.** Adicione teste, validação, monitoramento, documentação ou checklist quando fizer sentido.
8. **Registre.** Use [[../Templates/Template-Problema|o template de problema]] e conecte à tecnologia e ao projeto.

## Checklist rápido

- [ ] Consigo reproduzir o problema?
- [ ] Tenho o erro completo e o contexto mínimo?
- [ ] Diferenciei causa, efeito e tentativa de correção?
- [ ] Testei o caminho feliz e os limites relevantes?
- [ ] O dado foi protegido — sem publicar senhas, tokens ou informação pessoal?
- [ ] Registrei a lição para não pagar o mesmo custo duas vezes?

Veja também [[../../Programacao-Geral/12-Debugging-e-Testes|Debugging e Testes]] e [[../Problemas-Resolvidos/00-Indice|Problemas Resolvidos]].

## Perguntas de revisão

Qual o ciclo de depuração do cofre? :: Observar, reproduzir, reduzir, formular hipótese, testar, corrigir, prevenir e registrar.

Por que testar uma hipótese por vez? :: Porque mudar várias coisas às cegas impede saber qual alteração teve efeito.

Que evidências guardar ao investigar um problema? :: Mensagem de erro, entrada usada, versão, horário, logs seguros e captura relevante.

O que significa corrigir a causa e não o sintoma? :: Resolver a origem do problema e confirmar que os casos vizinhos continuam funcionando.
