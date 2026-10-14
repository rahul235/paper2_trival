"""CLI entry: run Stage 1 on a corpus CSV, write multi-sheet Excel.

Usage:
    python scripts/run_stage1.py \
        --input data/raw/your_corpus.csv \
        --out data/output/stage1_results.xlsx
"""
from __future__ import annotations
import argparse
from pathlib import Path
from trival.stage1 import run_stage1


def main() -> None:
    parser = argparse.ArgumentParser(description="Run TRIVAL Stage 1 pipeline.")
    parser.add_argument("--input", type=Path, required=True, help="Input corpus CSV (Scopus format).")
    parser.add_argument("--out", type=Path, required=True, help="Output xlsx path.")
    parser.add_argument("--auto-tune", action="store_true", help="Run HDBSCAN grid search.")
    parser.add_argument("--no-claude-labels", action="store_true", help="Skip Claude topic naming.")
    args = parser.parse_args()

    run_stage1(
        input_csv=args.input,
        output_xlsx=args.out,
        auto_tune=args.auto_tune,
        label_topics_with_claude=not args.no_claude_labels,
    )


if __name__ == "__main__":
    main()
