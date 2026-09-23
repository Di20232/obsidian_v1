---
tags: [ecommerce, negocio, precificacao, financas, flashcards]
cssclasses: [cerebro-nota, cerebro-ecommerce]
---

# Planejamento e precificação

## O mínimo de planejamento

Uma página resolve. Ela precisa responder:

| Pergunta | Exemplo de resposta útil |
|---|---|
| Para quem? | "Mulheres de 25 a 40 anos que treinam em casa", não "todo mundo" |
| Qual problema resolvo? | "Equipamento compacto que cabe em apartamento" |
| Por que eu? | curadoria, marca própria, entrega rápida na região, conteúdo que ensina a usar |
| Quanto custa operar por mês? | plano da plataforma, apps, domínio, contador, embalagem, internet |
| Quanto posso investir até vender? | estoque inicial + anúncios de teste + reserva |
| Como vou saber que deu errado? | "Se em 90 dias o custo por venda passar do lucro por venda, paro e revejo" |

## Custos fixos e variáveis

- **Fixos:** existem mesmo sem venda — plano da Shopify, apps, contador, domínio, ferramentas.
- **Variáveis:** acontecem **a cada venda** — custo do produto, taxa de pagamento, taxa da plataforma, imposto, frete subsidiado, embalagem, anúncio.

O erro mais comum é precificar olhando só o custo do produto.

## A conta completa de uma venda

Exemplo ilustrativo (percentuais típicos, que **variam** por provedor, regime e contrato):

| Item | Valor |
|---|---|
| Preço de venda | R$ 100,00 |
| Custo do produto | − R$ 40,00 |
| Taxa do provedor de pagamento (≈ 5% no cartão) | − R$ 4,99 |
| Taxa da Shopify por usar provedor de terceiros (2% no plano Basic) | − R$ 2,00 |
| Imposto (Simples Nacional, comércio, faixa inicial: 4%) | − R$ 4,00 |
| Frete grátis bancado pela loja | − R$ 15,00 |
| Embalagem | − R$ 3,00 |
| Anúncio necessário para conseguir essa venda (custo por venda) | − R$ 20,00 |
| **Sobra (margem de contribuição)** | **R$ 11,01 (11%)** |

Olhando só produto e preço, parecia 60% de margem. Na prática, sobram 11 reais — e desse valor ainda saem os custos fixos do mês.

> [!danger] A armadilha
> Se o anúncio subir de R$ 20 para R$ 32 por venda, a loja passa a **pagar para vender**. Crescer em pedidos só aumenta o prejuízo. Por isso a [[17-Metricas-do-Ecommerce|métrica de custo por venda]] precisa ser acompanhada toda semana.

## Formar o preço a partir da margem desejada

Separe o que é **valor fixo por venda** (produto, frete, embalagem, anúncio) do que é **percentual do preço** (taxas e imposto):

```text
preço = custos fixos por venda / (1 − soma dos percentuais − margem desejada)
```

No exemplo, com margem desejada de 20%:

```text
fixos por venda  = 40 + 15 + 3 + 20 = R$ 78,00
percentuais      = 4,99% + 2% + 4% = 10,99%
preço            = 78 / (1 − 0,1099 − 0,20) = 78 / 0,6901 ≈ R$ 113,03
```

Conferência: 10,99% de R$ 113,03 ≈ R$ 12,42; R$ 113,03 − 78 − 12,42 = R$ 22,61, que é 20% do preço. ✔

## Markup não é margem

- **Markup** multiplica o custo: custo R$ 40 × 2,5 = R$ 100.
- **Margem** é o que sobra em relação ao preço.

Markup divisor, rateio do custo fixo e ponto de equilíbrio estão em [[Financas/06-Formacao-de-Preco|formação de preço]] e [[Financas/05-Custos-Margem-e-Ponto-de-Equilibrio|ponto de equilíbrio]], na trilha de finanças.

"Markup 2,5" soa como lucro alto, mas não diz nada sobre taxas, frete e anúncio. Use a conta completa.

## Frete grátis, desconto e parcelamento

Todos saem da margem:

- **Frete grátis** a partir de um valor mínimo (ex.: acima de R$ 199) aumenta o ticket médio sem dar frete em pedido pequeno.
- **Cupom de 10%** num produto com 11% de margem zera o lucro. Calcule antes de anunciar.
- **Parcelamento sem juros** é pago pela loja: o provedor cobra taxa maior por parcela, ou antecipa o recebível com desconto. Veja [[07-Pagamentos-no-Brasil|pagamentos]].

## Perguntas de revisão

Qual a diferença entre custo fixo e custo variável numa loja virtual? :: Custo fixo existe mesmo sem vender, como plano da plataforma e contador; custo variável acontece a cada venda, como produto, taxas, imposto, frete e anúncio.

O que é margem de contribuição? :: É o que sobra de cada venda depois de pagar todos os custos variáveis; é dela que saem os custos fixos e o lucro.

Qual a fórmula para formar o preço a partir da margem desejada? :: Preço = custos fixos por venda / (1 − soma dos percentuais sobre o preço − margem desejada).

Qual a diferença entre markup e margem? :: Markup multiplica o custo para chegar ao preço; margem é o que sobra em relação ao preço depois dos custos. Markup alto não garante margem boa.

Por que um cupom de 10% pode zerar o lucro? :: Porque o desconto sai inteiro da margem; se a margem de contribuição é 11%, um cupom de 10% deixa quase nada.

Quem paga o parcelamento sem juros? :: A loja, por meio de taxa maior do provedor ou do custo de antecipar os recebíveis.

---
Anterior: [[01-Modelos-de-Negocio|Modelos de negócio]] · Próxima: [[03-Plataformas-Comparadas|Plataformas comparadas]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
