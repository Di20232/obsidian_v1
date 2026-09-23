---
tags: [ambiente, git, github]
cssclasses: [cerebro-nota, cerebro-ambiente]
---

# Contas Git nesta máquina

Duas contas do GitHub aparecem nos projetos, e a confusão entre elas bloqueou um projeto inteiro.

## As duas contas

| Conta | Onde aparece |
|---|---|
| **Di20232** | Autenticada no Git Credential Manager. Dona de `mercadinho-seu-joao` |
| **diego2600612** | Dona de `AP1-python`, destino dos [[../Projetos/08-Exercicios-IMP|Exercícios IMP]] |

## O conceito que resolve

**Quem assina o commit e quem faz o push são configurações diferentes.**

| Papel | Definido por |
|---|---|
| Autor do commit | `git config user.name` / `user.email` |
| Autenticação do push | Git Credential Manager do Windows |

Podem divergir sem aviso — e foi isso que produziu o erro 403 nos Exercícios IMP: commits corretos, push recusado.

> [!problema] 403 não é problema de credencial
> **401** = credencial inválida. **403** = credencial válida, sem permissão.
> Um 403 quase sempre significa **conta errada**, não senha errada. Mexer na credencial pensando que ela está quebrada é perder tempo no lugar errado.

## Verificar antes de um push para repositório de terceiro

```bash
gh auth status
```
```bash
git config user.name && git config user.email
```

## Trocar a conta autenticada

O Credential Manager **guarda a credencial em cache** — tentar de novo não abre login, ele reusa silenciosamente. Para forçar a troca:

1. Painel de Controle → Contas de Usuário → **Gerenciador de Credenciais** → Credenciais do Windows
2. Remover entradas `git:https://github.com`
3. Tentar o push — agora o navegador abre para login

> [!seguranca] Sobre tokens
> Um token pessoal com escopo `repo` também resolve, mas **não cole tokens em conversa nem os guarde neste cofre**. Configure direto no Credential Manager ou em variável de ambiente.

## Pendência aberta

Os [[../Projetos/08-Exercicios-IMP|Exercícios IMP]] seguem sem push. Resolver exige trocar a credencial para `diego2600612` ou adicionar `Di20232` como colaborador no repositório.

## Links relacionados

- Problema: [[../Problemas-Resolvidos/24-Push-403-com-Conta-Git-Errada|Push 403 com conta errada]]
- Tecnologia: [[../Tecnologias/06-Git-e-GitHub|Git e GitHub]]
