"""SBERT cosine-similarity classifier (deepset/sentence_bert).

Native output is cosine similarity in [-1, 1]; we shift-rescale to [0, 1]
in `classify` so all voices use the same scale.
"""
from __future__ import annotations

from functools import lru_cache

from trival.config import CFG


@lru_cache(maxsize=1)
def _get_model():
    """Lazy-load the SBERT tokenizer + model."""
    from transformers import AutoModel, AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(CFG.stage2.sbert_model)
    model = AutoModel.from_pretrained(CFG.stage2.sbert_model)
    return tokenizer, model


def classify(abstract: str, candidate_labels: list[str]) -> dict[str, float]:
    """Return {label: normalized_similarity} with scores in [0, 1].

    Steps: encode abstract and each label, mean-pool, compute cosine
    similarity, shift-rescale from [-1, 1] to [0, 1].
    """
    raise NotImplementedError  # TODO
