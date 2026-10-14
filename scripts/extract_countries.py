"""CLI entry: extract country mentions from abstracts via spaCy NER.

Usage:
    python scripts/extract_countries.py \
        --input data/raw/your_corpus.csv \
        --out data/output/abstracts_with_countries.csv
"""
from __future__ import annotations
import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract country mentions from abstracts.")
    parser.add_argument("--input", type=Path, required=True, help="Input corpus CSV.")
    parser.add_argument("--out", type=Path, required=True, help="Output CSV path.")
    args = parser.parse_args()

    from trival.io import read_corpus_csv, extract_titles_and_abstracts
    from trival.ner import extract_countries_bulk

    df = read_corpus_csv(args.input)
    titles, abstracts = extract_titles_and_abstracts(df)
    countries = extract_countries_bulk(abstracts.tolist())
    # TODO: write to CSV with title, abstract, countries columns


if __name__ == "__main__":
    main()
