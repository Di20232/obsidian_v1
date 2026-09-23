---
tags: [ecommerce, plataformas, shopify, decisao]
cssclasses: [cerebro-nota, cerebro-ecommerce]
---

# Plataformas de e-commerce comparadas

Não existe plataforma "melhor". Existe a que combina com o seu momento, seu orçamento e quanto você quer mexer em tecnologia.

## Os três caminhos

| Caminho | Exemplos | Você cuida de | Serve quando |
|---|---|---|---|
| **Plataforma pronta (SaaS)** | Shopify, Nuvemshop, Tray, Loja Integrada | produtos, visual, operação | quer vender logo, sem manter servidor |
| **Código aberto hospedado por você** | WooCommerce (WordPress), Magento/Adobe Commerce | tudo acima + hospedagem, atualizações, segurança, backup | já conhece WordPress ou precisa de algo muito específico |
| **Código próprio** | um sistema como o [[Cerebro/GitHub/byteShop/01-Arquitetura-e-Aprendizados\|byteShop]] (FastAPI + React) | absolutamente tudo, inclusive segurança de pagamento | a loja é o produto, ou para aprender |

## Critérios para comparar

1. **Custo total por mês**, não só o plano: plano + apps + taxa sobre cada venda + tema pago.
2. **Pagamentos brasileiros:** Pix, boleto, parcelamento, e quanto a plataforma cobra por venda com provedor de terceiros.
3. **Frete:** integração com Correios e transportadoras e cálculo no carrinho.
4. **Nota fiscal:** integração com emissor de NF-e ou ERP (Bling, Tiny etc.).
5. **Marketplaces:** consegue anunciar e receber pedidos do Mercado Livre, Shopee e outros no mesmo painel?
6. **Suporte em português** e comunidade de parceiros no Brasil.
7. **Saída:** se um dia mudar, consegue exportar produtos, clientes e pedidos?

## Shopify vs. plataformas nacionais

| | Shopify | Plataformas nacionais (ex.: Nuvemshop, Tray) |
|---|---|---|
| Cobrança do plano | em **dólar** (sujeita a câmbio e IOF no cartão) | em real |
| Pagamento | Shopify Payments **não** opera no Brasil → provedor de terceiros + taxa adicional por venda | meios de pagamento nacionais integrados de fábrica |
| Ecossistema | o maior do mundo em temas e apps; recursos novos chegam primeiro | apps focados no Brasil (frete, NF-e, Pix) |
| Venda internacional | forte (idiomas, moedas, Markets) | foco no mercado brasileiro |

Os detalhes da Shopify estão em [[04-Shopify-Visao-Geral|Shopify: visão geral]].

> [!tip] Como decidir sem se arrepender
> Monte uma planilha com **o mesmo cenário** (ex.: 100 pedidos de R$ 120 por mês) e calcule o custo total em cada plataforma, incluindo taxa sobre venda e os apps que você realmente vai precisar. A diferença costuma aparecer nas taxas por venda, não no preço do plano.

## Quando código próprio faz sentido

Quase nunca para **vender** no começo: pagamento, antifraude, frete, nota fiscal e segurança já vêm prontos numa plataforma. Faz sentido para aprender (como no byteShop) ou quando o modelo de negócio não cabe em nenhuma plataforma. O [[Cerebro/Projetos/04-Planejamento-de-E-commerce|planejamento técnico]] registra a ordem segura para construir.

---
Anterior: [[02-Planejamento-e-Precificacao|Planejamento e precificação]] · Próxima: [[04-Shopify-Visao-Geral|Shopify: visão geral]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
