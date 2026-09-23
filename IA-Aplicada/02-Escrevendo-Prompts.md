---
tags: [ia, llm, prompts, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Escrevendo prompts

Um **prompt** é tudo que você envia ao modelo: instrução, contexto, exemplos e dados. A qualidade da resposta depende menos de "palavras mágicas" e mais de **clareza**: escreva como se estivesse passando a tarefa para uma pessoa competente que não conhece o seu negócio.

## As partes de um bom prompt

| Parte | Pergunta que responde | Exemplo |
|---|---|---|
| **Objetivo** | o que é para fazer, e para quê? | "Escreva a descrição de um produto para a página da loja" |
| **Contexto** | o que o modelo precisa saber e não sabe? | público, tom da marca, dados do produto, restrições |
| **Material** | com base em quê? | a ficha técnica colada, o texto a revisar |
| **Formato** | como a resposta deve vir? | "título de até 60 caracteres, 3 tópicos, 1 parágrafo" |
| **Critérios** | como saber se ficou bom? | "sem promessas que não estão na ficha; sem superlativos" |
| **Exemplos** | como é uma resposta boa? | 1 a 3 exemplos do resultado esperado |

## Técnicas que funcionam

- **Dê o porquê.** "Responda em até 3 frases, porque vai aparecer num card no celular" funciona melhor que só "seja breve".
- **Separe material de instrução.** Coloque os dados entre marcadores claros, como `<ficha>…</ficha>` ou blocos de código, para o modelo não confundir o texto a processar com o pedido.
- **Mostre exemplos** (*few-shot*): dois ou três pares de entrada e saída ensinam formato e tom melhor que parágrafos de explicação. Use exemplos variados, senão o modelo copia um só.
- **Peça o raciocínio antes da conclusão** em tarefas com várias etapas: "analise primeiro, depois responda".
- **Permita o "não sei":** "se a informação não estiver no texto, diga que não está".
- **Divida tarefas grandes:** um prompt para extrair, outro para escrever, outro para revisar. Cada etapa fica testável.
- **Peça saída estruturada** (JSON, tabela) quando outra ferramenta vai ler o resultado.

## Exemplo: antes e depois

**Fraco:**
```text
Faça uma descrição legal para minha garrafa.
```

**Bom:**
```text
Escreva a descrição de produto para uma loja online de utilidades para academia.
Público: pessoas que treinam e levam a garrafa para o trabalho.
Tom: direto e prático, sem exageros.

Use somente as informações da ficha abaixo. Se faltar algo importante, liste no fim.

<ficha>
Garrafa térmica inox 500 ml, parede dupla, mantém gelado por 24 h e quente por 12 h,
tampa com trava, cabe no porta-copos do carro, não vai à lava-louças.
</ficha>

Formato:
- título de até 60 caracteres
- 1 parágrafo de até 3 frases
- 4 tópicos de benefício
- 1 linha "Cuidados"
```

## Erros comuns

- **Vago:** "melhore este texto" (melhorar em quê? para quem?).
- **Contexto demais e irrelevante:** o modelo tenta usar tudo que recebe.
- **Pedir o proibido pelo negativo só:** "não use jargão" funciona pior que "use palavras do dia a dia, como se explicasse a um cliente".
- **Aceitar a primeira resposta:** trate como rascunho; ajuste o prompt e compare.

## Guardar prompts que funcionam

Prompt bom é ativo: guarde no cofre com o objetivo, o texto e um exemplo de saída aprovada. Assim ele vira modelo reutilizável e, mais tarde, **dado de avaliação** ([[07-Avaliar-Sistemas-de-IA|avaliação]]).

## Perguntas de revisão

Quais são as partes de um bom prompt? :: Objetivo, contexto, material, formato de saída, critérios de qualidade e, quando útil, exemplos.

Por que explicar o porquê de uma instrução ajuda? :: Porque o modelo entende o objetivo e generaliza melhor do que seguindo uma regra solta.

O que é few-shot? :: Incluir alguns exemplos de entrada e saída no prompt para ensinar formato e tom.

Por que separar o material da instrução com marcadores? :: Para o modelo não confundir o texto a processar com o pedido.

Como reduzir invenção de informações num prompt? :: Pedir para usar só o material fornecido e dizer o que falta quando a informação não estiver lá.

Por que dividir uma tarefa grande em vários prompts? :: Cada etapa fica mais simples e pode ser testada e corrigida separadamente.

---
Anterior: [[01-Como-Funcionam-os-Modelos-de-Linguagem|Como funcionam]] · Próxima: [[03-Embeddings-e-Busca-Semantica|Embeddings]] · Trilha: [[IA-Aplicada/00-Indice|IA Aplicada]]
