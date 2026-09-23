---
tags: [ecommerce, operacao, pedidos, shopify, flashcards]
cssclasses: [cerebro-nota, cerebro-ecommerce]
---

# Gestão de pedidos

## O ciclo de vida de um pedido

```text
checkout concluído
   → pagamento pendente (boleto/Pix aguardando) ── expirou → cancelar e liberar estoque
   → pago
      → análise (fraude? endereço completo? estoque real?)
         → separação e embalagem
            → nota fiscal emitida
               → etiqueta gerada e postado → pedido processado + rastreio enviado ao cliente
                  → em trânsito → entregue
                     → pós-venda (avaliação, recompra)
                     → troca / devolução / reembolso, se houver
```

## Os status na Shopify

A Shopify separa dois eixos em cada pedido:

| Eixo | Status principais | Significado |
|---|---|---|
| **Pagamento** | Pendente · Autorizado · Pago · Parcialmente reembolsado · Reembolsado · Anulado | a situação do dinheiro |
| **Processamento** | Não processado · Parcialmente processado · Processado | a situação do envio |

A fila de trabalho do dia é: **Pago + Não processado**. Crie essa visualização salva na lista de pedidos.

> [!tip] Pagamento "autorizado" não é "pago"
> Alguns provedores apenas **autorizam** o cartão e deixam a **captura** do valor para depois (manual ou automática). Se a captura for manual e esquecida, a autorização expira e a venda some. Confira em **Configurações → Pagamentos** como está a captura.

## Rotina de expedição

1. Filtrar **pagos e não processados**, do mais antigo para o mais novo.
2. Verificar a **análise de fraude** e o endereço (número, complemento, CEP que bate com a cidade).
3. Separar pelo **SKU**, não pela descrição, para evitar trocar tamanho ou cor.
4. Emitir a nota fiscal (app ou ERP).
5. Gerar a etiqueta e postar.
6. **Processar** o pedido na Shopify com o código de rastreio. O cliente recebe o e-mail de envio.

Defina um prazo interno, por exemplo "pedido pago até 12h sai no mesmo dia", e cumpra.

## Cancelamento

Cancele quando: o boleto ou Pix expirou; houver suspeita de fraude sem confirmação; o produto estiver sem estoque de verdade; o cliente pedir antes do envio.

Ao cancelar na Shopify, escolha **reembolsar** e **repor o estoque**. Registre o motivo e avise o cliente com uma mensagem humana, não só o e-mail automático.

## Trocas e devoluções

| Caso | Prazo legal | Quem paga o frete de volta |
|---|---|---|
| **Arrependimento** (compra fora do estabelecimento) | 7 dias a partir do recebimento | a loja; devolução integral, inclusive o frete pago |
| **Defeito** | 30 dias (não duráveis) ou 90 dias (duráveis) para reclamar | a loja |
| **Troca por gosto** (tamanho, cor) fora do arrependimento | não é obrigatória por lei; vale a sua política | como a sua política definir |

Na Shopify, use **Devolução** no pedido para registrar o item voltando, o reembolso ou a troca, e a reposição de estoque. Assim relatório e estoque continuam certos.

## Pedido manual (rascunho)

Venda feita pelo WhatsApp ou no balcão? Crie um **pedido preliminar** (rascunho) na Shopify e envie o link de pagamento ao cliente. Tudo fica no mesmo histórico, com estoque e relatórios corretos.

## O que medir

- tempo entre **pago** e **postado**;
- porcentagem de pedidos com problema (atraso, extravio, troca);
- motivos de devolução, que apontam problemas de descrição, foto ou tabela de medidas.

Mais em [[17-Metricas-do-Ecommerce|métricas]] e na [[19-Rotina-de-Gestao-da-Loja|rotina de gestão]].

## Perguntas de revisão

Quais são os dois eixos de status de um pedido na Shopify? :: Pagamento (pendente, pago, reembolsado etc.) e processamento (não processado, processado).

Qual é a fila de trabalho diária de expedição? :: Pedidos pagos e ainda não processados, do mais antigo para o mais novo.

Por que separar pedidos pelo SKU e não pela descrição? :: Para evitar trocar tamanho ou cor na hora de embalar.

Quais os prazos legais para reclamar de defeito? :: 30 dias para produto não durável e 90 dias para produto durável.

Como registrar uma venda feita pelo WhatsApp na Shopify? :: Criando um pedido preliminar e enviando o link de pagamento, para manter estoque e relatórios corretos.

---
Anterior: [[08-Frete-e-Logistica|Frete e logística]] · Próxima: [[10-Estoque-e-Compras|Estoque e compras]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
