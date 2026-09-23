---
tags: [ecommerce, trafego-pago, metricas, rastreamento, lgpd]
cssclasses: [cerebro-nota, cerebro-ecommerce]
---

# Rastreamento e mensuração de anúncios

Anúncio sem medição é gasto no escuro. As estratégias automáticas do [[30-Google-Ads|Google Ads]] e da [[31-Meta-Ads|Meta]] aprendem **com as conversões que você envia**: se a compra não chega, ou chega sem valor, elas otimizam para a coisa errada.

## As peças

| Peça | O que faz |
|---|---|
| **Pixel da Meta** / **tag do Google** | código no navegador que registra eventos: visualização de página, adicionar ao carrinho, iniciar checkout, compra |
| **API de Conversões** (Meta) / **conversões otimizadas** (Google) | enviam os eventos **do servidor**, não só do navegador. Recuperam parte das compras que bloqueadores e restrições de privacidade escondem |
| **Google Analytics 4** | visão de todos os canais juntos, e não só a de cada plataforma de anúncio |
| **UTMs** | etiquetas no link que dizem de onde veio a visita |
| **Pedidos da loja** | a **fonte da verdade**: o que realmente foi vendido e pago |

Na **Shopify**, instale pelos canais oficiais: **Facebook & Instagram** (pixel + API de Conversões) e **Google & YouTube** (tag + conversões). Evite colar código manualmente no tema: duplica eventos e quebra quando o tema muda.

## Os eventos de e-commerce

```text
ViewContent / visualização de produto
  → AddToCart / adicionar ao carrinho
    → InitiateCheckout / iniciar finalização
      → Purchase / compra   ← com valor e moeda (BRL)
```

Confirme com uma **compra de teste** que o evento **Compra** chega **uma vez só** e **com o valor certo**. Evento duplicado dobra o ROAS no painel e engana a estratégia de lance.

## UTMs

Padrão simples para links de redes, e-mail e influenciadores:

```text
https://sualoja.com.br/products/garrafa?utm_source=instagram&utm_medium=bio&utm_campaign=lancamento-garrafa
```

| Parâmetro | Responde | Exemplos |
|---|---|---|
| `utm_source` | de onde | instagram, google, newsletter, influenciador-ana |
| `utm_medium` | que tipo | cpc, bio, email, stories |
| `utm_campaign` | qual ação | black-friday-2026, lancamento-garrafa |

Use sempre **minúsculas** e o mesmo padrão; senão "Instagram" e "instagram" viram duas fontes nos relatórios. O Google Ads e a Meta preenchem UTMs automaticamente se configurados.

## Por que os números não batem

O painel do Google, o da Meta, o GA4 e a Shopify vão mostrar números **diferentes**, e isso é normal:

- **Janela de atribuição:** cada plataforma conta vendas até X dias depois do clique (ou da visualização, no caso da Meta).
- **Contagem dupla:** a pessoa clicou num anúncio do Google e depois num da Meta; **as duas** dizem que a venda foi delas.
- **Visualização sem clique:** a Meta pode atribuir uma venda a quem só **viu** o anúncio.
- **Bloqueios de privacidade** escondem parte das conversões do navegador. É por isso que a API de Conversões existe.

A soma das vendas "atribuídas" pelas plataformas quase sempre passa das vendas reais.

## MER: a métrica que não mente

```text
MER (marketing efficiency ratio) = receita total da loja / gasto total em anúncios (todas as plataformas)
```

Exemplo: R$ 30.000 de receita no mês, R$ 6.000 somando Google e Meta → **MER 5**. Se o gasto sobe para R$ 9.000 e a receita vai só a R$ 32.000, o MER cai para 3,6: os R$ 3.000 extras trouxeram R$ 2.000. Isso é um prejuízo que nenhum painel mostra sozinho.

Use o ROAS de cada plataforma para **decidir dentro dela** (qual criativo, qual campanha) e o MER, comparado com a margem, para decidir **quanto investir no total** ([[17-Metricas-do-Ecommerce|métricas]]).

## Teste de incrementalidade simples

Para saber se um canal ou o remarketing traz venda **nova**:
1. Pause (ou reduza bastante) por 1 a 2 semanas, num período sem datas especiais.
2. Compare a receita **total** com o período anterior equivalente.
3. Se quase nada mudou, o canal estava pegando vendas que viriam de qualquer jeito.

É a mesma ideia da [[27-Trafego-Pago-em-Marketplace|canibalização em marketplace]].

## LGPD e consentimento

- A política de privacidade precisa citar o uso de pixels e ferramentas de anúncio ([[11-Fiscal-e-Legal|fiscal e legal]]).
- Use um **banner de cookies** com opção real de recusar os não essenciais. A Shopify tem configurações de privacidade e consentimento do cliente.
- Listas de clientes enviadas às plataformas (para públicos personalizados) exigem base legal. A Meta e o Google fazem hash dos dados, mas a responsabilidade pelo envio continua sendo da loja.

---
Anterior: [[31-Meta-Ads|Meta Ads]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
