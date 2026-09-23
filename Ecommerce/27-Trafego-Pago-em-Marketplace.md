---
tags: [ecommerce, marketplace, trafego-pago, anuncios, metricas, flashcards]
cssclasses: [cerebro-nota, cerebro-ecommerce]
verificado_em: 2026-09-23
---

# Tráfego pago em marketplace

Anúncio dentro do marketplace é diferente de anúncio no Instagram ou no Google. A pessoa **já está pesquisando para comprar**, e o anúncio só empurra o seu produto para as primeiras posições da busca ou das recomendações. Por isso costuma converter bem, mas disputa com a comissão pela mesma margem.

As duas ferramentas principais têm notas próprias: [[28-Mercado-Ads|Mercado Ads]] e [[29-Shopee-Ads|Shopee Ads]].

## Como funciona

1. Você escolhe **o que anunciar** (produtos, ou a loja).
2. Define **quanto quer gastar** (orçamento diário) e **qual retorno espera** (ROAS objetivo), ou um **lance** por clique.
3. A plataforma faz um **leilão** a cada busca: quem combina lance maior e anúncio mais relevante aparece no topo.
4. Você paga **por clique** (CPC). A exibição não é cobrada.
5. O painel atribui ao anúncio as vendas feitas depois do clique e calcula ROAS e ACOS.

## ROAS e ACOS: a mesma coisa de dois jeitos

```text
ROAS = receita atribuída ao anúncio / investimento
ACOS = investimento / receita atribuída ao anúncio   (= 1 / ROAS, em %)
```

| Investimento | Receita | ROAS | ACOS |
|---|---|---|---|
| R$ 100 | R$ 1.000 | 10 | 10% |
| R$ 1.000 | R$ 4.500 | 4,5 | 22,2% |
| R$ 1.000 | R$ 3.000 | 3,0 | 33,3% |

O Mercado Livre e a Shopee mostram os dois. Use o que achar mais intuitivo, mas **sempre compare com o equilíbrio** da tabela abaixo.

## O equilíbrio no marketplace é mais apertado

A regra é a mesma de [[17-Metricas-do-Ecommerce|métricas]]: **ACOS máximo = margem antes do anúncio**, e **ROAS mínimo = 1 / margem**. A diferença é que, no marketplace, a margem já perdeu a comissão.

Mesmo produto de R$ 150, custo R$ 60, embalagem R$ 3, imposto 4%:

| Canal | Taxas do canal | Sobra antes do anúncio | ACOS máximo | ROAS mínimo |
|---|---|---|---|---|
| Loja Shopify (≈5% provedor + 2%) | R$ 10,48 | R$ 70,51 (47%) | 47% | 2,1 |
| Shopee (14% + R$ 20) | R$ 41,00 | R$ 40,00 (26,7%) | 26,7% | 3,75 |
| Mercado Livre Premium (17% + ~R$ 20 de frete, ilustrativo) | R$ 45,50 | R$ 35,50 (23,7%) | 23,7% | 4,2 |

Na Shopee, uma campanha com ROAS 3 **perde dinheiro**, e a mesma campanha com ROAS 3 daria lucro na loja própria.

Com o exemplo da Shopee (margem de 26,7%):

```text
ROAS 4,5 → R$ 4.500 × 26,7% − R$ 1.000 = + R$ 200 de contribuição
ROAS 3,0 → R$ 3.000 × 26,7% − R$ 1.000 = − R$ 200
```

> [!tip] Calcule o ROAS mínimo de cada produto
> Produtos diferentes têm margens diferentes. Guarde numa planilha o ROAS mínimo de cada um e use-o como **ROAS objetivo** na campanha, com uma folga para cima. Veja [[02-Planejamento-e-Precificacao|a conta completa]].

## Atribuição: o que o painel conta como venda do anúncio

- Na Shopee, a receita padrão conta vendas **do produto anunciado e de outros produtos da loja** feitas em até **7 dias** após o clique. A **receita direta** conta só o produto anunciado. Por isso existem ROAS e ROAS direto.
- No Mercado Livre, o Product Ads conta uma venda para cada produto diferente no carrinho.
- Nos dois, parte dessas vendas aconteceria **sem o anúncio**: gente que já ia comprar clicou no patrocinado. É a **canibalização** do orgânico.

**Teste de verdade:** compare o faturamento **total** do produto (orgânico + pago) antes e depois de ligar a campanha. Se o anúncio registra R$ 3.000 de vendas, mas o total do produto subiu só R$ 1.000, o ganho real foi de R$ 1.000.

## O que anunciar

| Anuncie | Evite |
|---|---|
| produtos com margem boa, que suportam o ACOS | produto com margem que já está no limite |
| produtos que **já convertem** organicamente (boas fotos, avaliações, preço competitivo) | anúncio fraco: o clique é pago e a página não converte |
| lançamentos, para gerar as primeiras vendas e avaliações | produto com pouco estoque ou prestes a acabar |
| campeões em datas de pico (11.11, Black Friday) | produto na faixa de preço desfavorável ([[22-Shopee\|degraus]]) |

Anúncio não conserta anúncio ruim: ele só leva mais gente até ele. Antes de pagar, revise [[24-Anuncios-em-Marketplace|título, fotos e ficha]].

## Ciclo de otimização

| Quando | O que fazer |
|---|---|
| Primeira semana | não mexer muito: o algoritmo aprende |
| Toda semana | ver investimento, vendas, ACOS por produto; pausar quem está acima do ACOS máximo há 2 semanas |
| A cada 15 dias | subir o orçamento **aos poucos** (ex.: 20%) de quem está com folga abaixo do ACOS máximo |
| Todo mês | teste de canibalização: faturamento total do produto com e sem anúncio |

Um sinal comum: o orçamento diário **acaba cedo** e o ROAS está bom → aumente o orçamento. O orçamento **sobra** → o ROAS objetivo pode estar alto demais, ou o lance baixo, e o anúncio quase não aparece.

## Métricas do funil do anúncio

```text
impressões → cliques (CTR) → vendas (taxa de conversão) → receita (ROAS/ACOS)
```

| Se isto está ruim | Provável causa |
|---|---|
| poucas impressões | lance baixo, ROAS objetivo alto, orçamento pequeno, palavra-chave sem busca |
| CTR baixo | primeira foto, título, preço ou frete piores que os vizinhos |
| conversão baixa | página do produto: descrição, avaliações, variações, prazo |
| ACOS alto com boa conversão | CPC caro na categoria: teste palavras mais específicas |

## Perguntas de revisão

Qual a relação entre ROAS e ACOS? :: ACOS = 1 / ROAS, em porcentagem; ROAS 4 equivale a ACOS de 25%.

Qual o ACOS máximo aceitável? :: A margem antes do anúncio; acima disso, cada venda anunciada dá prejuízo.

Por que o ROAS mínimo é maior no marketplace do que na loja própria? :: Porque a comissão já consumiu parte da margem antes do anúncio.

Um produto de R$ 150 na Shopee com R$ 40 de sobra antes do anúncio precisa de que ROAS mínimo? :: Cerca de 3,75 (margem de 26,7%).

O que é canibalização em anúncios? :: Quando o anúncio recebe crédito por vendas que aconteceriam de qualquer jeito pelo orgânico.

Como testar se o anúncio traz venda nova? :: Comparar o faturamento total do produto com e sem a campanha.

---
Anterior: [[26-Integracao-Multicanal|Integração multicanal]] · Próxima: [[28-Mercado-Ads|Mercado Ads]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
