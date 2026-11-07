"""Corpus I/O: read input CSVs, write result Excel/CSV.

Input CSVs follow the Scopus export format with columns `Title` and `Abstract`
(or `Article Title` and `Abstract` for the 996 variant); both are accepted.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

NA_VALUES = ["[No abstract available]", ""]
TITLE_COLUMNS = ("Title", "Article Title")
ABSTRACT_COLUMN = "Abstract"


def read_corpus_csv(path: str | Path) -> pd.DataFrame:
    """Read a corpus CSV and normalize column names.

    Returns a DataFrame with columns `title`, `abstract`, plus all other
    original columns preserved.

    Raises:
        FileNotFoundError: if the path does not exist.
        ValueError: if neither `Title` nor `Article Title` is present.
    """
    raise NotImplementedError  # TODO: implement in Subtask D


def extract_titles_and_abstracts(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Extract `title` and `abstract` series with NaN replaced by empty string.

    Used by both Stage 1 and Stage 2 to prepare inputs for downstream steps.
    """
    raise NotImplementedError  # TODO


def read_stage1_themes(path: str | Path) -> list[str]:
    """Read a Stage 1 output Excel/CSV and return the unique theme labels.

    The count is NOT fixed to 33 - it is whatever Stage 1 produced for the
    given corpus. Stage 2 uses this list as `candidate_labels`.
    """
    raise NotImplementedError  # TODO


def write_stage1_results(
    path: str | Path,
    df_assignments: pd.DataFrame,
    df_topics: pd.DataFrame,
    df_theme_counts: pd.DataFrame | None = None,
) -> None:
    """Write Stage 1 outputs as a multi-sheet Excel.

    Sheets:
        - `Assignments`: one row per abstract with its assigned cluster.
        - `Topics`: cluster id, count, top keywords, LLM-generated label.
        - `ThemeCounts`: optional journal x theme count matrix.
    """
    raise NotImplementedError  # TODO


def write_stage2_validation_report(
    path: str | Path,
    bart_scores: pd.DataFrame,
    sbert_scores: pd.DataFrame,
    gemini_scores: pd.DataFrame,
    consensus: pd.DataFrame,
    disagreements: pd.DataFrame,
    summary: pd.DataFrame,
) -> None:
    """Write the Stage 2 validation report as a multi-sheet Excel.

    All score DataFrames have the shape (n_abstracts, n_labels + metadata).
    `n_labels` is derived from the Stage 1 output, not hardcoded.
    """
    raise NotImplementedError  # TODO
