---
tags: [ecommerce, trafego-pago, tiktok-ads, anuncios, redes-sociais, flashcards]
cssclasses: [cerebro-nota, cerebro-ecommerce]
verificado_em: 2026-09-23
fonte: https://ads.tiktok.com/resources/help
---

# TikTok Ads

O TikTok Ads Manager mostra anúncios em vídeo no feed "Para Você", na busca e na aba Shop do TikTok. Como na [[31-Meta-Ads|Meta]], a pessoa não estava procurando o seu produto: o anúncio **cria demanda**. A diferença é que no TikTok o anúncio precisa **parecer um vídeo do TikTok**. Comercial polido é pulado em um segundo.

Esta nota trata de levar vendas para a **loja própria** (Shopify, Nuvemshop etc.). Vender **dentro** do TikTok, pela TikTok Shop, está em [[34-TikTok-Shop-Ads-e-GMV-Max|TikTok Shop Ads e GMV Max]].

## Estrutura

```text
Campanha        → objetivo
 └─ Grupo       → público, posicionamento, orçamento, lance, evento a otimizar
     └─ Anúncio → vídeo (ou Spark Ad), texto, link
```

## Objetivos

Pela central de ajuda (23/09/2026):

| Etapa | Objetivo | Na loja virtual |
|---|---|---|
| Reconhecimento | **Alcance** | marca nova; não espere venda direta |
| Consideração | **Tráfego**, **Visualizações de vídeo**, **Interação com a comunidade** | aquecer público e ganhar seguidores; tráfego barato raramente compra |
| Ação | **Promoção do app**, **Geração de leads** | lista de espera, cadastros |
| Ação | **Vendas**: site, catálogo ou TikTok Shop | **o objetivo padrão para vender** |

## Antes de começar

1. **Pixel do TikTok + API de Eventos**, que manda os eventos pelo servidor. Na Shopify, Nuvemshop e Loja Integrada, instale pelo **app oficial do TikTok**: a central de ajuda tem guias de integração para essas plataformas. Confirme com uma compra de teste que o evento **Compra** chega uma vez só e com valor. Veja [[32-Rastreamento-e-Mensuracao|rastreamento]].
2. **Catálogo** conectado, para anúncios de catálogo e para o Smart+.
3. **Verificação de negócios:** a central de ajuda trata a verificação da empresa como obrigatória. Confira os documentos pedidos antes de planejar a data de estreia.

## Orçamento: o TikTok pede mais do que parece

As práticas recomendadas oficiais (atualizadas em agosto de 2026) sugerem, para o **orçamento diário do grupo de anúncios**:

| Otimização | Orçamento diário recomendado | Sem histórico de CPA |
|---|---|---|
| Eventos de topo do funil (visualização de página etc.) | 50 × CPA atual | US$ 100 ou equivalente |
| **Conversões profundas** (adicionar ao carrinho, **compra**) | **10 × CPA atual** | **US$ 200** ou equivalente |

> [!warning] Faça a conta antes
> Com custo por compra de R$ 30, a recomendação é **R$ 300 por dia** num grupo otimizando para compra. Com R$ 50 por dia, a campanha fica instável. Para orçamentos pequenos:
> - **um** grupo só, concentrando o dinheiro;
> - otimizar para um evento mais frequente (adicionar ao carrinho) enquanto junta dados;
> - usar **Spark Ads** de vídeos que já funcionaram no orgânico, que custam menos para aprender.

Outras regras oficiais:
- use **orçamento diário** no grupo, não vitalício, e deixe o orçamento da campanha **em aberto** no início;
- depois da fase de aprendizado, mude o orçamento em **no máximo 50%** de cada vez;
- espere **pelo menos 2 dias** entre mudanças de público, lance ou orçamento.

## Fase de aprendizado

Pela central de ajuda (junho de 2026): o desempenho oscila enquanto o sistema aprende, e **costuma estabilizar depois de cerca de 25 resultados ou 7 dias**. Durante essa fase, evite:
- **pausar** a campanha ou o grupo;
- edições que reiniciam o aprendizado;
- orçamento ou quantidade de criativos fora de proporção.

É mais curto que o da Meta (~50 resultados por semana), mas o princípio é o mesmo: **não mexer** nos primeiros dias.

## Smart+: a automação do TikTok

As campanhas **Smart+** automatizam público, criativos e lances. As práticas recomendadas oficiais para Smart+ na web:
- **pixel + API de Eventos** configurados, e catálogo para anúncios Smart+ de catálogo;
- **pelo menos 6 criativos** na criação; a campanha escolhe quais usar;
- **pelo menos 7 dias** no ar, sem edições significativas;
- com meta de **CPA** ou **ROAS mínimo**: orçamento diário da campanha de **30 × CPA histórico** (mínimo **10 ×**);
- depois dos 7 dias, ajuste o lance **em até 15% a cada 2 dias**;
- se a campanha gasta **90% ou mais** do orçamento todo dia e está boa, aumente o orçamento **em até 30%**;
- se usa atribuição **view-through** (quem só viu) e não gasta o orçamento, tente desligá-la.

O ROAS mínimo sai da sua margem: 1 / margem antes do anúncio ([[17-Metricas-do-Ecommerce|métricas]]).

## Spark Ads: o formato que mais combina com o TikTok

Spark Ads transformam uma **postagem orgânica** em anúncio:
- da **sua conta**, ou de **criadores**, com autorização deles por um código com prazo configurável;
- curtidas, comentários, seguidores e compartilhamentos ficam na **postagem original**, então o anúncio também fortalece o perfil;
- funcionam em todos os objetivos de leilão, inclusive **Vendas**;
- vídeos de até **10 minutos**; até 10.000 Spark Ads por conta.

Fluxo que funciona: publique no orgânico → veja qual vídeo prende a atenção e gera comentários → impulsione esse como Spark Ad. Com criadores e afiliados, combine o uso do vídeo em anúncio **por escrito**, com prazo ([[15-Redes-Sociais-e-Trafego-Pago|influenciadores]]).

## Criativo no TikTok

- **Gancho nos 2 primeiros segundos:** uma pergunta, um problema, o resultado primeiro.
- **Vertical 9:16**, com som, legenda e cara de celular. Bastidores, demonstração, "testei e…", resposta a comentário.
- **Pessoas** falando com a câmera costumam render mais que produto sozinho.
- **Trocar criativos com frequência:** no TikTok, a fadiga chega mais rápido que em outras redes.
- O **Creative Center** do TikTok mostra anúncios e tendências em alta por país e categoria, uma boa fonte de referência.
- **Teste A/B** nativo do Ads Manager: segmentação, posicionamento, lance, orçamento, criativo, catálogo ou Smart+, com o público dividido em dois grupos iguais.

## Rotina

- [ ] **Diária:** gasto dentro do previsto; anúncio reprovado?
- [ ] **A cada 2 ou 3 dias** (nunca antes de 2 dias): ajustes pequenos de lance e orçamento, dentro dos limites acima
- [ ] **Semanal:** custo por compra e ROAS comparados com o mínimo; 1 ou 2 criativos novos; quais vídeos orgânicos viram Spark Ads
- [ ] **Mensal:** receita total contra gasto total ([[32-Rastreamento-e-Mensuracao|MER]])

## Perguntas de revisão

Qual o orçamento diário recomendado pelo TikTok para otimizar por compra? :: 10 vezes o CPA atual, ou US$ 200 se ainda não houver histórico.

Quando a fase de aprendizado do TikTok costuma estabilizar? :: Depois de cerca de 25 resultados ou 7 dias.

Quanto tempo esperar entre mudanças numa campanha do TikTok? :: Pelo menos 2 dias, mudando o orçamento em no máximo 50%.

O que são Spark Ads? :: Anúncios feitos a partir de postagens orgânicas, da sua conta ou de criadores com autorização, cujo engajamento fica na postagem original.

Quantos criativos o Smart+ recomenda na criação? :: Pelo menos seis.

Em quanto ajustar o lance do Smart+ depois dos primeiros 7 dias? :: Até 15% a cada 2 dias.

---
Anterior: [[32-Rastreamento-e-Mensuracao|Rastreamento e mensuração]] · Próxima: [[34-TikTok-Shop-Ads-e-GMV-Max|TikTok Shop Ads e GMV Max]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
