---
tags: [projeto, python, git]
status: bloqueado
cssclasses: [cerebro-nota, cerebro-projetos]
---

# Exercícios IMP

> [!projeto] Origem
> Registro extraído das sessões de trabalho no Claude Code. Volta para [[00-Indice|📦 Projetos]].

## O que é

Exercícios de algoritmos em Python (`ex01.py` … `ex05.py`), clonados do repositório do professor para entrega em repositório próprio.

- **Pasta:** `C:\Users\Perim\Documents\proejto\exercicio_imp\exercicios_imp`
- **Origem:** `profedsonvieira/AlgoritmosExercicios`
- **Destino pretendido:** `diego2600612/AP1-python`

## O que foi feito

1. Clone do repositório do professor
2. Remoção do `.git` original e `git init -b main` — para virar repositório próprio, não um fork
3. Commit dos 5 exercícios mais o `.gitignore`
4. `git remote add origin` e tentativa de push

## 🔴 Por que está bloqueado

O push falhou com **403**: o Git da máquina está autenticado como **Di20232**, mas o repositório de destino pertence a **diego2600612** — e essa conta não tem permissão de escrita nele.

→ Solução completa em [[../Problemas-Resolvidos/24-Push-403-com-Conta-Git-Errada|Push 403 — conta Git errada]] e contexto em [[../Ambiente/03-Contas-Git|Contas Git]].

**Próximo passo:** limpar a credencial salva no Gerenciador de Credenciais do Windows e logar como `diego2600612` — ou dar permissão de colaborador para `Di20232`.

## Não confundir com Di20232/exercises_python

> [!problema] Repositório parecido, mas não é este
> A importação do GitHub encontrou [`Di20232/exercises_python`](https://github.com/Di20232/exercises_python) — catalogado em [[../GitHub/exercises_python/00-Indice|Cerebro/GitHub/exercises_python]] — e à primeira vista parece o destino natural destes exercícios. **Não é.** Três diferenças:
>
> | | Esta nota (bloqueada) | `exercises_python` (publicado) |
> |---|---|---|
> | Origem | Clone de `profedsonvieira/AlgoritmosExercicios` | Autoria própria, sem clone |
> | Destino do push | `diego2600612/AP1-python` | Já é o repositório final |
> | Conteúdo | `ex01.py`…`ex05.py`, algoritmos genéricos do professor | `combo_a`/`combo_b`: os mesmos 5 temas (variáveis, carrinho, recibo, regras de acesso, sistema escolar) resolvidos **duas vezes** — uma com funções, outra com classes — ver [[../GitHub/exercises_python/01-Guia-de-Estudo|guia de estudo]] |
>
> Ou seja: `exercises_python` é um **projeto de estudo separado**, já publicado com sucesso, e não a solução do bloqueio de push descrito nesta nota. As duas sessões nunca se cruzaram — vale não apresentar uma como continuação da outra sem confirmar com o usuário.
