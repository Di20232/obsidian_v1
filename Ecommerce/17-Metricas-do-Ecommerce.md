---
tags: [ecommerce, metricas, dados, gestao]
cssclasses: [cerebro-nota, cerebro-ecommerce]
---

# Métricas do e-commerce

Poucas métricas, olhadas sempre, valem mais que um painel com cinquenta números que ninguém lê.

## As fórmulas

| Métrica | Fórmula | Responde |
|---|---|---|
| **Taxa de conversão** | pedidos / sessões | a loja convence quem chega? |
| **Ticket médio** | receita / pedidos | quanto cada pedido vale? |
| **Abandono de checkout** | 1 − (pedidos / checkouts iniciados) | onde o cliente desiste? |
| **CAC** (custo de aquisição de cliente) | gasto em marketing / clientes novos | quanto custa conquistar alguém? |
| **ROAS** (retorno sobre anúncio) | receita atribuída ao anúncio / gasto no anúncio | cada real em anúncio volta quanto? |
| **ROAS de equilíbrio** | 1 / margem de contribuição antes do anúncio | abaixo disso, o anúncio dá prejuízo |
| **Margem de contribuição** | receita − custos variáveis | sobra algo em cada venda? ([[02-Planejamento-e-Precificacao\|a conta]]) |
| **Taxa de recompra** | clientes com 2+ pedidos / total de clientes | o cliente volta? |
| **LTV** (valor do cliente no tempo) | ticket médio × pedidos por cliente no período × margem | quanto um cliente deixa de margem ao longo do tempo? |
| **LTV / CAC** | LTV / CAC | o negócio se paga a longo prazo? |

## Um mês de exemplo

| Dado do mês | Valor |
|---|---|
| Sessões | 5.000 |
| Checkouts iniciados | 150 |
| Pedidos | 60 |
| Receita | R$ 6.000 |
| Gasto em anúncios | R$ 1.500 |
| Clientes novos | 45 |
| Margem antes do anúncio | 31% |

```text
conversão          = 60 / 5.000            = 1,2%
ticket médio       = 6.000 / 60            = R$ 100
abandono checkout  = 1 − 60/150            = 60%
CAC                = 1.500 / 45            ≈ R$ 33,33
ROAS               = 6.000 / 1.500         = 4,0
ROAS de equilíbrio = 1 / 0,31              ≈ 3,2      → ROAS 4 está acima: dá lucro, mas pouco
contribuição       = 6.000 × 0,31 − 1.500  = R$ 360   → e a mensalidade da plataforma, os apps e o contador ainda não saíram
```

Com 1,8 pedido por cliente em 12 meses:

```text
LTV       = 100 × 1,8 × 0,31 ≈ R$ 55,80
LTV / CAC = 55,80 / 33,33    ≈ 1,7
```

Uma referência muito usada é LTV/CAC de pelo menos 3. Com 1,7, a loja conquista cliente caro demais para o quanto ele compra. As saídas são aumentar a recompra ([[16-Email-e-Retencao|retenção]]), o ticket (kits, frete grátis acima de um valor) ou a margem, ou reduzir o CAC (SEO, conteúdo, indicação).

> [!tip] ROAS alto pode enganar
> O ROAS do painel de anúncios conta vendas que talvez acontecessem de qualquer jeito (cliente que já ia comprar e clicou no anúncio de marca). Compare sempre com o resultado da loja inteira: se o gasto em anúncio dobra e a receita total não se mexe, o ROAS do painel está otimista. A métrica para essa comparação é o **MER**, explicado em [[32-Rastreamento-e-Mensuracao|rastreamento e mensuração]].

## Onde ver na Shopify

**Análises** mostra o painel com sessões, conversão, ticket médio, receita e canais, além de relatórios de vendas por produto, por canal e por cliente. Dá para exportar para planilha. Anúncios têm os próprios painéis (Meta, Google). Cruze pelo menos uma vez por mês com a receita real.

## Que métrica mexe em quê

| Se isto está ruim | Olhe primeiro |
|---|---|
| Conversão baixa | fotos, descrição, preço, frete aparecendo tarde, confiança (avaliações, políticas), velocidade no celular |
| Abandono de checkout alto | frete caro ou surpresa, poucas formas de pagamento, pedir cadastro obrigatório |
| CAC alto | criativo, público, oferta; dependência só de anúncio |
| Recompra baixa | experiência de entrega, pós-venda, e-mails de recompra |
| Ticket baixo | kits, produto complementar no carrinho, frete grátis acima de um valor |

---
Anterior: [[16-Email-e-Retencao|E-mail e retenção]] · Próxima: [[18-Checklist-de-Lancamento|Checklist de lançamento]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
