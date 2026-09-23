---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-ia]
source: https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_podcast_transcript_schema.py
source_commit: 02fba47d3e4904caa2026d07f3cacfb4abfb34b9
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# tests/test_podcast_transcript_schema.py

Origem: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain/blob/02fba47d3e4904caa2026d07f3cacfb4abfb34b9/tests/test_podcast_transcript_schema.py). Versao consultada: 02fba47d3e49.

[[Cerebro/GitHub/Second-Brain/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/eugeniughelbur--obsidian-second-brain--02fba47d3e49.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""A JSON transcript that uses `segments[].text` must be read, not discarded.

`_parse_json_transcript` only accepted the Podcast Index spelling of the
per-segment string, `body`. Whisper-derived exports spell the same field
`text`, and several hosts ship those: flightcast (the host behind SOLVED with
Mark Manson, where this was found), Deepgram, AssemblyAI. On those feeds the
transcript tag resolved, the file downloaded, and the parser then returned None
and let the caller fall through to a show-notes-only summary. The user gets a
much thinner note with an empty Notable Quotes section, and nothing in the
output says a full transcript was in hand and dropped.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def test_whisper_style_text_segments_are_read():
    from research.lib.podcast import _parse_json_transcript

    # Shape as served by flightcast, extra Whisper fields included verbatim.
    body = json.dumps(
        {
            "segments": [
                {"start": 0.0, "end": 3.2, "text": "So a lot of people", "avg_logprob": -0.2},
                {"start": 3.2, "end": 6.1, "text": "don't know this.", "avg_logprob": -0.3},
            ]
        }
    )
    assert _parse_json_transcript(body) == "So a lot of people don't know this."


def test_podcast_index_body_segments_still_win():
    from research.lib.podcast import _parse_json_transcript

    body = json.dumps({"segments": [{"body": "first"}, {"body": "second"}]})
    assert _parse_json_transcript(body) == "first second"


def test_segments_with_neither_field_still_return_none():
    from research.lib.podcast import _parse_json_transcript

    body = json.dumps({"segments": [{"start": 0.0, "end": 1.0}]})
    assert _parse_json_transcript(body) is None


def test_empty_strings_do_not_count_as_a_transcript():
    from research.lib.podcast import _parse_json_transcript

    body = json.dumps({"segments": [{"text": ""}, {"text": "   "}]})
    assert _parse_json_transcript(body) is None

```
