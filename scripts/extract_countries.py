"""Thin wrapper around trival.cli.countries so this file runs without installing the package.

Usage:
    python scripts/extract_countries.py --input data/raw/corpus.csv --out data/output/abstracts_with_countries.csv
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trival.cli import countries  # noqa: E402

if __name__ == "__main__":
    countries()
