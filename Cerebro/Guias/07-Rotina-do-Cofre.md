---
tags: [guia, cerebro, obsidian, git, flashcards]
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

**Salvar:** no Windows, clicar duas vezes em `ferramentas/salvar-cofre.bat`, na pasta do cofre pelo Explorador de Arquivos. Em qualquer sistema, rodar no terminal aberto na pasta do cofre:

```bash
node ferramentas/salvar-cofre.js "o que mudou"
```

Ele verifica os links, mostra o que mudou e grava. Sem mensagem, usa "Cofre em AAAA-MM-DD HH:MM (N arquivos)". Grava tudo o que não está no `.gitignore` (`git add -A`), sem pedir confirmação. O ponto de restauração fica só neste computador: o script não faz `git push`.

> [!info] Os `.bat` são atalhos para Windows
> `salvar-cofre.bat` e `lembretes.bat` só chamam, com o Node.js, o script `.js` de mesmo nome em `ferramentas/`. No Linux ou no macOS, use `node ferramentas/<script>.js`.

**Ver o histórico de uma nota:**

```bash
git log --oneline -- "Cerebro/Projetos/00-Indice.md"
```

**Ver como a nota estava numa versão:**

```bash
git show 8ab2c88:"Cerebro/Projetos/00-Indice.md"
```

**Restaurar a nota para essa versão** (sobrescreve a atual; o estado de agora continua recuperável se já estiver salvo):

```bash
git restore --source 8ab2c88 -- "Cerebro/Projetos/00-Indice.md"
```

`8ab2c88` é o código que o `git log` acima mostra para essa nota (a fotografia inicial do cofre, de 23/09/2026). Troque pelo código da versão que você quer. Os comandos rodam no terminal aberto na pasta do cofre.

> [!seguranca] Por que isso existe
> Em 15/09/2026 uma sessão sobrescreveu o índice de projetos criado por outra, e não havia como recuperar. O git resolve exatamente esse caso — desde que se salve com frequência. Antes e depois de pedir a um agente que mexa no cofre, salve.

## Verificar os links sem salvar

```bash
node ferramentas/verificar-links.js
```

Por padrão ignora as cópias de código em `*/Fontes/*`, onde links como `[[people/Sam Patel]]` são exemplos do repositório original, não notas. Para ver tudo, acrescente `--tudo`.

## Lembretes e exportação para IA

`ferramentas/lembretes.bat` (Windows) ou `node ferramentas/lembretes.js` sorteia perguntas de revisão do cofre para relembrar, e `node ferramentas/exportar-para-ia.js` gera os arquivos de treino. Convenções e comandos em [[08-Cofre-para-IA-e-Lembretes|Cofre para IA e lembretes]].

## Encontrar notas soltas

```bash
node ferramentas/notas-soltas.js
```

Lista as notas **isoladas** (nenhuma ligação), **sem entrada** (ninguém aponta para elas, então só são achadas por busca) e **sem saída** (não apontam para nada). Por padrão ignora as cópias de código em `*/Fontes/*`; `--tudo` inclui essas cópias. Uma vez por mês, na revisão semanal, vale rodar e ligar o que apareceu. Dois casos aparecem sempre e estão certos:
- os modelos de conceito, decisão, problema, projeto e tecnologia, como "sem saída": os links deles são espaços vazios (`[[]]`) para preencher, porque um link fixo seria copiado para toda nota nova;
- o `README.md` da raiz, como "sem entrada": ele descreve o repositório para quem chega pelo GitHub, e nenhuma nota precisa apontar para ele.

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

## Perguntas de revisão

Como salvar um ponto de restauração do cofre? :: Com node ferramentas/salvar-cofre.js, ou no Windows com duplo clique em ferramentas/salvar-cofre.bat, que verifica os links e grava no git deste computador.

Como ver o histórico de uma nota do cofre? :: Com git log --oneline -- "caminho/da/nota.md".

Como restaurar uma nota para uma versão anterior? :: Com git restore --source CODIGO -- "caminho/da/nota.md", usando o código que o git log mostrar.

Onde caem as notas novas criadas com Ctrl+N? :: Na pasta Inbox, de onde saem na revisão semanal.

Quanto tempo leva a revisão semanal do cofre? :: De 20 a 30 minutos.
