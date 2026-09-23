---
tags: [github, conceito, testes, python, flashcards]
cssclasses: [cerebro-nota, cerebro-engenharia]
verificado_em: 2026-09-15
---
# Testar comportamento durante uma refatoração

## Ideia central

Mudar a organização interna do código não deveria alterar, sem intenção, as respostas que o usuário recebe.

No [[Cerebro/GitHub/exercises_python/01-Guia-de-Estudo|exercises_python]], duas versões resolvem os mesmos cinco exercícios. O [[Cerebro/GitHub/exercises_python/Fontes/comparar_saidas.py.md|comparador de saídas]] oferece uma forma prática de detectar divergências.

## Teste de equivalência

1. Defina uma entrada completa.
2. Execute as duas versões em condições comparáveis.
3. Compare saída e código de término.
4. Investigue qualquer diferença.
5. Acrescente uma expectativa independente para os resultados importantes.

**Duas versões iguais podem estar igualmente erradas.** Por isso, equivalência é útil para preservar comportamento, mas precisa de testes que expressem o resultado correto.

## Quando usar cada nível

| Situação | Teste que ajuda |
|---|---|
| Regra de classificação de aluno | Unitário: entrada → situação esperada |
| Mesmo recibo em dois estilos de código | Comparação de saída |
| Venda que altera saldo e extrato | Integração com banco |
| Carrinho e checkout acessíveis na tela | Teste de fluxo/interface |
| Duas vendas disputando a última unidade | Teste de concorrência |

No ByteShop há testes de API organizados por assunto. No Contro Vend a suíte de integração usa um banco descartável e verifica comportamento real de rotas. Isso é diferente de apenas conferir se o código tem sintaxe válida.

[[Programacao-Geral/12-Debugging-e-Testes|Debugging e testes]] · [[Cerebro/GitHub/00-Indice|GitHub]]

## Perguntas de revisão

O que é um teste de equivalência numa refatoração? :: Rodar a versão antiga e a nova com a mesma entrada e comparar saídas e código de término.

Por que só comparar duas versões não basta? :: Porque as duas podem estar igualmente erradas; é preciso teste com o resultado correto esperado.

Que tipo de teste usar para duas vendas disputando a última unidade? :: Teste de concorrência.
