---
tags: [ecommerce, marketplace, integracao, estoque, shopify]
cssclasses: [cerebro-nota, cerebro-ecommerce]
verificado_em: 2026-09-23
---

# Integração multicanal

Vender na loja própria, no Mercado Livre e na Shopee ao mesmo tempo significa **um estoque, vários balcões**. Sem integração, cada venda num canal precisa ser baixada à mão nos outros. Uma hora isso falha, o mesmo item é vendido duas vezes, e o cancelamento no marketplace custa reputação.

## O que precisa ficar centralizado

| Item | Por quê |
|---|---|
| **Estoque** | uma venda em qualquer canal baixa o estoque em todos |
| **Catálogo** (produto, SKU, fotos, descrição) | cadastrar uma vez e publicar em vários canais |
| **Pedidos** | uma fila única de expedição, não três painéis |
| **Nota fiscal** | emitida a partir de qualquer pedido, com os mesmos dados fiscais |
| **Preço por canal** | o mesmo produto pode (e muitas vezes deve) ter preço diferente por canal, por causa das comissões |

## Os caminhos

### 1. Shopify como centro
A Shopify importa pedidos de marketplaces e sincroniza o catálogo por canais de venda e apps de conexão com marketplaces. Pela página de preços (23/09/2026): **até 50 pedidos de marketplace por mês sincronizados grátis**; acima disso, **1%, com limite de US$ 99 por mês**. Veja [[04-Shopify-Visao-Geral|visão geral da Shopify]].

**Bom para:** quem já tem a Shopify como loja principal e poucos canais.

### 2. ERP ou hub de integração como centro
Um sistema de gestão (ERP) como Bling ou Tiny, ou um **hub de integração**, conecta loja própria, marketplaces, emissor de nota fiscal e, às vezes, frete. O estoque "de verdade" mora no ERP, e os canais são alimentados por ele.

**Bom para:** vários marketplaces, volume alto de pedidos e necessidade de nota fiscal em todos os canais.

### 3. Planilha e disciplina
Funciona no começo, com poucos pedidos e um ou dois canais. É o que o [[Cerebro/Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] resolve em pequena escala: um lugar só onde a venda baixa o estoque. Ponto de virada: quando passar a errar estoque ou gastar mais de uma hora por dia sincronizando, é hora do caminho 1 ou 2.

## Cuidados na integração

- **SKU igual em todos os canais.** A integração liga os anúncios pelo SKU. SKU diferente ou repetido = estoque errado. É o mesmo cuidado de [[Cerebro/Praticas/08-Unidades-de-Medida|unidades como regra de negócio]].
- **Kit vs. unidade:** um kit de 3 precisa baixar 3 unidades do item base. Configure a composição do kit no integrador.
- **Estoque de segurança por canal:** anunciar 1 ou 2 unidades a menos do que existe evita vender o que acabou de ser vendido em outro canal, antes da sincronização.
- **Teste com um produto** antes de conectar o catálogo inteiro. Importação e sincronização em massa têm o mesmo risco de [[Cerebro/Praticas/05-Importacao-de-Planilhas|importação de planilhas]]: sobrescrever o item errado.
- **Intervalo de sincronização:** saiba de quanto em quanto tempo o estoque é atualizado. Em datas de pico (11.11, Black Friday), minutos fazem diferença.

## Preço por canal

```text
preço no canal = custos fixos por venda / (1 − comissão do canal − outros % − margem desejada)
```

É a mesma fórmula de [[02-Planejamento-e-Precificacao|precificação]], com a comissão de cada canal. Resultado comum: o mesmo produto custa R$ 99 na loja própria e R$ 109 no marketplace, e não há nada de errado nisso. Lá o tráfego é pago pela comissão; na loja própria, pelo anúncio.

## Com ajuda do Claude

Com o conector da Shopify, o Claude consegue listar pedidos de todos os canais sincronizados, conferir estoque por SKU e apontar divergências, como "quais SKUs estão com estoque zerado mas anúncio ativo?". Mudanças em estoque e preço sempre pedem confirmação.

---
Anterior: [[25-Reputacao-e-Operacao-em-Marketplace|Reputação e operação]] · Próxima: [[27-Trafego-Pago-em-Marketplace|Tráfego pago em marketplace]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
