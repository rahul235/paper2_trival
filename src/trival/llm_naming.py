"""Claude-based topic labeling.

Replaces the LLaMA2-13B few-shot pipeline from the original TRIVALStage1.ipynb.
Default model is Claude Sonnet; configurable to Opus or Fable via CFG or
TRIVAL_CLAUDE_MODEL env var.

The prompt structure follows the original few-shot pattern:
  system: "You are a helpful, respectful, honest assistant for labeling topics."
  user:   example documents + keywords -> example label
          target documents + keywords -> please label
"""
from __future__ import annotations
from functools import lru_cache
from trival.config import CFG
from trival.auth import get_anthropic_key


EXAMPLE_DOCS: list[str] = []   # TODO: carry over the yoga/CAM example from the original notebook
EXAMPLE_KEYWORDS: str = ""     # TODO
EXAMPLE_LABEL: str = ""        # TODO


@lru_cache(maxsize=1)
def _get_client():
    """Lazy-load the Anthropic client (singleton)."""
    import anthropic
    return anthropic.Anthropic(api_key=get_anthropic_key())


def build_topic_prompt(documents: list[str], keywords: list[str]) -> str:
    """Build the user-message prompt for a single topic.

    Includes the few-shot example and the target documents + keywords.
    """
    raise NotImplementedError  # TODO


def label_topic(documents: list[str], keywords: list[str]) -> str:
    """Call Claude to produce a short topic label for one cluster.

    Returns a single-line topic label (no newlines, no quotes).
    """
    raise NotImplementedError  # TODO


def label_all_topics(topic_to_docs_keywords: dict[int, tuple[list[str], list[str]]]) -> dict[int, str]:
    """Label every topic in a BERTopic model.

    Args:
        topic_to_docs_keywords: mapping from cluster id to (representative_docs, keywords).

    Returns:
        mapping from cluster id to Claude-generated label.
    """
    raise NotImplementedError  # TODO
