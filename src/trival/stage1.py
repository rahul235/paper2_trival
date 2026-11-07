"""Stage 1 orchestrator: data -> embeddings -> UMAP -> HDBSCAN -> cTF-IDF -> topic naming.

Entry point for the full Stage 1 pipeline. Uses BERTopic's modular architecture
internally with the components wired via trival.* modules.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class Stage1Output:
    """Container for Stage 1 results."""
    assignments: pd.DataFrame   # title, abstract, cluster_id, probability
    topics: pd.DataFrame        # cluster_id, count, top_keywords, llm_label
    bertopic_model: object      # the fitted BERTopic model (for visualization)


def run_stage1(
    input_csv: str | Path,
    output_xlsx: str | Path,
    auto_tune: bool = False,
    label_topics_with_claude: bool = True,
) -> Stage1Output:
    """Full Stage 1 pipeline.

    Args:
        input_csv: path to the input corpus CSV (Scopus export format).
        output_xlsx: where to write the multi-sheet Excel result.
        auto_tune: if True, run the HDBSCAN grid search; else use CFG defaults.
        label_topics_with_claude: if True, call Claude to label clusters; else
            use BERTopic's default MMR + KeyBERT keyword labels.

    Returns:
        Stage1Output with the fitted BERTopic model (useful for visualization).
    """
    raise NotImplementedError  # TODO
