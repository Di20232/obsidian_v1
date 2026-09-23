---
tags: [ecommerce, frete, logistica, operacao, flashcards]
cssclasses: [cerebro-nota, cerebro-ecommerce]
---

# Frete e logística

Frete caro e prazo longo estão entre os maiores motivos de abandono de carrinho. Frete é **parte do produto**.

## Quem leva o pacote

| Opção | Bom para | Cuidado |
|---|---|---|
| **Correios** (PAC, SEDEX) | cobertura nacional, pacotes pequenos e médios | prazos variam por região; greves |
| **Transportadoras** (Jadlog, Loggi, J&T, Total Express etc.) | capitais e regiões com boa cobertura; às vezes mais baratas | cobertura desigual no interior |
| **Plataformas de frete** (Melhor Envio, Frenet, Intelipost etc.) | cotam várias transportadoras de uma vez, geram etiqueta e rastreio, e costumam ter preço negociado | cada uma tem um app e uma forma própria de integrar com a Shopify |
| **Entrega própria / motoboy** | mesma cidade, entrega no dia | seguro, custo por entrega, rotas |
| **Retirada na loja** | quem tem ponto físico | combinar horário |
| **Fulfillment** (Mercado Livre Full, Amazon, operadores logísticos) | volume: eles armazenam, embalam e enviam | custo de armazenagem; estoque longe de você |

## Como cobrar o frete

| Estratégia | Como funciona | Quando usar |
|---|---|---|
| **Calculado** | o cliente vê o preço real por CEP | padrão honesto; bom com produto de peso variado |
| **Tabela fixa por região** | um valor para Sudeste, outro para Norte etc. | catálogo de peso parecido; simples de configurar |
| **Grátis acima de X** | frete grátis quando o carrinho passa de um valor | aumenta o ticket médio; defina X acima do ticket atual |
| **Grátis sempre** | o frete está embutido no preço | produtos leves e de margem boa |

Na Shopify, o **cálculo em tempo real por transportadora** aparece como recurso do plano Advanced. Nos planos menores, os apps brasileiros de frete oferecem alternativas: confirme com o app escolhido, **antes** de fechar o plano, como ele calcula no seu plano.

## Peso e dimensões

As transportadoras cobram pelo **maior** entre o peso real e o **peso cúbico** (as dimensões da caixa convertidas em peso). Uma caixa grande e leve pode sair cara. Por isso:
- cadastre no produto o peso e as medidas **com a embalagem**;
- tenha poucos tamanhos de caixa padrão e escolha o menor que protege.

## Embalagem

- protege (plástico bolha, papel, caixa firme) e cabe no tamanho padrão;
- identifica: etiqueta com nota fiscal (DANFE simplificado) e rastreio;
- encanta, sem exagero: um cartão de agradecimento com cupom para a próxima compra custa pouco e alimenta a [[16-Email-e-Retencao|recompra]].

## Prazo prometido

```text
prazo exibido = dias para separar e postar + prazo da transportadora
```

Se você posta em até 2 dias úteis e o PAC leva 7, o prazo exibido é 9 dias úteis. Prometer menos e entregar antes gera avaliação boa. Prometer o prazo da transportadora sem somar a separação gera reclamação.

## Rastreio e problemas

- Envie o código de rastreio assim que postar (na Shopify, ao **processar o pedido**, o cliente recebe o e-mail de envio).
- Acompanhe pedidos parados há muitos dias sem movimentação e **avise o cliente antes que ele pergunte**.
- Extravio ou avaria: abra reclamação com a transportadora, mas **resolva com o cliente primeiro** (reenvio ou reembolso). A responsabilidade perante ele é da loja.

## Logística reversa

Devoluções (arrependimento, defeito, troca de tamanho) precisam de um caminho simples: código de postagem reversa dos Correios ou de uma plataforma de frete. No arrependimento dentro de 7 dias, o custo do retorno é da loja (ver [[11-Fiscal-e-Legal|fiscal e legal]]).

## Perguntas de revisão

Como calcular o prazo de entrega exibido ao cliente? :: Dias para separar e postar mais o prazo da transportadora.

O que é peso cúbico? :: É o peso calculado a partir das dimensões da caixa; a transportadora cobra pelo maior entre ele e o peso real.

Como usar o frete grátis sem perder margem? :: Oferecer frete grátis acima de um valor mínimo de pedido, maior que o ticket médio atual.

Quem paga a devolução no direito de arrependimento? :: A loja, que deve devolver tudo, inclusive o frete pago pelo cliente.

Em caso de extravio, o que resolver primeiro? :: Resolver com o cliente, com reenvio ou reembolso, e depois reclamar com a transportadora.

---
Anterior: [[07-Pagamentos-no-Brasil|Pagamentos]] · Próxima: [[09-Gestao-de-Pedidos|Gestão de pedidos]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
