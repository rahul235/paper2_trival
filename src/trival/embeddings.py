"""Sentence-level embedding wrappers.

Primary: BAAI/bge-small-en (Stage 1 BERTopic input).
Secondary: deepset/sentence_bert (Stage 2 cosine-similarity voice).

Both load lazily on first use; expect a one-time ~100 MB download per model.
"""
from __future__ import annotations
from functools import lru_cache
import numpy as np
from trival.config import CFG


@lru_cache(maxsize=2)
def _load_sentence_transformer(model_name: str):
    """Lazy-load a SentenceTransformer model and cache it per process."""
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(model_name)


def encode_abstracts(abstracts: list[str], model_name: str | None = None) -> np.ndarray:
    """Encode a list of abstracts into dense vectors.

    Args:
        abstracts: list of abstract strings.
        model_name: SentenceTransformer model id. Defaults to CFG.stage1.embedding_model.

    Returns:
        np.ndarray of shape (n_abstracts, embedding_dim).
    """
    raise NotImplementedError  # TODO
