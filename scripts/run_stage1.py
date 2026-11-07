"""Thin wrapper around trival.cli.stage1 so this file runs without installing the package.

Usage:
    python scripts/run_stage1.py --input data/raw/corpus.csv --out data/output/stage1_results.xlsx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trival.cli import stage1  # noqa: E402

if __name__ == "__main__":
    stage1()
