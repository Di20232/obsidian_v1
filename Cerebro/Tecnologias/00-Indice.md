---
tags: [moc, tecnologias]
aliases: [Tecnologias na prática]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# ⚙️ Tecnologias na Prática

Aqui ficam anotações sobre ferramentas usadas de verdade: configuração mínima, quando usar, escolhas feitas e pegadinhas que não aparecem em um tutorial inicial.

Volta para [[../00-Cerebro|🧠 Cérebro]].

## Usadas nos projetos

| # | Tecnologia | Onde | A pegadinha principal |
|---|---|---|---|
| 01 | [[01-Reflex\|Reflex]] | [[../Projetos/05-CTL-TINTA-FL\|CTL-TINTA-FL]] | Valores na tela são `Var`, não dados Python |
| 02 | [[02-Flask\|Flask]] | CTL-TINTA-FL (fase anterior) | `secret_key` precisa ser persistida em disco |
| 03 | [[03-SQLite-na-Pratica\|SQLite]] | CTL-TINTA-FL | JOIN sem alias gera colunas duplicadas |
| 04 | [[04-Docker\|Docker]] | [[../Projetos/06-Mercadinho-Seu-Joao\|Mercadinho]], [[../Projetos/07-Projeto-W-Analise-de-Vendas\|Projeto W]] | O diretório atual vira o nome do projeto |
| 05 | [[05-Prisma-e-PostgreSQL\|Prisma e PostgreSQL]] | Mercadinho | Client é gerado no `npm install` |
| 06 | [[06-Git-e-GitHub\|Git e GitHub]] | Todos | Assinar o commit ≠ autenticar o push |
| 07 | [[07-Streamlit\|Streamlit]] | Projeto W | `query_params` é entrada hostil |
| 08 | [[08-Claude-Code\|Claude Code]] | Todos | Plugin ≠ marketplace |

## Trilhas de estudo no cofre

A teoria por trás dessas ferramentas:

- [[../../Python/00-Indice|Python]] · [[../../JavaScript/00-Indice|JavaScript]] · [[../../PHP/00-Indice|PHP]]
- [[../../MySQL/00-Indice|MySQL]] · [[../../SQLite/00-Indice|SQLite]]
- [[../../CSS/00-Indice|CSS]] · [[../../Bootstrap/00-Indice|Bootstrap]] · [[../../TailwindCSS/00-Indice|Tailwind CSS]]

## Para registrar uma tecnologia nova

Comece com [[../Templates/Template-Tecnologia|Template de Tecnologia]]. Dê preferência à documentação oficial como fonte, registre versão quando ela importar e conecte a casos práticos.

Veja [[../Mapas/00-Mapa-Programacao|Mapa de Programação]] e [[../Mapas/03-Mapa-Engenharia|Engenharia de Software]].
