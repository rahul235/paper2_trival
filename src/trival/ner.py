"""spaCy-based named-entity extraction (country names from abstracts).

Ported from the final cells of TRIVALStage2_996Article.ipynb. Optional
utility - not part of the Stage 2 ensemble.

Setup: `python -m spacy download en_core_web_sm` once.
"""
from __future__ import annotations

from functools import lru_cache


@lru_cache(maxsize=1)
def _get_nlp():
    """Lazy-load spaCy's small English model (singleton)."""
    import spacy
    return spacy.load("en_core_web_sm")


def extract_countries(abstract: str) -> list[str]:
    """Return unique GPE entities from an abstract.

    Uses spaCy's small English NER model and the GPE entity label.
    A GPE is a geopolitical entity: country, city, state, etc.
    """
    raise NotImplementedError  # TODO


def extract_countries_bulk(abstracts: list[str]) -> list[list[str]]:
    """Apply `extract_countries` to a list of abstracts."""
    raise NotImplementedError  # TODO
