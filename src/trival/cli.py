"""Command-line entry points for TRIVAL.

Installed as console scripts by pyproject.toml:
    trival-stage1          -> stage1()
    trival-stage2-themes   -> stage2_themes()
    trival-stage2-methods  -> stage2_methods()
    trival-countries       -> countries()

The files in scripts/ are thin wrappers around these functions, so
`python scripts/run_stage1.py ...` also works without installing the package.
"""
from __future__ import annotations

import argparse
from pathlib import Path

DEFAULT_METHOD_LABELS = [
    "The article uses qualitative research method",
    "The article uses quantitative research method",
    "The article uses mixed method for study",
]


def stage1(argv: list[str] | None = None) -> None:
    """Run Stage 1 on a corpus CSV and write a multi-sheet Excel."""
    parser = argparse.ArgumentParser(prog="trival-stage1", description="Run TRIVAL Stage 1 pipeline.")
    parser.add_argument("--input", type=Path, required=True, help="Input corpus CSV (Scopus format).")
    parser.add_argument("--out", type=Path, required=True, help="Output xlsx path.")
    parser.add_argument("--auto-tune", action="store_true", help="Run HDBSCAN grid search.")
    parser.add_argument("--no-claude-labels", action="store_true", help="Skip Claude topic naming.")
    args = parser.parse_args(argv)

    from trival.stage1 import run_stage1

    run_stage1(
        input_csv=args.input,
        output_xlsx=args.out,
        auto_tune=args.auto_tune,
        label_topics_with_claude=not args.no_claude_labels,
    )


def stage2_themes(argv: list[str] | None = None) -> None:
    """Validate every abstract against the themes Stage 1 produced for this corpus.

    The number of themes comes from the Stage 1 output file; nothing is hardcoded.
    """
    parser = argparse.ArgumentParser(
        prog="trival-stage2-themes", description="Run TRIVAL Stage 2 theme validation."
    )
    parser.add_argument("--input", type=Path, required=True, help="Input corpus CSV.")
    parser.add_argument("--themes", type=Path, required=True, help="Stage 1 output xlsx.")
    parser.add_argument("--out", type=Path, required=True, help="Output xlsx path.")
    args = parser.parse_args(argv)

    from trival.stage2 import run_stage2_themes

    run_stage2_themes(input_csv=args.input, stage1_output=args.themes, output_xlsx=args.out)


def stage2_methods(argv: list[str] | None = None) -> None:
    """Classify each abstract by research method (labels configurable)."""
    parser = argparse.ArgumentParser(
        prog="trival-stage2-methods", description="Run TRIVAL Stage 2 method classification."
    )
    parser.add_argument("--input", type=Path, required=True, help="Input corpus CSV.")
    parser.add_argument("--out", type=Path, required=True, help="Output xlsx path.")
    parser.add_argument("--labels", nargs="+", default=DEFAULT_METHOD_LABELS, help="Candidate labels.")
    args = parser.parse_args(argv)

    from trival.stage2 import run_stage2_methods

    run_stage2_methods(input_csv=args.input, output_xlsx=args.out, method_labels=args.labels)


def countries(argv: list[str] | None = None) -> None:
    """Extract country mentions from abstracts with spaCy NER and write a CSV."""
    parser = argparse.ArgumentParser(
        prog="trival-countries", description="Extract country mentions from abstracts."
    )
    parser.add_argument("--input", type=Path, required=True, help="Input corpus CSV.")
    parser.add_argument("--out", type=Path, required=True, help="Output CSV path.")
    args = parser.parse_args(argv)

    import pandas as pd

    from trival.io import extract_titles_and_abstracts, read_corpus_csv
    from trival.ner import extract_countries_bulk

    df = read_corpus_csv(args.input)
    titles, abstracts = extract_titles_and_abstracts(df)
    found = extract_countries_bulk(abstracts.tolist())
    pd.DataFrame(
        {"title": titles, "abstract": abstracts, "countries": ["; ".join(c) for c in found]}
    ).to_csv(args.out, index=False)
