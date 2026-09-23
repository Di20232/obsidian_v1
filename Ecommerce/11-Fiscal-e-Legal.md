---
tags: [ecommerce, legal, fiscal, lgpd, seguranca]
cssclasses: [cerebro-nota, cerebro-ecommerce]
verificado_em: 2026-09-23
---

# Fiscal e legal

> [!warning] Isto é um mapa, não assessoria
> Esta nota organiza o que precisa ser resolvido. Enquadramento tributário, alíquotas e obrigações de cada estado **devem ser confirmados com um contador**. A reforma tributária (IBS e CBS) está em transição a partir de 2026, e as regras vão mudar nos próximos anos.

## Formalização

| Forma | Em resumo | Atenção |
|---|---|---|
| **MEI** | CNPJ simples, imposto fixo mensal (DAS) | limite anual de faturamento e lista de atividades permitidas: confira os valores atuais no Portal do Empreendedor; não pode ter sócio |
| **ME / EPP no Simples Nacional** | alíquota única sobre o faturamento, por faixa | no comércio, a faixa inicial parte de 4%; a alíquota efetiva sobe com o faturamento |
| **Lucro Presumido / Real** | regimes para faturamentos maiores ou margens específicas | exige contador desde o início |

CNPJ também costuma ser exigido por provedores de pagamento, transportadoras e marketplaces para taxas melhores.

## Nota fiscal

- Venda de **produto** gera **NF-e** (nota fiscal eletrônica, modelo 55). O DANFE acompanha o pacote.
- O MEI é dispensado de emitir nota em venda para pessoa física, mas **obrigado** em venda para empresa. Muitas lojas emitem sempre, porque transportadoras e marketplaces pedem.
- Venda para **outro estado** tem regras de ICMS (DIFAL) que dependem do regime. Pergunte ao contador.
- Na Shopify, a emissão é feita por **app emissor** ou por um **ERP integrado** (Bling e Tiny são exemplos comuns). Os dados vêm do pedido: CPF/CNPJ, endereço, NCM do produto.
- Cadastre em cada produto o **NCM** (classificação fiscal) correto, com orientação do contador.

## Código de Defesa do Consumidor

| Regra | O que diz | Na prática |
|---|---|---|
| **Direito de arrependimento** (CDC, art. 49) | compra fora do estabelecimento pode ser desistida em **7 dias** do recebimento, sem justificativa | devolver **tudo**, inclusive o frete; o custo do retorno é da loja |
| **Garantia legal** (CDC, art. 26) | 30 dias para produto não durável, 90 para durável, para reclamar de defeito | não depende de "garantia da loja" |
| **Oferta vincula** (CDC, art. 30) | o preço e as condições anunciados precisam ser cumpridos | erro de preço evidente é discutível; na dúvida, honre ou resolva com o cliente |
| **Propaganda enganosa** | proibida | nada de "de R$ 200 por R$ 99" se nunca custou 200; nada de estoque "últimas unidades" falso |

## Decreto do comércio eletrônico (Decreto 7.962/2013)

A loja precisa mostrar, **em local de fácil visualização**:
- razão social, **CNPJ**, endereço físico e eletrônico;
- características essenciais do produto e riscos;
- **preço total**, com despesas adicionais como o frete, discriminadas;
- condições da oferta: pagamento, disponibilidade, prazo de entrega;
- resumo do contrato antes de concluir a compra;
- **confirmação imediata** do recebimento do pedido;
- atendimento eletrônico, com resposta em até **5 dias**;
- forma clara de exercer o **direito de arrependimento**.

Na Shopify: rodapé com dados da empresa, [[05-Shopify-Configurando-a-Loja|políticas configuradas]] e e-mail de confirmação de pedido ativo.

## LGPD (Lei 13.709/2018)

- Colete só o necessário para vender, entregar e emitir nota.
- **Política de privacidade** clara: o que coleta, para quê, com quem compartilha (provedor de pagamento, transportadora, emissor de nota), como pedir exclusão.
- **Consentimento** para marketing: caixa de e-mail e SMS **desmarcada** por padrão.
- Acesso ao painel só para quem precisa, com login próprio e verificação em duas etapas.
- Planilhas de clientes exportadas não ficam soltas no computador ou no WhatsApp.

## Outros cuidados

- **Produtos regulados** (alimentos, cosméticos, suplementos, eletrônicos, produtos infantis) podem exigir registro na Anvisa, certificação do Inmetro ou rotulagem específica.
- **Marca:** antes de investir num nome, pesquise no INPI se já existe registro.
- **Imagens:** use fotos próprias ou autorizadas pelo fornecedor. Copiar foto de concorrente é violação de direito autoral.

---
Anterior: [[10-Estoque-e-Compras|Estoque e compras]] · Próxima: [[12-Atendimento-e-Pos-Venda|Atendimento e pós-venda]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
