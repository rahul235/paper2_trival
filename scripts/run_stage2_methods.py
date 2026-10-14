"""CLI entry: research-method classification.

Classifies each abstract as qualitative, quantitative, or mixed method
(labels configurable). Reuses the same Stage 2 ensemble but with a
different candidate_labels list.

Usage:
    python scripts/run_stage2_methods.py \
        --input data/raw/your_corpus.csv \
        --out data/output/stage2_method_classification.xlsx
"""
from __future__ import annotations
import argparse
from pathlib import Path
from trival.stage2 import run_stage2_methods


DEFAULT_METHOD_LABELS = [
    "The article uses qualitative research method",
    "The article uses quantitative research method",
    "The article uses mixed method for study",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run TRIVAL Stage 2 method classification.")
    parser.add_argument("--input", type=Path, required=True, help="Input corpus CSV.")
    parser.add_argument("--out", type=Path, required=True, help="Output xlsx path.")
    parser.add_argument("--labels", nargs="+", default=DEFAULT_METHOD_LABELS, help="Candidate labels.")
    args = parser.parse_args()

    run_stage2_methods(
        input_csv=args.input,
        output_xlsx=args.out,
        method_labels=args.labels,
    )


if __name__ == "__main__":
    main()
