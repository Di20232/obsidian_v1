---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/x_read.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# scripts/research/x_read.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/scripts/research/x_read.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
#!/usr/bin/env python3
"""/x-read [url] - deep-read an X post via Grok's x_search tool.

Output: original post (verbatim) + TL;DR + key claims + reply sentiment + voices.
Default behavior: print to chat. Does NOT save to vault unless the user explicitly asks.
"""

import sys

from .lib import grok

PROMPT_TEMPLATE = """Analyze this X post and return a structured deep-read.

URL: {url}

Use live X access to fetch the original post AND its replies/thread. Then return EXACTLY this structure (markdown), nothing else:

ORIGINAL POST
[verbatim text from the post - do not paraphrase. Include the author's @ handle and post timestamp if available.]

THREAD
[If the author posted a thread chained from this post, include the verbatim text of the next 1-5 posts in order. If no thread, write "No thread."]

TL;DR
[1-2 sentences capturing the core message of the post.]

KEY CLAIMS
- [bulleted list of distinct factual or opinion claims made in the post]

REPLY SENTIMENT
[Approximate breakdown like "~70% positive, 20% skeptical, 10% off-topic" based on the actual replies you can see. If you cannot fetch replies, write "Unable to fetch replies - sentiment not assessed."]

NOTABLE COUNTER-ARGUMENTS
- [bulleted list of substantive pushback from replies, with the @ handle of the replier in brackets]
- [If no notable counters, write "None observed."]

VOICES TO WATCH
- [@handles of replies with substantive engagement - people whose follow-up posts add real signal]
- [If unable to assess, write "Could not identify."]

Rules:
- Do NOT add commentary, opinion, or framing outside this structure.
- Do NOT include source URLs at the end - they are not needed.
- The post text in ORIGINAL POST must be verbatim, not summarized.
"""


def main(argv: list[str]) -> int:
    if len(argv) < 2 or not argv[1].strip():
        print("Usage: /x-read <x-post-url>", file=sys.stderr)
        return 2

    url = argv[1].strip()
    if "x.com" not in url and "twitter.com" not in url:
        print(f"⚠️  URL doesn't look like an X/Twitter post: {url}", file=sys.stderr)
        print("Continuing anyway - Grok will tell us if it can't fetch.", file=sys.stderr)

    prompt = PROMPT_TEMPLATE.format(url=url)
    print(f"[/x-read] Fetching {url} via Grok x_search...\n", file=sys.stderr)

    try:
        result = grok.call(
            prompt,
            command="x-read",
            tools=[{"type": "x_search"}],
            max_output_tokens=3000,
        )
    except SystemExit:
        raise
    except Exception as e:
        print(f"\n❌ /x-read failed: {e}", file=sys.stderr)
        return 1

    print(result["text"])
    approx = "~" if result.get("cost_is_estimate") else ""
    print(
        f"\n---\n[cost: {approx}${result['cost_usd']:.4f} · {result.get('model', '?')}"
        f" · tokens in/out: {result['input_tokens']}/{result['output_tokens']}]",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

```
