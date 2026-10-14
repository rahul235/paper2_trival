"""BART zero-shot NLI classifier (facebook/bart-large-mnli).

Uses the transformers `zero-shot-classification` pipeline. Native output
is already in [0, 1] per label, so no normalization is needed.
"""
from __future__ import annotations
from functools import lru_cache
from trival.config import CFG


@lru_cache(maxsize=1)
def _get_classifier():
    """Lazy-load the BART pipeline (singleton, large download first time)."""
    from transformers import pipeline
    return pipeline("zero-shot-classification", model=CFG.stage2.bart_model)


def classify(abstract: str, candidate_labels: list[str]) -> dict[str, float]:
    """Return {label: probability} with probabilities in [0, 1].

    Uses multi_label=True so scores are independent per label.
    """
    raise NotImplementedError  # TODO
