---
tags: [financas, fluxo-de-caixa, planilha, flashcards]
cssclasses: [cerebro-nota, cerebro-financas]
---

# Fluxo de caixa

O **fluxo de caixa** é o registro de todo dinheiro que entra e sai da empresa, com data. Ele tem duas funções:
- **realizado:** o que já aconteceu, conferido com o extrato bancário;
- **projetado:** o que vai acontecer nas próximas semanas e meses, para enxergar o aperto **antes** que ele chegue.

## A estrutura mínima

Uma planilha resolve. Uma linha por movimento:

| Data | Descrição | Categoria | Entrada | Saída | Saldo | Status |
|---|---|---|---|---|---|---|
| 01/10 | Saldo inicial | — | | | 8.000 | realizado |
| 03/10 | Vendas Pix | Vendas | 2.300 | | 10.300 | realizado |
| 05/10 | Aluguel | Fixo | | 3.000 | 7.300 | realizado |
| 10/10 | Fornecedor A | Mercadoria | | 6.500 | 800 | previsto |
| 15/10 | Recebíveis cartão | Vendas | 4.200 | | 5.000 | previsto |

O saldo de cada linha = saldo anterior + entrada − saída. A linha de 10/10 mostra o valor do fluxo: **o saldo vai cair para R$ 800** cinco dias antes do dinheiro do cartão entrar. Dá tempo de negociar o prazo do fornecedor, antecipar um recebível ou segurar uma compra.

## Categorias úteis

- **Entradas:** vendas à vista (Pix, dinheiro, débito), recebíveis de cartão, boletos recebidos, outras.
- **Saídas variáveis:** mercadoria, frete, taxas de cartão e plataforma, comissões, impostos sobre vendas.
- **Saídas fixas:** aluguel, pró-labore, salários e encargos, contador, sistemas, internet, energia.
- **Saídas de investimento:** equipamento, reforma.
- **Financiamento:** empréstimo recebido (entrada), parcelas pagas (saída).
- **Retiradas do sócio**, separadas das despesas ([[01-Separar-Pessoa-Fisica-e-Empresa|por quê]]).

Categorizar permite responder perguntas como "quanto gastei em frete este mês?" sem abrir extrato por extrato.

## Projetar para frente

1. Lance **todas as contas a pagar** já conhecidas, com a data de vencimento ([[09-Contas-a-Pagar-e-Fornecedores|contas a pagar]]).
2. Lance os **recebíveis** já garantidos, como parcelas de cartão ([[08-Recebiveis-e-Antecipacao|recebíveis]]).
3. Estime as **vendas** futuras com base na média dos últimos meses, de forma conservadora.
4. Olhe o **menor saldo** de cada semana nas próximas 4 a 12 semanas.

> [!warning] O saldo mínimo é o número que importa
> Não é o saldo do fim do mês que quebra a empresa, é o **pior dia** do mês. Um mês que termina positivo pode ter ficado negativo no dia 10, e aí vêm cheque especial, juros e boletos atrasados.

## Conciliação

Toda semana, confira o fluxo **realizado** contra o **extrato bancário**. Diferença que não fecha é lançamento esquecido, taxa não prevista ou erro de digitação. Sem conciliação, a planilha deixa de ser confiável em poucas semanas.

## Perguntas de revisão

O que é o fluxo de caixa? :: O registro com data de todo dinheiro que entra e sai da empresa, realizado e projetado.

Para que serve projetar o fluxo de caixa? :: Para enxergar com antecedência os dias de saldo baixo e agir antes, negociando prazos ou segurando compras.

Por que olhar o saldo mínimo e não o saldo do fim do mês? :: Porque o mês pode fechar positivo e ter ficado negativo num dia intermediário, gerando juros e atrasos.

O que é conciliação bancária? :: Conferir o fluxo realizado contra o extrato do banco para achar lançamentos esquecidos, taxas e erros.

Por que categorizar as entradas e saídas? :: Para saber quanto vai para cada tipo de gasto sem abrir extrato por extrato.

---
Anterior: [[02-Regime-de-Caixa-e-Competencia|Caixa e competência]] · Próxima: [[04-DRE-Simplificada|DRE simplificada]] · Trilha: [[Financas/00-Indice|Finanças]]
