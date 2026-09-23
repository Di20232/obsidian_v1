---
tags: [ecommerce, estoque, compras, dados]
cssclasses: [cerebro-nota, cerebro-ecommerce]
---

# Estoque e compras

Estoque é dinheiro parado em forma de produto. Pouco estoque perde venda; estoque demais trava o caixa.

## Na Shopify

- Ative **rastrear quantidade** em cada variante.
- **Continuar vendendo quando estiver esgotado** fica desligado, a menos que seja pré-venda assumida e avisada na página.
- **Locais:** cada depósito ou loja física é um local com estoque próprio. Os pedidos saem do local definido nas regras de envio.
- **Ajustes** de estoque (perda, avaria, contagem) ficam registrados no histórico da variante. Registre sempre o motivo.
- **Ordens de compra** (na área de Produtos, conforme o plano): registram o que foi pedido ao fornecedor e dão entrada no estoque quando chega.

## Quando repor

A conta básica é a mesma do [[Cerebro/GitHub/Conhecimento/04-Previsao-de-Reposicao|controle de vendas do cofre]]:

```text
média diária de vendas  = vendidos nos últimos 30 dias / 30
dias de cobertura       = estoque atual / média diária
ponto de pedido         = média diária × (prazo do fornecedor + margem de segurança)
```

Exemplo: 60 vendidos em 30 dias → 2 por dia. O fornecedor leva 10 dias e você quer 5 de segurança: ponto de pedido = 2 × 15 = **30 unidades**. Quando o estoque chegar a 30, faça o pedido.

> [!warning] Média zero não é estoque infinito
> Produto sem venda na janela gera média zero e "dias de cobertura" impossível de calcular. Isso não quer dizer que está tudo bem: pode ser produto parado, ou ruptura (não vendeu **porque** faltou).

## Curva ABC

Ordene os produtos pelo faturamento e some até 100%:

| Classe | Parte do faturamento | Em geral | Cuidado |
|---|---|---|---|
| **A** | ~80% | ~20% dos itens | nunca pode faltar; revisar toda semana |
| **B** | ~15% | ~30% dos itens | revisar a cada 15 dias |
| **C** | ~5% | ~50% dos itens | comprar pouco; avaliar se deve continuar no catálogo |

O relatório de vendas por produto da Shopify, exportado para planilha, dá a curva em minutos.

## Giro e produtos parados

```text
giro no período = unidades vendidas / estoque médio
```

Produto sem venda há 60 ou 90 dias é candidato a: kit com um produto campeão, desconto progressivo, brinde acima de um valor, ou saída do catálogo. Parado, ele ocupa espaço e dinheiro.

## Contagem

Faça contagem física periódica, pelo menos da classe A, e ajuste o sistema. Diferença recorrente entre físico e sistema é sintoma de processo: separação errada, devolução não registrada, ou venda em outro canal sem baixa no estoque.

## Vários canais, um estoque

Quem vende na loja e em marketplace precisa de **estoque sincronizado** (integração pela Shopify ou por um ERP). Sem isso, o mesmo item é vendido duas vezes, e o cancelamento no marketplace prejudica a reputação da conta.

---
Anterior: [[09-Gestao-de-Pedidos|Gestão de pedidos]] · Próxima: [[11-Fiscal-e-Legal|Fiscal e legal]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
