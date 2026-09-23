---
tags: [ia, fine-tuning, treino, llm, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Fine-tuning

**Fine-tuning** (ajuste fino) é continuar o treino de um modelo já pronto com **exemplos seus**, para que ele passe a se comportar de um jeito específico sem precisar de instruções longas a cada pedido.

## Quando vale a pena

| Use fine-tuning para | Não use fine-tuning para |
|---|---|
| um **formato** fixo de saída, repetido milhares de vezes | ensinar **fatos que mudam** (preços, taxas, estoque): use [[04-RAG-Busca-Mais-Geracao\|RAG]] |
| um **tom** ou estilo da marca difícil de descrever em palavras | resolver um problema que um prompt melhor já resolve |
| **classificar** textos em categorias suas (ex.: motivo de devolução) | quando você tem poucos exemplos, ou exemplos de qualidade ruim |
| reduzir custo e tempo: modelo menor ajustado fazendo o que um maior faz com prompt longo | quando precisa citar a fonte de cada informação |

**Ordem recomendada:** primeiro um bom [[02-Escrevendo-Prompts|prompt]] com exemplos; depois RAG, se falta conhecimento; fine-tuning só quando os dois não bastam e você tem dados bons.

## Como funciona, sem matemática

1. Você prepara pares de **entrada → saída desejada** (centenas a milhares, conforme a tarefa).
2. O treino ajusta os parâmetros do modelo para que, diante daquelas entradas, as saídas desejadas fiquem mais prováveis.
3. O resultado é um modelo novo, que você chama igual ao original.

Muitos serviços usam técnicas como **LoRA**, que treinam só uma pequena camada extra em vez do modelo inteiro. Sai bem mais barato e dá resultados parecidos para ajustes de comportamento.

## O formato dos dados

O formato mais comum para modelos de conversa é **JSONL**: um exemplo por linha, cada um com as mensagens da conversa.

```json
{"messages": [{"role": "user", "content": "Qual a comissão da Shopee para item de R$ 150?"}, {"role": "assistant", "content": "14% + R$ 20 por item, conforme a tabela válida a partir de 01/10/2026."}]}
```

Muitas vezes há também uma mensagem de sistema com a instrução geral. Cada provedor tem pequenas diferenças de formato: **confira a documentação do serviço que for usar**. O exportador do cofre gera esse formato em `exportacao/perguntas-chat.jsonl` a partir das perguntas de revisão ([[06-Preparar-Dados-para-Treinar-IA|preparar dados]]).

> [!warning] O exemplo acima tem um problema
> A comissão da Shopee **muda**. Treinar o modelo com ela faz a resposta ficar errada no próximo reajuste, sem aviso. Perguntas com dados que envelhecem (as notas com `verificado_em`) devem ficar fora do fine-tuning e ir para o RAG.

## Treino, validação e teste

Separe os exemplos antes de treinar:
- **treino** (~80%): o que o modelo vê;
- **validação** (~10%): para acompanhar durante o treino se ele está aprendendo ou só decorando;
- **teste** (~10%): guardado para a [[07-Avaliar-Sistemas-de-IA|avaliação final]], nunca visto no treino.

**Overfitting** (sobreajuste) é quando o modelo decora os exemplos de treino e piora em casos novos. Sinal: o erro no treino cai e o erro na validação sobe.

## Qualidade vence quantidade

- Exemplos **corretos** e **consistentes**: se metade das respostas usa um formato e metade outro, o modelo aprende a confusão.
- **Variedade** de casos, incluindo os difíceis e os "não sei".
- **Sem dados pessoais** nem segredos: o modelo pode reproduzir o que aprendeu.
- Poucas centenas de exemplos excelentes costumam valer mais que milhares medianos.

## Perguntas de revisão

O que é fine-tuning? :: Continuar o treino de um modelo pronto com exemplos próprios para mudar o comportamento dele.

Quando não usar fine-tuning? :: Para ensinar fatos que mudam, quando um prompt melhor resolve, com poucos exemplos ruins ou quando é preciso citar a fonte.

Qual a ordem recomendada antes de fazer fine-tuning? :: Primeiro melhorar o prompt com exemplos, depois usar RAG se faltar conhecimento, e só então fine-tuning.

O que é LoRA? :: Uma técnica que treina só uma pequena camada extra em vez do modelo inteiro, reduzindo o custo do ajuste.

Qual o formato mais comum de dados para fine-tuning de modelos de conversa? :: JSONL, com um exemplo por linha contendo a lista de mensagens da conversa.

Como dividir os dados de treino? :: Cerca de 80% para treino, 10% para validação e 10% para teste final, que nunca entra no treino.

O que é overfitting? :: Quando o modelo decora os exemplos de treino e piora em casos novos; o erro de validação sobe enquanto o de treino cai.

Por que não treinar o modelo com taxas e preços? :: Porque mudam, e o modelo passa a responder o valor antigo sem avisar; esse tipo de dado deve ir para o RAG.

---
Anterior: [[04-RAG-Busca-Mais-Geracao|RAG]] · Próxima: [[06-Preparar-Dados-para-Treinar-IA|Preparar dados]] · Trilha: [[IA-Aplicada/00-Indice|IA Aplicada]]
