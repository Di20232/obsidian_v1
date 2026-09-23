---
tags: [github, conceito, banco-de-dados, concorrencia, flashcards]
cssclasses: [cerebro-nota, cerebro-dados]
verificado_em: 2026-09-15
---
# Estoque concorrente — impedir sobrevenda e atualização perdida

## O problema

Duas compras podem ler o mesmo saldo antes de qualquer uma gravar. Se restar uma unidade e ambas decidirem que há estoque, uma simples sequência de leitura, subtração em memória e gravação não protege a regra de negócio.

## Solução encontrada nos seus repositórios

A condição e a alteração acontecem na mesma instrução do banco:

```sql
-- Exemplo conceitual; adaptar nomes e parâmetros ao seu banco.
UPDATE produto
SET estoque = estoque - :quantidade
WHERE id = :id AND estoque >= :quantidade;
```

O número de linhas alteradas decide se a operação conseguiu reservar o saldo. Zero linhas precisa virar falha controlada; não pode ser tratado como venda concluída.

### ByteShop

[[Cerebro/GitHub/byteShop/Fontes/backend/app/routers/orders.py.md|orders.py]] usa SQLAlchemy para atualizar o saldo sob condição e verifica `rowcount`. O pedido e os itens são gravados junto da transação.

### Contro Vend

[[Cerebro/GitHub/contro-vend-public/Fontes/src/stockOps.js.md|stockOps.js]] usa Prisma `updateMany` com `increment` e limites. A leitura do saldo resultante acontece dentro da mesma transação; o movimento registra antes e depois.

## Como testar a regra

- Faça requisições concorrentes contra estoque pequeno em um banco descartável.
- Confira quantas operações foram aceitas, saldo final e extrato.
- Verifique se uma falha no meio de uma venda desfaz toda a transação.
- Teste cancelamentos, entradas e perdas além do caminho de venda.

A presença desse padrão não equivale a certificação de segurança; o comportamento deve ser testado com o banco e a carga do projeto.

[[Cerebro/Mapas/02-Mapa-Dados|Dados]] · [[Cerebro/GitHub/00-Indice|GitHub]]

## Perguntas de revisão

O que é sobrevenda por concorrência? :: Duas compras leem o mesmo saldo antes de gravar e ambas vendem a última unidade.

Como impedir sobrevenda no banco? :: Com UPDATE que subtrai o estoque com a condição estoque >= quantidade na mesma instrução, verificando as linhas alteradas.

O que fazer quando o UPDATE condicional de estoque altera zero linhas? :: Tratar como falha controlada, nunca como venda concluída.

Como testar a regra de estoque concorrente? :: Com requisições simultâneas contra estoque pequeno num banco descartável, conferindo aceitas, saldo final e extrato.
