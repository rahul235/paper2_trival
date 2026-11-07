"""Gemini LLM-as-judge classifier (gemini-2.5-flash).

Uses structured output (JSON) to get a numeric score per candidate label.
The prompt frames the task as 'score how well this abstract fits each
label', with the model returning a JSON object. Scores are divided by 100
to normalize to [0, 1].
"""
from __future__ import annotations

from functools import lru_cache

from trival.auth import get_gemini_key


@lru_cache(maxsize=1)
def _get_client():
    """Lazy-load the Gemini client (singleton), using the google-genai SDK.

    Calls then pass the model id each time:
        _get_client().models.generate_content(model=CFG.stage2.gemini_model, contents=...)
    """
    from google import genai
    return genai.Client(api_key=get_gemini_key())


def _build_prompt(abstract: str, candidate_labels: list[str]) -> str:
    """Build the judge prompt that asks for a JSON score object."""
    raise NotImplementedError  # TODO


def classify(abstract: str, candidate_labels: list[str]) -> dict[str, float]:
    """Return {label: score} with scores normalized to [0, 1].

    Calls Gemini with a structured-output prompt, parses the JSON response,
    and divides scores by 100.
    """
    raise NotImplementedError  # TODO
