"""BERTopic visualization wrappers.

Thin wrappers around `topic_model.visualize_documents` and friends. The
output is a plotly Figure; render in a notebook or save to HTML.
"""
from __future__ import annotations

import numpy as np


def visualize_document_clusters(
    topic_model,
    titles: list[str],
    reduced_embeddings: np.ndarray | None = None,
    output_html: str | None = None,
) -> object:
    """Render the document cluster scatter plot.

    Args:
        topic_model: a fitted BERTopic model.
        titles: document titles for hover text.
        reduced_embeddings: optional pre-computed 2D UMAP projection.
        output_html: optional path to save the plot as a standalone HTML file.

    Returns:
        A plotly Figure.
    """
    raise NotImplementedError  # TODO
