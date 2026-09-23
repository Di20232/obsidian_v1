---
tags: [ia, rag, busca, llm, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# RAG: busca + geração

**RAG** (*retrieval-augmented generation*, geração aumentada por recuperação) é a técnica de **buscar** os trechos relevantes nas suas fontes e **colocá-los no contexto** do modelo antes de ele responder. O modelo passa a responder com base nas **suas** notas, e não só no que aprendeu no treino.

É o jeito mais comum e barato de fazer uma IA "saber" o conteúdo de um cofre como este.

## O fluxo

```text
pergunta
  → busca semântica (ou híbrida) nos trechos das notas
  → seleciona os 3 a 10 trechos mais relevantes
  → monta o prompt: instrução + trechos com a fonte + pergunta
  → modelo responde citando de qual nota veio cada informação
```

Um prompt típico:

```text
Responda à pergunta usando apenas os trechos abaixo.
Cite a nota de origem entre colchetes depois de cada informação.
Se os trechos não trazem a resposta, diga que o cofre não cobre esse assunto.

<trecho fonte="Ecommerce/22-Shopee.md" verificado_em="2026-09-23">…</trecho>
<trecho fonte="Ecommerce/20-Marketplaces-Visao-Geral.md">…</trecho>

Pergunta: qual a comissão da Shopee para um item de R$ 150?
```

## Por que RAG em vez de treinar

| RAG | Fine-tuning |
|---|---|
| a informação atualiza assim que a nota muda | precisa treinar de novo para atualizar |
| cita a fonte, dá para conferir | o modelo "sabe", mas não diz de onde |
| barato de montar | exige dados preparados e custo de treino |
| bom para **conhecimento** (fatos, regras, preços) | bom para **comportamento** (formato, tom, tarefas repetidas) |

Taxas de marketplace mudam todo trimestre: esse tipo de dado deve ficar no RAG, nunca "gravado" no modelo. Veja [[05-Fine-Tuning|quando fazer fine-tuning]].

## Onde o RAG erra, e como corrigir

| Problema | Sintoma | Correção |
|---|---|---|
| **busca trouxe o trecho errado** | resposta confiante sobre outra coisa | melhorar chunking, busca híbrida, títulos mais descritivos |
| **trecho certo ficou de fora** | "o cofre não cobre" quando cobre | buscar mais trechos, reescrever a pergunta antes de buscar |
| **informação desatualizada** | taxa antiga | metadado `verificado_em` no trecho; preferir o mais recente |
| **notas contraditórias** | resposta mistura versões | manter uma nota por assunto e atualizar em vez de duplicar |
| **modelo ignora o contexto** | inventa além dos trechos | instrução explícita, temperatura baixa, pedir citação |

A maior parte da qualidade de um RAG vem da **organização das notas**, não do modelo. As regras deste cofre (uma ideia por seção, links, não duplicar) são exatamente as que tornam a busca boa.

## Ponto de partida neste cofre

O exportador `node ferramentas/exportar-para-ia.js` gera `exportacao/notas.jsonl`, com uma nota por linha, texto limpo e metadados. É a matéria-prima para indexar num RAG ([[06-Preparar-Dados-para-Treinar-IA|preparar dados]]).

## Perguntas de revisão

O que é RAG? :: Uma técnica que busca trechos relevantes nas suas fontes e os coloca no contexto do modelo antes da resposta.

Por que RAG é melhor que fine-tuning para dados que mudam? :: Porque a resposta muda assim que a nota muda, sem treinar de novo, e a fonte pode ser citada.

Para que tipo de coisa o fine-tuning é melhor que o RAG? :: Para comportamento: formato, tom e tarefas repetidas.

Qual o erro mais comum num RAG e como corrigir? :: A busca trazer o trecho errado; corrige-se com chunking melhor, títulos descritivos e busca híbrida.

Por que pedir citação da nota de origem? :: Para conferir a resposta e reduzir invenção.

De onde vem a maior parte da qualidade de um RAG? :: Da organização das fontes: uma ideia por seção, títulos claros e sem duplicatas contraditórias.

---
Anterior: [[03-Embeddings-e-Busca-Semantica|Embeddings]] · Próxima: [[05-Fine-Tuning|Fine-tuning]] · Trilha: [[IA-Aplicada/00-Indice|IA Aplicada]]
