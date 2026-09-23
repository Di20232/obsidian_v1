---
tags: [linha-do-tempo, projetos, revisao]
aliases: [Linha do tempo]
cssclasses: [cerebro-nota, cerebro-geral]
---

# 🗓️ Linha do Tempo

Marcos que ajudam a recuperar contexto: início ou encerramento de um projeto, mudança importante de arquitetura, migração, incidente relevante ou aprendizado que alterou a forma de trabalhar.

Volta para [[00-Cerebro|🧠 Cérebro]].

## Como registrar um marco

```markdown
## AAAA-MM-DD — Título do marco

- O que aconteceu:
- Por que importa:
- Links: nota do projeto · nota da decisão · nota do problema
```

## Marcos

### 2026-09-03 — Primeiro repositório próprio, e o primeiro bloqueio

- **O que aconteceu:** exercícios de algoritmos clonados do professor, convertidos em repositório próprio (`rm -rf .git && git init`) e preparados para entrega. O push falhou com 403.
- **Por que importa:** revelou que a máquina tem **duas contas GitHub** e que assinar o commit e autenticar o push são configurações independentes. O projeto segue bloqueado por isso.
- **Links:** [[Projetos/08-Exercicios-IMP|Exercícios IMP]] · [[Problemas-Resolvidos/24-Push-403-com-Conta-Git-Errada|Push 403]] · [[Ambiente/03-Contas-Git|Contas Git]]

### 2026-09-08 — Dois sistemas no ar no mesmo dia

- **O que aconteceu:** pela manhã o [[Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] subiu em Docker e localmente; à tarde o [[Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]] entrou no ar via Streamlit. Ambos ganharam dados de exemplo e passaram por auditoria de segurança.
- **Por que importa:** foi o dia que produziu a maior densidade de aprendizado de **ambiente** — conflito de porta, containers órfãos, dependência ausente — e as duas primeiras auditorias de segurança de verdade.
- **Links:** [[Problemas-Resolvidos/16-PostgreSQL-Nativo-Ocupa-a-Porta-5432|Porta 5432]] · [[Problemas-Resolvidos/17-Containers-Orfaos-em-System32|Containers órfãos]] · [[Praticas/06-Caca-de-Bugs|Caça de bugs]]

### 2026-09-08 — Importação de planilhas entra no Mercadinho

- **O que aconteceu:** aba Importar aceitando Excel, CSV, TSV e dados colados, com fluxo de 4 passos onde nada é gravado antes da confirmação.
- **Por que importa:** consolidou o padrão de **escrita em massa segura** — pré-visualização antes, auditoria depois, recusa em vez de palpite — que virou prática reutilizável.
- **Links:** [[Praticas/05-Importacao-de-Planilhas|Importação de planilhas]] · [[Problemas-Resolvidos/20-Importacao-Renomeia-Produto-Errado|O bug que motivou a regra]]

### 2026-09-10 — CTL-TINTA-FL troca de pele duas vezes

- **O que aconteceu:** o sistema de controle de tinta e toner saiu do **Tkinter** para **Flask + Jinja2**, foi validado com screenshots, e no mesmo dia migrou para **Reflex**.
- **Por que importa:** o `db.py` atravessou as três interfaces **sem reescrita**. É a evidência mais forte deste cofre de que separar dados de apresentação se paga sozinho.
- **Links:** [[Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · [[Tecnologias/02-Flask|Flask]] · [[Tecnologias/01-Reflex|Reflex]]

### 2026-09-11 — As unidades de medida viram regra de negócio

- **O que aconteceu:** ao longo do dia emergiram, uma a uma, as regras de litro, mililitro e unidade — incluindo garrafinhas de 65 ml e 120 ml e a separação do saldo no painel.
- **Por que importa:** nenhuma dessas regras estava no pedido original. Todas apareceram **usando o sistema**. Levou à criação de um módulo único (`util_unidade.py`) para evitar divergência entre telas.
- **Links:** [[Praticas/08-Unidades-de-Medida|Unidades de medida]] · [[Problemas-Resolvidos/11-Saldo-Geral-Misturando-Unidades|Saldo misturando unidades]]

### 2026-09-11 — O bug de exclusão revela sua terceira causa

- **O que aconteceu:** depois de duas correções que pareciam definitivas, a investigação no banco mostrou que **100% dos registros** estavam travados por chave estrangeira — e que o aviso existia, mas era invisível.
- **Por que importa:** virou o caso de referência sobre não confundir sintoma com causa, e sobre como dado de exemplo molda o que se consegue testar.
- **Links:** [[Problemas-Resolvidos/05-Exclusao-Nao-Funciona-em-Cadastros|O caso completo]]

### 2026-09-14 — O executável é removido: o projeto é um site

- **O que aconteceu:** decisão de eliminar todo o código ligado a aplicativo executável no CTL-TINTA-FL. Em seguida, caça intensa de bugs com dois workflows automáticos em paralelo — que **falharam** nos dois maiores arquivos.
- **Por que importa:** delimitou o escopo do produto e ensinou onde a automação em lote degrada. A pendência em `controle_suprimentos.py` e `db.py` continua aberta.
- **Links:** [[Problemas-Resolvidos/14-Workflows-Massivos-Falham-em-Arquivos-Grandes|Workflows massivos]]

### 2026-09-15 — O conhecimento vira cofre

- **O que aconteceu:** as 19 sessões de trabalho foram lidas e destiladas em notas de projeto, problema, tecnologia, prática e ambiente, dentro da estrutura do Cérebro.
- **Por que importa:** encerra o ciclo — o que era histórico de conversa virou material consultável antes do próximo bug.
- **Links:** [[00-Cerebro|Índice do Cérebro]] · [[Praticas/09-Como-Trabalhamos|Como trabalhamos]]

### 2026-09-15 — O código publicado entra no cofre, e nem tudo bate com o histórico

- **O que aconteceu:** os quatro repositórios públicos de `Di20232` foram importados arquivo por arquivo (498 arquivos, 90 em Markdown), junto com uma biblioteca externa sobre segundo cérebro. Ao ligar essas notas aos projetos já documentados, apareceram três discrepâncias reais: o `contro-vend-public` publicado **não tem** a aba de importação de planilhas do [[Projetos/06-Mercadinho-Seu-Joao|Mercadinho]]; o `CTL-TINTA` público está **vazio** — todo o trabalho do [[Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] segue só local; e `exercises_python` **não é** o mesmo projeto que os [[Projetos/08-Exercicios-IMP|Exercícios IMP]] bloqueados, apesar do nome parecido.
- **Por que importa:** o código publicado é uma fotografia de um commit específico, não um espelho do histórico de sessões. Antes de dizer que algo "já está no GitHub", vale conferir a nota da importação, não presumir pelo nome do repositório.
- **Links:** [[GitHub/00-Indice|Central GitHub]] · [[GitHub/04-Registro-da-Importacao|Registro da importação]] · [[Projetos/06-Mercadinho-Seu-Joao|Mercadinho]] · [[Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · [[Projetos/08-Exercicios-IMP|Exercícios IMP]]

### 2026-09-23 — O cofre ganha desfazer e rotina

- **O que aconteceu:** o cofre virou repositório git, com uma fotografia de todo o estado anterior. O Obsidian passou a criar notas novas no Inbox e notas diárias no Diário, com modelos próprios, e ganhou uma revisão semanal guiada e um verificador de links. Os dois únicos links realmente quebrados (MySQL → comparação com SQLite) foram corrigidos; os outros 76 eram exemplos dentro de código de terceiros.
- **Por que importa:** a perda de 15/09 — um índice sobrescrito sem volta — deixa de ser possível para qualquer coisa já salva. E o cofre deixa de depender de uma sessão grande de consolidação: passa a crescer um pouco por dia.
- **Links:** [[Guias/07-Rotina-do-Cofre|Rotina do cofre]] · [[Diario/00-Diario|Diário]] · [[Templates/Template-Revisao-Semanal|Revisão semanal]]

## Revisão

Ao fim de um projeto ou trimestre, releia os marcos e transforme padrões recorrentes em notas de prática, tecnologia ou problema resolvido.
