---
tags: [financas, precificacao, markup, flashcards]
cssclasses: [cerebro-nota, cerebro-financas]
---

# Formação de preço

Preço bom paga o custo do produto, as despesas variáveis, a parte dos custos fixos e ainda deixa lucro. A conta completa de uma venda está em [[Ecommerce/02-Planejamento-e-Precificacao|planejamento e precificação no e-commerce]]; aqui estão as ferramentas gerais, que servem para qualquer negócio.

## Markup: as duas formas

**Markup multiplicador:** um número que multiplica o custo para chegar ao preço.

```text
preço = custo × markup multiplicador
```

**Markup divisor:** parte dos percentuais que saem do preço, o que é mais correto quando impostos e taxas são percentuais **sobre o preço**.

```text
preço = custo / (1 − soma dos percentuais sobre o preço − margem de lucro desejada)
```

Exemplo: custo de R$ 40; impostos 5%, taxa de cartão 4%, comissão 3%, rateio de custo fixo 15% e margem desejada de 10% (total de 37%):

```text
preço = 40 / (1 − 0,37) = 40 / 0,63 ≈ R$ 63,49
markup multiplicador equivalente = 1 / 0,63 ≈ 1,587
```

Conferência: os 27% de impostos, taxas, comissão e rateio sobre R$ 63,49 somam R$ 17,14; R$ 63,49 − R$ 40 − R$ 17,14 = **R$ 6,35 de lucro**, exatamente 10% do preço. ✔

> [!warning] O erro do "37% em cima do custo"
> Somar os 37% **ao custo** (R$ 40 × 1,37 = R$ 54,80) parece a mesma coisa, mas não é. Os 27% de impostos, taxas e rateio incidem sobre o **preço**: 27% de R$ 54,80 = R$ 14,80. R$ 54,80 − R$ 40 − R$ 14,80 = **R$ 0,00 de lucro**. Os 10% planejados sumiram inteiros.

## Rateio do custo fixo

O percentual de custo fixo no markup vem da proporção entre custos fixos e faturamento:

```text
% de custo fixo = custos fixos do mês / faturamento médio do mês
```

R$ 8.000 de custos fixos com faturamento médio de R$ 50.000 → **16%**. Se o faturamento cair, esse percentual sobe e o preço antigo passa a não cobrir a estrutura. Revise a cada trimestre.

## Preço não é só custo

O custo define o **piso**: abaixo dele, cada venda dá prejuízo. O **teto** vem de fora:
- **concorrência:** quanto cobram pelo mesmo produto, com o mesmo prazo e serviço?
- **valor percebido:** marca, atendimento, garantia, entrega rápida justificam cobrar acima;
- **canal:** o mesmo produto pode ter preços diferentes em loja própria e marketplace, porque as taxas são diferentes ([[Ecommerce/26-Integracao-Multicanal|preço por canal]]).

Se o preço de mercado fica **abaixo** do piso, o problema não é o preço: é custo alto, estrutura pesada ou produto errado para o canal.

## Descontos e promoções

Um desconto sai **inteiro** da margem. Com margem de lucro de 10%, um desconto de 10% zera o lucro daquela venda. Antes de anunciar:

```text
aumento de vendas necessário para manter o lucro = margem / (margem − desconto) − 1
```

Com margem de contribuição de 35% e desconto de 10%: 0,35 / 0,25 − 1 = **40% a mais de vendas** só para empatar com o lucro de antes.

## Perguntas de revisão

Qual a diferença entre markup multiplicador e divisor? :: O multiplicador multiplica o custo; o divisor divide o custo por (1 menos os percentuais sobre o preço e a margem), o que trata corretamente impostos e taxas sobre o preço.

Qual a fórmula do preço pelo markup divisor? :: Preço = custo / (1 − soma dos percentuais sobre o preço − margem de lucro desejada).

Por que somar os percentuais ao custo dá um preço errado? :: Porque impostos e taxas incidem sobre o preço, que é maior que o custo; o valor somado fica menor que o necessário.

Como calcular o percentual de custo fixo no preço? :: Dividindo os custos fixos do mês pelo faturamento médio do mês.

Com margem de contribuição de 35%, quanto é preciso vender a mais para compensar um desconto de 10%? :: Cerca de 40% a mais: 0,35 dividido por 0,25, menos 1.

O que define o piso e o teto do preço? :: O custo define o piso; concorrência, valor percebido e canal definem o teto.

---
Anterior: [[05-Custos-Margem-e-Ponto-de-Equilibrio|Ponto de equilíbrio]] · Próxima: [[07-Capital-de-Giro-e-Ciclo-Financeiro|Capital de giro]] · Trilha: [[Financas/00-Indice|Finanças]]
