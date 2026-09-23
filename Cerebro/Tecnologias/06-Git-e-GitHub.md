---
tags: [tecnologia, git, github, versionamento, flashcards]
cssclasses: [cerebro-nota, cerebro-engenharia]
---

# Git e GitHub nesta máquina

Complementa o guia prático [[../Guias/05-Git-e-VS-Code-no-Dia-a-Dia|Git e VS Code no dia a dia]].

## Duas identidades, dois papéis

Este é o conceito que gerou o problema mais persistente do cofre:

| Quem | Definido por | Papel |
|---|---|---|
| **Autor do commit** | `git config user.name` / `user.email` | Assina o commit |
| **Quem faz o push** | Git Credential Manager do Windows | Autentica no GitHub |

**Eles podem divergir** — e divergem. Foi exatamente isso no [[../Problemas-Resolvidos/24-Push-403-com-Conta-Git-Errada|erro 403]]: os commits eram assinados corretamente, mas o push falhava porque a credencial em cache era de outra conta.

> [!programacao] 401 e 403 dizem coisas diferentes
> **401** = não sei quem você é (credencial inválida).
> **403** = sei quem você é, e você não pode (conta errada ou sem permissão).
> Confundir os dois leva a horas mexendo em credencial válida.

## Verificar antes de um push importante

```bash
gh auth status
```
```bash
git config user.name && git config user.email
```

## Fluxo usado nos projetos

```bash
git status --short && git diff --stat
```
```bash
git log origin/master..HEAD --oneline
```

**Antes de commitar, sempre conferir se arquivos sensíveis estão rastreados:**

```bash
git ls-files --error-unmatch .env
```

Se esse comando **encontra** o `.env`, há um problema — ele deveria estar no `.gitignore`.

## Transformar clone em repositório próprio

Quando se quer os arquivos sem o histórico do original (caso dos [[../Projetos/08-Exercicios-IMP|Exercícios IMP]]):

```bash
rm -rf .git && git init -b main
```

## O que o `.gitignore` precisa cobrir

Levantado na auditoria do CTL-TINTA-FL: bancos (`*.db`, `*.sqlite*`) e seus **backups** (`*.db.bak*`), `.env` e arquivos de segredo, diretórios de build (`.web`), screenshots, lockfiles de ferramentas e arquivos internos de documentação.

## Links relacionados

- Ambiente: [[../Ambiente/03-Contas-Git|Contas Git nesta máquina]]
- Problema: [[../Problemas-Resolvidos/24-Push-403-com-Conta-Git-Errada|Push 403]]
- Trilha: [[../../Programacao-Geral/00-Indice|Programação Geral]]

## Perguntas de revisão

Como ver os commits locais que ainda não foram enviados? :: Com git log origin/master..HEAD --oneline (trocando master pelo nome do branch).

Como transformar um clone num repositório próprio sem o histórico original? :: Apagando a pasta .git e rodando git init -b main.

O que o .gitignore de um projeto precisa cobrir? :: Bancos e seus backups, .env e segredos, pastas de build, screenshots e arquivos internos.
