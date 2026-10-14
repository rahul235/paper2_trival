"""CLI entry: full-corpus theme validation.

Reads the themes from a Stage 1 output file, then validates every abstract
in the input corpus against those themes (BART + SBERT + Gemini ensemble).

The number of themes is derived from the Stage 1 output - no hardcoded count.

Usage:
    python scripts/run_stage2_themes.py \
        --input data/raw/your_corpus.csv \
        --themes data/output/stage1_results.xlsx \
        --out data/output/stage2_theme_validation.xlsx
"""
from __future__ import annotations
import argparse
from pathlib import Path
from trival.stage2 import run_stage2_themes


def main() -> None:
    parser = argparse.ArgumentParser(description="Run TRIVAL Stage 2 theme validation.")
    parser.add_argument("--input", type=Path, required=True, help="Input corpus CSV.")
    parser.add_argument("--themes", type=Path, required=True, help="Stage 1 output xlsx.")
    parser.add_argument("--out", type=Path, required=True, help="Output xlsx path.")
    args = parser.parse_args()

    run_stage2_themes(
        input_csv=args.input,
        stage1_output=args.themes,
        output_xlsx=args.out,
    )


if __name__ == "__main__":
    main()
