---
tags: [moc, projetos]
aliases: [Projetos]
cssclasses: [cerebro-nota, cerebro-projetos]
---

# 📦 Projetos

Cada nota descreve um sistema real: o que resolve, como executar, decisões tomadas e o que ficou pendente. Volta para [[../00-Cerebro|🧠 Cérebro]].

## Registrados

| # | Projeto | Natureza | Estado | Código no GitHub |
|---|---|---|---|---|
| 01 | [[01-Assistente-Jarvis-Local\|Assistente JARVIS Local]] | Assistente pessoal local em português | entregue localmente | — |
| 02 | [[02-Sistema-de-Vendas-e-Estoque\|Sistema de Vendas e Estoque]] | Requisitos para pequeno comércio | requisitos iniciais | — |
| 03 | [[03-Loja-de-Infoprodutos-sobre-IA\|Loja de Infoprodutos sobre IA]] | Negócio digital | planejamento | — |
| 04 | [[04-Planejamento-de-E-commerce\|Planejamento de E-commerce]] | Negócio digital | planejamento | — |
| 05 | [[05-CTL-TINTA-FL\|CTL-TINTA-FL]] | Controle de tinta/toner em 16 filiais | 🟢 em desenvolvimento | [[../GitHub/CTL-TINTA/00-Indice\|Di20232/CTL-TINTA]] ⚠️ vazio |
| 06 | [[06-Mercadinho-Seu-Joao\|Mercadinho Seu João]] | Vendas e estoque de mercadinho | 🟢 em uso | [[../GitHub/contro-vend-public/00-Indice\|Di20232/contro-vend-public]] |
| 07 | [[07-Projeto-W-Analise-de-Vendas\|Projeto W]] | Análise de vendas e planejamento de estoque | 🟢 em uso | — (não encontrado na importação) |
| 08 | [[08-Exercicios-IMP\|Exercícios IMP]] | Exercícios de algoritmos | 🔴 bloqueado | — (push nunca completou) |
| 09 | [[09-OmniRoute\|OmniRoute]] | — | ⚪ apenas iniciado | — |

> [!projeto] Um repositório sem nota de projeto
> A importação do GitHub também encontrou [`Di20232/byteShop`](https://github.com/Di20232/byteShop) — um e-commerce completo (FastAPI + React/TypeScript, 88 arquivos) catalogado em [[../GitHub/byteShop/00-Indice|Cerebro/GitHub/byteShop]]. Nenhuma das 19 sessões lidas para este cérebro menciona esse projeto — ele não tem nota aqui porque não há histórico de trabalho para destilar, só o código publicado. Se for retomado com Claude Code, vale criar a nota 10 quando isso acontecer.

> [!projeto] Duas origens, um cofre
> As notas **01 a 04** nasceram de conversas de planejamento e requisitos. As notas **05 a 09** vêm das sessões de implementação no Claude Code, com código executado, bugs corrigidos e commits reais. Quando as duas descrevem o mesmo domínio, vale ler as duas: [[02-Sistema-de-Vendas-e-Estoque|os requisitos]] e [[06-Mercadinho-Seu-Joao|a implementação]] tratam do mesmo problema em momentos diferentes.

## O padrão comum

Os três sistemas implementados (05, 06 e 07) seguem a mesma forma:

> **Planilha ou lançamento manual entra → banco local guarda → tela mostra saldo, alerta e relatório → exporta CSV.**

E os três esbarraram na mesma família de obstáculos:

| Obstáculo | Onde está documentado |
|---|---|
| Conflito de porta no Windows | [[../Ambiente/02-Portas-e-Conflitos\|Portas e conflitos]] |
| Números e datas no formato brasileiro | [[../Praticas/05-Importacao-de-Planilhas\|Importação de planilhas]] |
| Auditoria de segurança pedida pelo usuário | [[../Praticas/06-Caca-de-Bugs\|Caça de bugs]] |

## Adicionar um projeto

Use [[../Templates/Template-Projeto|Template de Projeto]]. Registre objetivo, como executar, decisões e pendências — e conecte os problemas que ele gerou em [[../Problemas-Resolvidos/00-Indice|Problemas Resolvidos]].
