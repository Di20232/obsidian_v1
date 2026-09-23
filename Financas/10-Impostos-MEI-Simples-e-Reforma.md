---
tags: [financas, impostos, mei, simples-nacional, reforma-tributaria, flashcards]
cssclasses: [cerebro-nota, cerebro-financas]
verificado_em: 2026-09-23
fonte: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
---

# Impostos: MEI, Simples Nacional e reforma tributária

> [!warning] Confirme com o contador
> Esta nota explica como o sistema funciona e mostra as contas. O enquadramento certo, as atividades permitidas e as obrigações do seu caso são decisão do contador. Os números foram conferidos em 23/09/2026 na Lei Complementar 123/2006, na Lei Complementar 214/2025 e no portal gov.br.

## MEI (Microempreendedor Individual)

Pelo portal gov.br (23/09/2026), para ser MEI é preciso:
- faturar até **R$ 81.000 por ano** (R$ 251.600 para o transportador autônomo de cargas);
- exercer uma atividade da **lista de ocupações permitidas**;
- ter **no máximo um empregado**, recebendo o salário mínimo ou o piso da categoria;
- não ser sócio, titular ou administrador de outra empresa, nem ter filial.

Quem abre o MEI depois de janeiro tem o limite **proporcional** aos meses de atividade no ano.

O MEI paga um valor **fixo mensal** (o DAS-MEI), que muda com o salário mínimo e conforme a atividade (comércio, indústria ou serviço). Confira o valor do ano no Portal do Empreendedor.

> [!tip] Acompanhe o faturamento do MEI todo mês
> Estourar o limite desenquadra o MEI e pode gerar imposto retroativo. Some o faturamento a cada mês e, ao se aproximar do teto, planeje a migração para microempresa no Simples Nacional com o contador.

## Simples Nacional

Regime para micro e pequenas empresas com faturamento de até **R$ 4,8 milhões por ano**. Vários tributos são pagos numa guia única, o **DAS**. As alíquotas estão em **anexos** conforme a atividade: comércio no Anexo I, indústria no Anexo II e serviços nos Anexos III, IV e V.

### Anexo I (comércio), conforme a LC 123

| Faixa | Receita bruta em 12 meses | Alíquota nominal | Parcela a deduzir |
|---|---|---|---|
| 1ª | até R$ 180.000 | 4,00% | — |
| 2ª | R$ 180.000,01 a R$ 360.000 | 7,30% | R$ 5.940 |
| 3ª | R$ 360.000,01 a R$ 720.000 | 9,50% | R$ 13.860 |
| 4ª | R$ 720.000,01 a R$ 1.800.000 | 10,70% | R$ 22.500 |
| 5ª | R$ 1.800.000,01 a R$ 3.600.000 | 14,30% | R$ 87.300 |
| 6ª | R$ 3.600.000,01 a R$ 4.800.000 | 19,00% | R$ 378.000 |

### A alíquota efetiva

A alíquota da tabela **não** é a que você paga. Pela LC 123 (art. 18, § 1º-A):

```text
alíquota efetiva = (RBT12 × alíquota nominal − parcela a deduzir) / RBT12
```

em que **RBT12** é a receita bruta dos **12 meses anteriores** ao mês de apuração.

| Receita dos últimos 12 meses | Conta | Alíquota efetiva |
|---|---|---|
| R$ 150.000 | 1ª faixa | **4,00%** |
| R$ 300.000 | (300.000 × 7,3% − 5.940) / 300.000 | **5,32%** |
| R$ 600.000 | (600.000 × 9,5% − 13.860) / 600.000 | **7,19%** |

A alíquota efetiva **sobe aos poucos** com o faturamento: não existe o "degrau" de pagar muito mais só por mudar de faixa. O imposto do mês é a alíquota efetiva × a receita do mês.

### Fator R (serviços)

Para algumas atividades de serviço, a tributação depende do **fator R**: a razão entre a folha de pagamento (incluindo pró-labore) e a receita dos últimos 12 meses. Com fator R de 28% ou mais, a atividade pode ser tributada pelo Anexo III, em geral mais barato que o Anexo V. É um ponto clássico de planejamento com o contador.

## Reforma tributária: o que muda

A reforma do consumo (Emenda Constitucional 132/2023, regulamentada pela LC 214/2025) troca PIS, Cofins, ICMS, ISS e parte do IPI por dois tributos sobre valor agregado: a **CBS** (federal) e o **IBS** (estadual e municipal). A transição é longa:

| Período | O que acontece (LC 214/2025) |
|---|---|
| **2026** | ano de teste: CBS de 0,9% e IBS de 0,1%, compensáveis com PIS/Cofins; há dispensa de recolhimento para quem cumpre as obrigações acessórias. Essas alíquotas **não se aplicam aos optantes do Simples Nacional** (art. 348) |
| **2027 e 2028** | a CBS passa a valer de fato; o IBS segue com alíquota simbólica |
| **2029 a 2032** | o IBS sobe aos poucos enquanto ICMS e ISS diminuem |
| **2033** | o novo sistema passa a valer por completo |

O **Simples Nacional continua existindo**. A reforma cria opções para a empresa do Simples decidir como tratar IBS e CBS, o que importa principalmente para quem vende para outras empresas, por causa dos créditos. É uma decisão para os próximos anos, **com o contador**.

## Nota fiscal

- Venda de produto: **NF-e**; serviço: **NFS-e**, com o padrão nacional em implantação.
- O MEI é dispensado de emitir nota para pessoa física, mas precisa emitir para empresas. Veja também [[Ecommerce/11-Fiscal-e-Legal|fiscal e legal no e-commerce]].

## Perguntas de revisão

Qual o limite anual de faturamento do MEI? :: R$ 81.000, ou R$ 251.600 para transportador autônomo de cargas (conferido em 23/09/2026).

Quantos empregados o MEI pode ter? :: No máximo um, recebendo o salário mínimo ou o piso da categoria.

O que acontece com o limite de quem abre MEI no meio do ano? :: É proporcional aos meses de atividade no ano.

Qual o limite de faturamento do Simples Nacional? :: R$ 4,8 milhões por ano.

Qual a fórmula da alíquota efetiva do Simples Nacional? :: (RBT12 × alíquota nominal − parcela a deduzir) / RBT12, com RBT12 sendo a receita dos 12 meses anteriores.

Qual a alíquota efetiva de uma empresa de comércio com R$ 300.000 de receita em 12 meses? :: Cerca de 5,32%.

O que é o fator R? :: A razão entre folha de pagamento e receita dos últimos 12 meses; com 28% ou mais, certos serviços podem ser tributados pelo Anexo III em vez do V.

Quais tributos a reforma tributária cria? :: A CBS, federal, e o IBS, estadual e municipal, no lugar de PIS, Cofins, ICMS, ISS e parte do IPI.

As alíquotas de teste de 2026 da CBS e do IBS valem para o Simples Nacional? :: Não; a LC 214/2025 exclui as operações dos optantes do Simples Nacional.

Em que ano o novo sistema tributário passa a valer por completo? :: Em 2033.

---
Anterior: [[09-Contas-a-Pagar-e-Fornecedores|Contas a pagar]] · Próxima: [[11-Credito-Juros-e-Emprestimos|Crédito e juros]] · Trilha: [[Financas/00-Indice|Finanças]]
