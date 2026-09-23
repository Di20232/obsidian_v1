---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/claude-md-assistant-template.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# references/claude-md-assistant-template.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/references/claude-md-assistant-template.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

# `_CLAUDE.md` Template - Assistant Mode

Use this template when the vault operator is maintaining a vault FOR someone else (e.g., an executive assistant managing their boss's knowledge base, a consultant tracking a client's decisions).

---

## The Template

```markdown
# Claude Operating Manual - [Subject Name]'s Vault

> Read this file before doing anything in this vault.
> This vault is maintained BY [Operator Name] FOR [Subject Name].

---

## Vault Identity

- **Subject:** [Subject Name] - the person this vault is about
- **Operator:** [Operator Name] - the person who maintains this vault
- **Vault path:** [path]
- **Structure:** Wiki-style (LLM-first)
- **Last updated:** [date]

---

## Operating Mode: Assistant

This vault is operated on behalf of someone else. Key differences from personal mode:

- **Voice**: write in [Subject Name]'s voice and perspective, not the operator's
- **Capture logic**: save what matters to [Subject Name], not what matters to the operator
- **Synthesis focus**: surface patterns relevant to [Subject Name]'s goals and decisions
- **Privacy**: the operator may not have full context - ask before saving sensitive topics
- **Decision records**: always note WHO made the decision (subject or operator)

---

## Subject Profile

- **Role:** [role]
- **Company:** [company]
- **Communication style:** [how the subject thinks and communicates]
- **Priorities:** [current top priorities]
- **Key people:** [important relationships]

---

## Operator Rules

- Save everything from conversations the operator has ABOUT the subject
- Flag when the operator's interpretation might differ from the subject's intent
- Keep a clear audit trail - the subject should be able to review what was saved and why
- Never mix the operator's personal notes into this vault

---

[Rest of standard _CLAUDE.md sections: folder map, auto-save rules, naming conventions, etc.]
```

---

## When to Use

- An executive assistant managing their CEO's knowledge base
- A consultant tracking decisions for a client
- A team lead maintaining a project vault on behalf of the team
- A researcher organizing notes about a subject they're studying
