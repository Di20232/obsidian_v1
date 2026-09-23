---
tags: [ia, llm, fundamentos, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Como funcionam os modelos de linguagem

Um **modelo de linguagem** (LLM, *large language model*) é um programa treinado com grandes volumes de texto para prever **qual pedaço de texto vem a seguir**. Conversar, resumir, traduzir, escrever código: tudo sai dessa mesma operação, repetida muitas vezes.

## Tokens

O modelo não lê letras nem palavras inteiras, e sim **tokens**: pedaços de texto que podem ser uma palavra, parte de uma palavra ou um sinal. "Precificação" pode virar 3 ou 4 tokens; "a" costuma ser um só. Em português, as palavras costumam gastar mais tokens que em inglês.

Tokens importam porque:
- o **custo** de usar um modelo por API é cobrado por token (de entrada e de saída);
- o **limite de contexto** é medido em tokens.

## Janela de contexto

É o tanto de texto que o modelo consegue considerar de uma vez: a instrução, o histórico da conversa, os documentos colados e a própria resposta. O que fica fora da janela o modelo **não vê**. Conversa muito longa ou documento enorme podem ser cortados ou resumidos.

## Como a resposta nasce

```text
texto de entrada → tokens → modelo calcula a probabilidade de cada próximo token
  → escolhe um → acrescenta ao texto → repete até terminar
```

A **temperatura** controla quanto o modelo arrisca na escolha: baixa, respostas mais previsíveis e repetíveis; alta, respostas mais variadas e criativas. Para extrair dados ou classificar, use baixa. Para ideias, pode subir.

## Treino em etapas

1. **Pré-treino:** o modelo aprende a língua e fatos gerais prevendo o próximo token em textos enormes.
2. **Ajuste por instruções:** aprende a seguir pedidos e conversar, com exemplos de pergunta e resposta.
3. **Ajuste por preferência:** aprende que respostas as pessoas consideram melhores e mais seguras.

O conhecimento do modelo tem **data de corte**: ele não sabe o que aconteceu depois do treino, a menos que receba a informação no contexto, por exemplo com [[04-RAG-Busca-Mais-Geracao|RAG]] ou uma busca na web.

## Alucinação

O modelo produz texto **provável**, não texto **verificado**. Quando falta informação, ele pode gerar uma resposta fluente e errada: uma taxa, uma lei, um nome de função que não existe. Isso se chama **alucinação**.

Como reduzir:
- dar a fonte no contexto e pedir para responder **só com base nela**;
- pedir que diga "não sei" quando a fonte não cobre;
- pedir citação do trecho usado;
- conferir números, leis, preços e código antes de usar.

É por isso que as notas deste cofre marcam `verificado_em` e `fonte` onde o dado envelhece ([[Cerebro/Referencias/00-Referencias-Confiaveis|referências]]).

## O que o modelo faz bem e mal

| Faz bem | Faz mal sem ajuda |
|---|---|
| resumir, reescrever, traduzir, mudar o tom | fatos recentes ou muito específicos |
| extrair campos de texto bagunçado | contas longas de cabeça (use código ou planilha) |
| explicar conceitos e dar exemplos | saber o que está no seu sistema, se ninguém mostrou |
| gerar rascunhos de código e texto | garantir que o código roda sem testar |
| classificar e agrupar | decisões com consequência legal ou financeira sem revisão humana |

## Perguntas de revisão

O que um modelo de linguagem faz, no nível mais básico? :: Prevê qual token de texto vem a seguir, repetindo essa operação para montar a resposta.

O que é um token? :: Um pedaço de texto (palavra, parte de palavra ou sinal) que o modelo usa como unidade; custo e limite de contexto são medidos em tokens.

O que é a janela de contexto? :: O tanto de texto que o modelo considera de uma vez, incluindo instrução, histórico, documentos e resposta; o que fica fora ele não vê.

Para que serve a temperatura? :: Controla o quanto o modelo arrisca na escolha dos tokens: baixa dá respostas previsíveis, alta dá respostas variadas.

O que é alucinação em IA? :: Uma resposta fluente e errada, gerada porque o modelo produz texto provável e não verificado.

Como reduzir alucinações? :: Dar a fonte no contexto, pedir resposta só com base nela, permitir "não sei", pedir citação e conferir números e código.

O que é a data de corte de um modelo? :: O limite do conhecimento aprendido no treino; fatos posteriores só chegam se forem colocados no contexto.

---
Próxima: [[02-Escrevendo-Prompts|Escrevendo prompts]] · Trilha: [[IA-Aplicada/00-Indice|IA Aplicada]]
