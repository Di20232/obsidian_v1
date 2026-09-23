---
tags: [financas, credito, juros, emprestimos, flashcards]
cssclasses: [cerebro-nota, cerebro-financas]
---

# Crédito, juros e empréstimos

Crédito é ferramenta: bem usado, financia estoque para uma data forte ou um equipamento que aumenta a produção. Mal usado, paga prejuízo com juros e transforma um mês ruim num ano ruim.

## Juros compostos

No Brasil, praticamente todo crédito usa **juros compostos**: os juros de cada mês incidem sobre o saldo que já inclui os juros anteriores.

```text
montante = valor inicial × (1 + taxa mensal) ^ meses
```

R$ 10.000 a **3% ao mês** por 12 meses, sem pagar nada no meio:

```text
10.000 × 1,03^12 ≈ R$ 14.257,61
```

### Taxa mensal e anual

Taxas mensais parecem pequenas. Converta sempre para o ano:

```text
taxa anual = (1 + taxa mensal) ^ 12 − 1
```

| Taxa ao mês | Equivale ao ano |
|---|---|
| 2,5% | ~34,5% |
| 3% | ~42,6% |
| 8% (comum em cheque especial e rotativo) | ~152% |

## Empréstimo parcelado (tabela Price)

Nas parcelas fixas, a parcela é:

```text
parcela = valor × taxa / (1 − (1 + taxa) ^ −meses)
```

R$ 10.000 a 3% ao mês em 12 parcelas: **R$ 1.004,62 por mês**, total de **R$ 12.055,45**, ou seja, **R$ 2.055,45 de juros**.

## CET: o número que importa

A taxa de juros anunciada não é o custo total. O **CET** (Custo Efetivo Total) inclui juros, tarifas, seguros e impostos (como o IOF) e é informado pelo banco antes da contratação. **Compare propostas pelo CET**, nunca só pela taxa de juros.

## Tipos de crédito, do mais barato ao mais caro (em geral)

| Tipo | Uso adequado | Cuidado |
|---|---|---|
| **Linhas com garantia pública ou programas para pequenas empresas** (como o Pronampe) | capital de giro e investimento | condições mudam a cada edição; consulte o banco e o Sebrae |
| **Capital de giro com prazo** | reforçar o caixa de forma planejada | compare o CET entre bancos e cooperativas |
| **Antecipação de recebíveis** | aperto pontual ([[08-Recebiveis-e-Antecipacao\|custo]]) | não usar como solução permanente |
| **Cheque especial e rotativo do cartão** | só emergência de poucos dias | entre os créditos mais caros do mercado |

Cooperativas de crédito costumam ter condições competitivas para pequenas empresas.

## Antes de pegar dinheiro emprestado

1. **Para que é?** Crédito para **gerar receita** (estoque de uma data forte, máquina) pode se pagar. Crédito para **cobrir prejuízo recorrente** só adia o problema e soma juros.
2. **A operação paga a parcela?** A parcela precisa caber na [[05-Custos-Margem-e-Ponto-de-Equilibrio|margem de contribuição]] do que o dinheiro vai gerar, com folga.
3. **O fluxo de caixa aguenta?** Lance as parcelas no [[03-Fluxo-de-Caixa|fluxo projetado]] e veja o saldo mínimo dos próximos meses.
4. **Qual o CET?** Compare pelo menos três propostas.
5. **E se as vendas caírem 20%?** Refaça a conta no cenário ruim.

> [!warning] O sinal vermelho
> Pegar empréstimo novo para pagar parcela de empréstimo antigo, ou usar cheque especial todo mês, indica que o problema é de **margem ou estrutura**, não de crédito. Olhe a [[04-DRE-Simplificada|DRE]] antes de assinar qualquer coisa.

## Perguntas de revisão

Como funcionam os juros compostos? :: Os juros de cada período incidem sobre o saldo que já inclui os juros anteriores: montante = valor × (1 + taxa) elevado ao número de períodos.

Como converter uma taxa mensal em anual? :: Taxa anual = (1 + taxa mensal) elevado a 12, menos 1.

A quanto equivalem 3% ao mês num ano? :: A cerca de 42,6% ao ano.

Qual a parcela de R$ 10.000 a 3% ao mês em 12 vezes? :: Cerca de R$ 1.004,62, totalizando R$ 12.055,45.

O que é CET? :: O Custo Efetivo Total, que soma juros, tarifas, seguros e impostos; é o número para comparar propostas de crédito.

Quando um empréstimo faz sentido para a empresa? :: Quando financia algo que gera receita capaz de pagar a parcela com folga, e não para cobrir prejuízo recorrente.

Qual o sinal de que o problema não é falta de crédito? :: Precisar de empréstimo novo para pagar o antigo ou usar cheque especial todo mês, o que indica problema de margem ou estrutura.

---
Anterior: [[10-Impostos-MEI-Simples-e-Reforma|Impostos]] · Próxima: [[12-Indicadores-Financeiros|Indicadores]] · Trilha: [[Financas/00-Indice|Finanças]]
