---
tags: [ia, embeddings, busca, dados, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Embeddings e busca semântica

Uma busca comum procura **palavras**: "frete" só acha textos com "frete". Uma **busca semântica** procura **significado**: a pergunta "quanto custa entregar o pacote?" encontra a nota de frete mesmo sem a palavra.

Quem faz isso possível são os **embeddings**.

## O que é um embedding

Um embedding é uma **lista de números** (um vetor, com centenas ou milhares de posições) que representa o significado de um texto. Um modelo de embeddings transforma textos em vetores de modo que:
- textos de significado parecido ficam com vetores **próximos**;
- textos de assuntos diferentes ficam **distantes**.

```text
"custo de entrega do pedido"   → [0.12, -0.40, 0.88, …]
"valor do frete"               → [0.10, -0.38, 0.91, …]   ← perto
"receita de bolo de cenoura"   → [-0.70, 0.22, 0.05, …]   ← longe
```

## Como medir a proximidade

A medida mais usada é a **similaridade de cosseno**: compara a direção de dois vetores. Vai de −1 a 1; quanto mais perto de 1, mais parecidos os significados.

## Como funciona uma busca semântica

```text
1. Indexar (uma vez, e de novo quando as notas mudam):
   notas → dividir em trechos → gerar embedding de cada trecho → guardar num banco de vetores
2. Buscar (a cada pergunta):
   pergunta → embedding → achar os trechos mais próximos → devolver os melhores
```

## Dividir em trechos (chunking)

Nota inteira como um vetor só mistura assuntos; frase solta perde o contexto. O comum é dividir:
- por **seção** (título `##`), que em notas bem organizadas já é uma unidade de assunto;
- ou por tamanho, com uma pequena **sobreposição** entre trechos para não cortar uma ideia no meio.

Guarde com cada trecho: a nota de origem, o título da seção e os metadados (tags, `verificado_em`). Isso permite **citar a fonte** e filtrar.

As notas deste cofre já ajudam: uma ideia por seção, títulos descritivos, frontmatter com tags ([[06-Preparar-Dados-para-Treinar-IA|preparar dados]]).

## Banco de vetores

Guarda os vetores e encontra rapidamente os mais próximos. Para poucos milhares de trechos, até uma extensão de banco comum resolve (por exemplo, o **pgvector** no PostgreSQL, que já aparece no cofre em [[Cerebro/Tecnologias/05-Prisma-e-PostgreSQL|Prisma e PostgreSQL]]). Para volumes grandes existem bancos especializados.

## Busca híbrida

Busca semântica erra com **códigos e nomes exatos** (SKU, número de lei, nome de função). Busca por palavra acerta esses. A **busca híbrida** combina as duas e costuma ser a melhor opção prática.

## Perguntas de revisão

Qual a diferença entre busca por palavra e busca semântica? :: A busca por palavra procura os termos exatos; a semântica procura textos de significado parecido, mesmo com outras palavras.

O que é um embedding? :: Uma lista de números (vetor) que representa o significado de um texto, de modo que textos parecidos ficam com vetores próximos.

Que medida compara dois embeddings? :: A similaridade de cosseno, que vai de −1 a 1; mais perto de 1 significa mais parecido.

O que é chunking? :: Dividir documentos em trechos menores, por seção ou tamanho, antes de gerar os embeddings.

Por que guardar metadados junto com cada trecho? :: Para citar a fonte da resposta e filtrar por assunto ou data.

Quando a busca semântica falha e o que fazer? :: Com códigos e nomes exatos; a busca híbrida combina semântica e busca por palavra.

---
Anterior: [[02-Escrevendo-Prompts|Escrevendo prompts]] · Próxima: [[04-RAG-Busca-Mais-Geracao|RAG]] · Trilha: [[IA-Aplicada/00-Indice|IA Aplicada]]
