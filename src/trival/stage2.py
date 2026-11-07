"""Stage 2 orchestrator: per-abstract classification by ensemble + majority vote.

Takes any list of candidate labels (NOT hardcoded to 33 or any other count)
and runs each abstract through the configured voices.

Voices:
    - BART (facebook/bart-large-mnli, zero-shot NLI)
    - SBERT (deepset/sentence_bert, cosine similarity)
    - Gemini (gemini-2.5-flash, LLM-as-judge via structured output)

Aggregation: majority vote on argmax(normalized_score); ties broken by
weighted score sum.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class Stage2Output:
    """Container for Stage 2 results."""
    bart_scores: pd.DataFrame        # one row per abstract, one col per candidate label
    sbert_scores: pd.DataFrame
    gemini_scores: pd.DataFrame
    consensus: pd.DataFrame          # top label per voice + agreement flags
    disagreements: pd.DataFrame      # subset where voices disagree
    summary: pd.DataFrame            # per-label counts and confidence stats


def validate_abstracts(
    abstracts: list[str],
    candidate_labels: list[str],
    titles: list[str] | None = None,
    stage1_cluster_assignments: list[str] | None = None,
    voices: tuple[str, ...] = ("bart", "sbert", "gemini"),
) -> Stage2Output:
    """Classify every abstract against every candidate label.

    Works with ANY number of labels and ANY number of voices. The theme
    count is derived from `candidate_labels` (which is produced by Stage 1
    on the current corpus, not hardcoded).

    Args:
        abstracts: list of abstract strings.
        candidate_labels: labels to classify against (e.g., Stage 1 themes,
            or [qualitative, quantitative, mixed] for method classification).
        titles: optional abstract titles for the output report.
        stage1_cluster_assignments: optional Stage 1 cluster labels per
            abstract, used to compute Stage1-vs-ensemble agreement.
        voices: which classifiers to include in the ensemble.

    Returns:
        Stage2Output with per-voice scores, consensus, disagreements, summary.
    """
    raise NotImplementedError  # TODO


def run_stage2_themes(
    input_csv: str | Path,
    stage1_output: str | Path,
    output_xlsx: str | Path,
) -> Stage2Output:
    """Full-corpus theme validation.

    Reads the Stage 1 themes from `stage1_output`, then validates every
    abstract in `input_csv` against those themes.
    """
    raise NotImplementedError  # TODO


def run_stage2_methods(
    input_csv: str | Path,
    output_xlsx: str | Path,
    method_labels: list[str] | None = None,
) -> Stage2Output:
    """Research-method classification (qualitative / quantitative / mixed).

    Reuses the same ensemble but with a different candidate_labels list.
    Default labels match the original TRIVALStage2_996Article.ipynb.
    """
    raise NotImplementedError  # TODO
