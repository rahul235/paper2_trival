"""Thin wrapper around trival.cli.stage2_themes so this file runs without installing the package.

Usage:
    python scripts/run_stage2_themes.py --input data/raw/corpus.csv --themes data/output/stage1_results.xlsx --out data/output/stage2_theme_validation.xlsx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trival.cli import stage2_themes  # noqa: E402

if __name__ == "__main__":
    stage2_themes()
