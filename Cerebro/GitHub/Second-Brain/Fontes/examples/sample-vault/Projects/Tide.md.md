---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/examples/sample-vault/Projects/Tide.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# examples/sample-vault/Projects/Tide.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/examples/sample-vault/Projects/Tide.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.


# Tide

## For future agent

Tide is a personal-project SaaS owned by <code>[[people/Alex Rivera]]</code>. Status: active as of 2026-04-27. Currently mid-rebuild of the retention/streaks system, which is the main feature users pay for. The Overview section explains what it is. Recent Activity captures the last 30 days. Key Decisions documents major directional choices with rationale. Everything in this note is fictional content for the obsidian-second-brain examples folder.

## Overview

Tide is a fictional habit-tracking SaaS aimed at indie creators who want a calmer alternative to gamified streak apps. Core mechanic: instead of binary streak/no-streak, Tide computes a rolling "tide level" that smooths out missed days based on rest patterns. Built on a fictional Postgres + Next.js stack.

## Status

- **Phase:** retention rebuild (week 2 of 3, as of 2026-04-27)
- **Paid users:** ~600 (as of 2026-04-27, internal stripe dashboard)
- **MRR:** TBD, not captured in this sample
- **Next release:** v0.9.0, target 2026-05-08

## Recent activity

- **2026-04-27** - Paired with <code>[[people/Sam Patel]]</code> on streak invalidation. Decision logged below. See <code>[[wiki/logs/2026-04-27 - Tide retention rebuild]]</code> for details
- **2026-04-26** - Released v0.8.4 patching a webhook race condition
- **2026-04-22** - Started the retention rebuild after support tickets clustered around streak loss complaints

## Key decisions

### 2026-04-27 - Drop hard streak invalidation in favor of decay

**Decision:** Stop invalidating streaks on a missed day. Instead, decay the tide level by a daily multiplier so users recover gradually instead of resetting to zero.

**Rationale:** Three weeks of support tickets (TBD: link the support digest note when written) showed users churning specifically after losing long streaks. The hard reset feels punitive and contradicts Tide's positioning as a calmer alternative. Confidence: `high` (multiple support tickets agree, plus competitor research from <code>[[Research/Web/2026-04-20 - Habit app retention mechanics]]</code> (TBD note)).

**Consequences:** Schema migration on the `streaks` table (decay coefficient column added). Front-end "tide level" gauge replaces the streak counter. Stripe subscriptions unaffected.

### 2026-03-12 - Build vs. buy on email delivery

**Decision:** Use a fictional managed service rather than self-hosting SMTP.

**Rationale:** Solo founder, deliverability is a specialist problem, the cost (~$30/month at current scale) is below the engineering hours saved. Confidence: `stated`.

## Open questions

- Should streak insurance (<code>[[Ideas/2026-04-27 - Streak insurance feature]]</code>) become its own SKU or a free-tier safety net?
- v0.9.0 changelog tone: keep technical or pitch the calmer-streak narrative? TBD.

## Sources

- Internal Stripe dashboard (private, owner-only access)
- Support tickets (Help Scout, owner-only access)
- TBD: link competitor research note when written

## Metadados originais

```yaml
---
date: 2025-09-15
updated: 2026-04-27
type: project
status: active
tags: [project, saas, habit-tracking]
related-people: ["[[people/Alex Rivera]]", "[[people/Sam Patel]]"]
related-projects: []
ai-first: true
---

```
