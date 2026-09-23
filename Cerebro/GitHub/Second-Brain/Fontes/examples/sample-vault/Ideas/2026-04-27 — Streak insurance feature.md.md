---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/examples/sample-vault/Ideas/2026-04-27%20%E2%80%94%20Streak%20insurance%20feature.md
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# examples/sample-vault/Ideas/2026-04-27 — Streak insurance feature.md

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/examples/sample-vault/Ideas/2026-04-27%20%E2%80%94%20Streak%20insurance%20feature.md). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.


# Streak insurance feature

## For future agent

Idea captured on 2026-04-27 about a "streak insurance" feature for <code>[[Projects/Tide]]</code>. Status: captured. The body explains the idea, why it's interesting, and what would make it real. If shelved later, the reason will be documented at the bottom. Owner: <code>[[people/Alex Rivera]]</code>.

## The idea

Let users buy or earn "streak insurance" days that absorb missed habits without breaking the tide level. Two variants worth exploring:

- **Earned variant:** users earn one insurance day per 14 consecutive days of activity, capped at 3 in the bank
- **Paid variant:** Tide Plus subscribers get 5 insurance days per month, automatically applied

## Why it's interesting

- Solves the "I missed one day on vacation, lost my whole streak" complaint that drove the <code>[[Projects/Tide]]</code> retention rebuild
- Earned variant reinforces consistent users without changing pricing
- Paid variant gives Tide Plus a tangible "save" moment, which converts better than abstract benefits in habit-app pricing pages (confidence: `medium`, single-source observation, TBD: cite habit-app pricing study)

## What would make it real

- Decide: feature inside <code>[[Projects/Tide]]</code> or its own product entirely?
- Mockup the "insurance applied" UI moment (the apology-receipt language matters)
- Validate with 5 paying users before building (`stated` interview required)
- Database: extend the `streaks` table with `insurance_balance` and `insurance_applied_at` columns

## Risks

- Could feel gamey, which contradicts Tide's calmer-streak positioning. Counter: framing as "rest credit" rather than "insurance" might fix the tone (confidence: `speculation`).
- Earned variant complicates the tide-level math that just got rebuilt this week

## Next step

Promote to a feature spec inside <code>[[Projects/Tide]]</code> if the rebuild ships clean and user feedback on the calmer-streak framing comes back positive. Decision date: TBD, expected post-2026-05-08 (v0.9.0 ship).

## Sources

- Origin: pair session with <code>[[people/Sam Patel]]</code> on 2026-04-27, see <code>[[wiki/logs/2026-04-27 — Tide retention rebuild]]</code>
- Adjacent: TBD competitor research on rest mechanics

## Metadados originais

```yaml
---
date: 2026-04-27
type: idea
tags: [idea, tide, retention, monetization]
status: captured
related-projects: ["[[Projects/Tide]]"]
ai-first: true
---

```
