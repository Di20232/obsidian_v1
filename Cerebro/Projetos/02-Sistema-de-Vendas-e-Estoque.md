---
tags: [projeto, requisitos, estoque, vendas, banco-de-dados]
status: requisitos-iniciais
cssclasses: [cerebro-nota, cerebro-projetos]
---

# Sistema de Vendas e Estoque para Pequeno Comércio

> [!projeto] Origem
> Requisitos extraídos de conversa anterior. Esta nota organiza o problema e não afirma que o sistema já foi implementado.

## Problema a resolver

Um pequeno comércio precisa registrar vendas e estoque para reduzir falta de produtos de alta procura, compras excessivas, itens parados e perdas por vencimento ou deterioração. O capital de giro é limitado, então simplicidade e informação útil importam mais que recursos sofisticados.

## Resultado mínimo útil (MVP)

1. cadastrar produtos com custo, preço, quantidade e estoque mínimo;
2. registrar uma venda e reduzir o estoque automaticamente;
3. registrar entrada e ajuste de estoque com motivo;
4. alertar produtos abaixo do mínimo e próximos do vencimento;
5. mostrar produtos mais vendidos, parados e com estoque crítico;
6. manter dados persistentes em banco de dados ou planilha estruturada.

## Perguntas que ainda precisam de resposta

- Há quantas pessoas usando o sistema e quais permissões elas precisam?
- A venda é registrada por item, por pedido ou por integração com caixa?
- Há código de barras, variações, unidades diferentes ou produtos vendidos por peso?
- Como serão registradas perdas, devoluções e compras de fornecedor?
- Qual regra define a previsão de reposição: média de venda, estoque mínimo ou ambas?
- Os dados ficarão em rede, nuvem ou em uma única máquina?

## Modelo inicial de dados

| Entidade | Informações essenciais |
|---|---|
| Produto | nome, código, custo, preço, estoque mínimo, validade opcional |
| Movimento de estoque | produto, tipo, quantidade, data, motivo e responsável |
| Venda | data, itens, total e forma de pagamento |
| Item de venda | venda, produto, quantidade, preço praticado |
| Fornecedor | contato, prazo e produtos fornecidos |

## Próxima decisão recomendada

Validar o fluxo diário com quem vende e repõe produtos antes de escolher tecnologia. Para o MVP, priorize uma tela simples de venda, relatórios de reposição e backups; depois evolua para previsão e integrações.

## Links relacionados

- [[../Mapas/02-Mapa-Dados|Mapa de Dados]]
- [[../Mapas/01-Mapa-Web|Mapa Web]]
- [[../Guias/03-Criar-Projeto|Guia para Criar Projetos]]
