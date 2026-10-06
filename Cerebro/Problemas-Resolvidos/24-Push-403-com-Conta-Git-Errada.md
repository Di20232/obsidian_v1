---
tags: [problema-resolvido, git, github, ambiente, windows, flashcards]
status: bloqueado
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Push recusado com 403 por conta Git errada

## Contexto

[[../Projetos/08-Exercicios-IMP|Exercícios IMP]] · Windows com Git Credential Manager · push para `diego2600612/AP1-python`.

## Sintoma e impacto

```
remote: Permission to diego2600612/AP1-python.git denied
fatal: unable to access ... : The requested URL returned error: 403
```

**Este problema segue em aberto** — é o motivo de o projeto estar bloqueado.

## Causa-raiz

A máquina tem **duas contas GitHub em jogo**:

| Conta | Papel |
|---|---|
| **Di20232** | A que está autenticada no Git Credential Manager |
| **diego2600612** | A dona do repositório de destino |

O Git autenticou com sucesso como `Di20232` — e essa conta **não tem permissão de escrita** no repositório da outra. Daí 403, e não 401: a credencial é válida, o acesso é que não existe.

> Vale separar: **401** é "não sei quem você é"; **403** é "sei quem você é, e você não pode". O segundo quase sempre significa conta errada ou permissão faltando, não credencial inválida.

Um detalhe que atrapalha o diagnóstico: o Credential Manager **guarda a credencial em cache**. Tentar de novo não abre tela de login — ele reusa a conta antiga silenciosamente.

## Caminhos para resolver

**Opção A — trocar a credencial salva (recomendada):**

1. Abrir o **Gerenciador de Credenciais do Windows**
   (Painel de Controle → Contas de Usuário → Gerenciador de Credenciais → Credenciais do Windows)
2. Localizar entradas como `git:https://github.com` e **removê-las**
3. Tentar o push de novo — sem cache, o Credential Manager abre o navegador para login como `diego2600612`

**Opção B — dar acesso à conta atual:**

Adicionar `Di20232` como colaborador em `diego2600612/AP1-python`, pelas configurações do repositório no GitHub.

> [!seguranca] Sobre tokens de acesso pessoal
> Um token com escopo `repo` também resolveria, mas **não cole tokens em conversas nem os guarde neste cofre**. Se optar por token, configure-o direto no Credential Manager ou em variável de ambiente da sua sessão.

## Prevenção

> [!problema] Antes de um push para repositório de terceiro
> Confirme com qual identidade o Git vai falar:
> ```bash
> gh auth status
> git config user.name
> ```
> `user.name` e `user.email` definem quem **assina o commit**; o Credential Manager define quem **faz o push**. São coisas diferentes, e podem divergir — foi exatamente o que aconteceu aqui.

## Links relacionados

- Projeto: [[../Projetos/08-Exercicios-IMP|Exercícios IMP]]
- Ambiente: [[../Ambiente/03-Contas-Git|Contas Git nesta máquina]]
- Tecnologia: [[../Tecnologias/06-Git-e-GitHub|Git e GitHub]]

## Perguntas de revisão

Qual a diferença entre erro 401 e 403 num push? :: 401 é credencial não reconhecida; 403 é credencial válida de uma conta sem permissão no repositório.

Por que tentar o push de novo não pede outro login? :: Porque o Git Credential Manager guarda a credencial em cache e reusa a conta antiga.

Como trocar a conta usada no push no Windows? :: Removendo as entradas git:https://github.com no Gerenciador de Credenciais do Windows e tentando de novo.

Qual a diferença entre user.name e a conta do Credential Manager? :: user.name e user.email assinam o commit; o Credential Manager define quem faz o push.
