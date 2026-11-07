"""Thin wrapper around trival.cli.stage2_methods so this file runs without installing the package.

Usage:
    python scripts/run_stage2_methods.py --input data/raw/corpus.csv --out data/output/stage2_method_classification.xlsx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trival.cli import stage2_methods  # noqa: E402

if __name__ == "__main__":
    stage2_methods()
