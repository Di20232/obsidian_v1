---
tags: [ecommerce, pagamentos, pix, seguranca, flashcards]
cssclasses: [cerebro-nota, cerebro-ecommerce]
verificado_em: 2026-09-23
---

# Pagamentos no Brasil

## As formas de pagamento

| Forma | Confirmação | Custo típico para a loja | Observação |
|---|---|---|---|
| **Pix** | instantânea | o menor entre os meios eletrônicos | ótimo para oferecer desconto à vista; o QR code expira |
| **Cartão de crédito** | em segundos (aprovação) | o maior, e cresce com o parcelamento | o brasileiro espera parcelar; permite estorno (chargeback) |
| **Boleto** | 1 a 3 dias úteis após o pagamento | tarifa fixa por boleto pago | muitos boletos gerados nunca são pagos; reserva estoque à toa |
| **Carteiras digitais** | instantânea | varia | Mercado Pago, PicPay, Google Pay, Apple Pay, conforme o provedor |

## Na Shopify

O **Shopify Payments não opera no Brasil**. A loja usa um **provedor de terceiros** instalado em **Configurações → Pagamentos**. Exemplos comuns no mercado brasileiro: Mercado Pago, Pagar.me e PagBank. Confira no painel quais estão disponíveis e compatíveis com o seu plano.

Cada venda paga duas taxas:
1. a do **provedor** (percentual + às vezes valor fixo, diferente para Pix, cartão à vista e parcelado);
2. a da **Shopify** por usar provedor de terceiros: 2% no Basic, 1% no Grow, 0,6% no Advanced (ver [[04-Shopify-Visao-Geral|visão geral]]).

Ao comparar provedores, pergunte:
- taxa de Pix, de cartão à vista e de cartão parcelado (por número de parcelas);
- **prazo de recebimento** do cartão (D+2? D+30? cada parcela no seu mês?) e custo da antecipação;
- antifraude incluso? quem paga o chargeback?
- Pix e boleto aparecem dentro do checkout da Shopify, ou o cliente é redirecionado?

## Parcelamento sem juros

"Até 6x sem juros" significa que **a loja paga os juros**. O provedor cobra taxa maior ou você recebe cada parcela no seu mês. Se quiser o dinheiro todo agora, paga pela antecipação. Coloque esse custo na [[02-Planejamento-e-Precificacao|conta de preço]]. Uma estratégia comum é parcelar sem juros só acima de um valor mínimo.

## Desconto no Pix

Dar 5% a 10% de desconto no Pix costuma compensar, porque a taxa é menor, o dinheiro entra na hora e não há chargeback. Informe o desconto já na página do produto: "R$ 94,90 no Pix".

## Fraude e chargeback

**Chargeback** é quando o titular do cartão contesta a compra no banco (fraude com cartão roubado, ou "não reconheço"). O valor é devolvido ao titular e, em geral, **a loja perde o dinheiro e o produto**.

Sinais de pedido suspeito:
- endereço de entrega diferente do de cobrança, em outra região;
- vários cartões tentados em sequência no mesmo pedido;
- pedido alto de cliente novo, com produtos fáceis de revender;
- e-mail aleatório, telefone que não confere;
- pedido de envio urgente ou pedido de alteração de endereço depois do pagamento.

Na Shopify, a **análise de fraude** aparece em cada pedido. Em pedido suspeito: segure o envio, confirme por telefone e, se não houver resposta, cancele e reembolse **antes** de enviar.

> [!seguranca] Nunca
> Nunca peça ou anote o número do cartão por WhatsApp ou e-mail, nem "passe o cartão manualmente" para o cliente. Isso fere as regras das bandeiras de cartão (padrão PCI) e deixa a loja responsável por qualquer vazamento. O pagamento acontece só no checkout.

## Reembolso

Reembolse pelo **próprio pedido** na Shopify (**Pedidos → pedido → Reembolsar**): o valor volta pelo mesmo meio de pagamento e fica registrado. Pix pode exigir devolução pelo provedor. A taxa do provedor normalmente **não** é devolvida à loja.

## Perguntas de revisão

Por que dar desconto no Pix costuma compensar? :: Porque a taxa é menor, o dinheiro entra na hora e não existe chargeback.

O que é chargeback? :: É a contestação da compra pelo titular do cartão junto ao banco; o valor volta para ele e a loja costuma perder o dinheiro e o produto.

Cite três sinais de pedido suspeito de fraude. :: Endereço de entrega diferente do de cobrança em outra região, vários cartões tentados em sequência e pedido alto de cliente novo com produtos fáceis de revender.

O que fazer com um pedido suspeito? :: Segurar o envio, confirmar por telefone e, sem resposta, cancelar e reembolsar antes de enviar.

Qual a diferença entre pagamento autorizado e pago? :: Autorizado reserva o valor no cartão; pago significa que o valor foi capturado. Autorização não capturada expira e a venda some.

Por que nunca anotar número de cartão por WhatsApp ou e-mail? :: Porque viola as regras das bandeiras (PCI) e deixa a loja responsável por qualquer vazamento.

---
Anterior: [[06-Shopify-Produtos-e-Colecoes|Produtos e coleções]] · Próxima: [[08-Frete-e-Logistica|Frete e logística]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
