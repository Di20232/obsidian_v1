---
tags: [guia, cerebro, obsidian, git]
aliases: [Rotina do Cofre, Revisão Semanal]
cssclasses: [cerebro-nota, cerebro-geral]
---

# Rotina do cofre

O cérebro só vale se continuar recebendo o que acontece de verdade. Esta rotina é o mínimo para isso, e o [[02-Como-Usar|Como usar]] explica o porquê de cada tipo de nota.

## Todo dia de trabalho

| Momento | O que fazer |
|---|---|
| Ao começar | Abrir a nota de hoje (ícone de calendário) — ela nasce em [[Diario/00-Diario|Diário]] já com o modelo |
| Durante | Jogar ideias, dúvidas e links em **Capturas**, sem organizar |
| Ao resolver um bug | Registrar na hora com o [[Template-Problema|modelo de problema]]: o sintoma exato e a causa-raiz somem da memória em dias |
| Ao terminar | Uma linha em **Próximo passo**: é o que permite retomar amanhã sem reler tudo |

Nota nova criada por `Ctrl+N` cai em `Inbox/`: é de propósito. Ela sai de lá na revisão.

## Toda semana — revisão de 20 a 30 minutos

Criar uma nota em `Diario/` e inserir o [[Template-Revisao-Semanal|modelo de revisão]] (`Ctrl+P` → *Modelos: Inserir modelo*). O modelo guia os cinco passos: esvaziar capturas, atualizar projetos, registrar problemas e decisões, marcar marcos na [[Linha-do-Tempo|Linha do Tempo]] e salvar.

## Salvar e desfazer

O cofre é um repositório git desde 23/09/2026. Cada vez que você salva, fica um ponto de restauração: dá para voltar qualquer nota a qualquer versão salva, mesmo que outro agente ou um clique errado a tenha sobrescrito.

**Salvar:** clicar duas vezes em `ferramentas/salvar-cofre.bat`, na pasta do cofre pelo Explorador de Arquivos. Ele verifica os links, mostra o que mudou e grava.

**Ver o histórico de uma nota:**

```bash
git log --oneline -- "Cerebro/Projetos/00-Indice.md"
```

**Ver como a nota estava numa versão:**

```bash
git show 37d467e:"Cerebro/Projetos/00-Indice.md"
```

**Restaurar a nota para essa versão** (sobrescreve a atual; o estado de agora continua recuperável se já estiver salvo):

```bash
git restore --source 37d467e -- "Cerebro/Projetos/00-Indice.md"
```

Troque `37d467e` pelo código que o `git log` mostrar. Os comandos rodam no terminal aberto na pasta do cofre.

> [!seguranca] Por que isso existe
> Em 15/09/2026 uma sessão sobrescreveu o índice de projetos criado por outra, e não havia como recuperar. O git resolve exatamente esse caso — desde que se salve com frequência. Antes e depois de pedir a um agente que mexa no cofre, salve.

## Verificar os links sem salvar

```bash
node ferramentas/verificar-links.js
```

Por padrão ignora as cópias de código em `*/Fontes/*`, onde links como `[[people/Sam Patel]]` são exemplos do repositório original, não notas. Para ver tudo, acrescente `--tudo`.

## Encontrar notas soltas

```bash
node ferramentas/notas-soltas.js
```

Lista as notas **isoladas** (nenhuma ligação), **sem entrada** (ninguém aponta para elas, então só são achadas por busca) e **sem saída** (não apontam para nada). Uma vez por mês, na revisão semanal, vale rodar e ligar o que apareceu. Os modelos em `Templates/` sempre aparecem como "sem saída" e está certo: um link dentro de um modelo seria copiado para toda nota nova.

## Configuração do Obsidian que sustenta a rotina

| Ajuste | Valor |
|---|---|
| Nota nova | `Cerebro/Inbox` |
| Notas diárias | `Cerebro/Diario`, nome `AAAA-MM-DD`, modelo de nota diária |
| Pasta de modelos | `Cerebro/Templates` |
| Anexos (imagens, PDFs) | `Cerebro/Anexos` |
| Atualizar links ao renomear | sempre, sem perguntar |
| Fora da busca e do grafo | `Cerebro/GitHub/Second-Brain/Fontes/` (código de terceiros com links de exemplo) |

Veja também: [[Guias/05-Git-e-VS-Code-no-Dia-a-Dia|Git e VS Code no dia a dia]] · [[Praticas/09-Como-Trabalhamos|Como trabalhamos]]
