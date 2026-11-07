"""Central configuration: hyperparameters, model IDs, paths.

Every value here can be overridden by an environment variable prefixed `TRIVAL_`.
All business-logic modules import from here instead of hardcoding values.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]
DATA_RAW_DIR: Path = PROJECT_ROOT / "data" / "raw"
DATA_OUTPUT_DIR: Path = PROJECT_ROOT / "data" / "output"

# Load .env before any setting below reads the environment, so TRIVAL_* overrides
# placed in .env take effect (e.g. TRIVAL_CLAUDE_MODEL=claude-opus-5-5).
load_dotenv(PROJECT_ROOT / ".env", override=False)


# ---------------------------------------------------------------------------
# Stage 1: Embeddings + Clustering + Topic naming
# ---------------------------------------------------------------------------
@dataclass
class Stage1Config:
    # Embedding model (BAAI/bge-small-en matches the paper's choice)
    embedding_model: str = os.getenv("TRIVAL_EMBEDDING_MODEL", "BAAI/bge-small-en")

    # UMAP
    umap_n_neighbors: int = int(os.getenv("TRIVAL_UMAP_NEIGHBORS", "40"))
    umap_n_components: int = int(os.getenv("TRIVAL_UMAP_COMPONENTS", "5"))
    umap_min_dist: float = float(os.getenv("TRIVAL_UMAP_MIN_DIST", "0.0"))
    umap_metric: str = os.getenv("TRIVAL_UMAP_METRIC", "cosine")
    umap_random_state: int = int(os.getenv("TRIVAL_UMAP_SEED", "42"))

    # HDBSCAN (final tuned values from the original paper)
    hdbscan_min_cluster_size: int = int(os.getenv("TRIVAL_HDBSCAN_MIN_CLUSTER", "3"))
    hdbscan_min_samples: int = int(os.getenv("TRIVAL_HDBSCAN_MIN_SAMPLES", "3"))
    hdbscan_metric: str = os.getenv("TRIVAL_HDBSCAN_METRIC", "euclidean")
    hdbscan_cluster_selection_method: str = os.getenv("TRIVAL_HDBSCAN_SELECTION", "eom")

    # Grid search ranges (used when auto-tuning hyperparameters)
    gs_min_samples_range: tuple[int, ...] = (3, 4, 5, 6, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55)
    gs_min_cluster_range: tuple[int, ...] = (3, 4, 5, 6, 7, 10, 15, 20, 25)
    gs_selection_methods: tuple[str, ...] = ("eom", "leaf")

    # BERTopic
    bertopic_top_n_words: int = 10

    # Claude for topic naming. Default Sonnet; to switch, set in .env:
    #   TRIVAL_CLAUDE_MODEL=claude-opus-5-5   (or claude-fable-5-1)
    claude_model: str = os.getenv("TRIVAL_CLAUDE_MODEL", "claude-sonnet-5-5")
    claude_max_tokens: int = int(os.getenv("TRIVAL_CLAUDE_MAX_TOKENS", "500"))
    claude_temperature: float = float(os.getenv("TRIVAL_CLAUDE_TEMPERATURE", "0.1"))

    # Few-shot example for topic labeling (one example by default; override to add more)
    fsl_num_example_docs: int = 5


# ---------------------------------------------------------------------------
# Stage 2: Ensemble validation
# ---------------------------------------------------------------------------
@dataclass
class Stage2Config:
    # BART (Meta - NLI)
    bart_model: str = os.getenv("TRIVAL_BART_MODEL", "facebook/bart-large-mnli")

    # SBERT (deepset - cosine similarity)
    sbert_model: str = os.getenv("TRIVAL_SBERT_MODEL", "deepset/sentence_bert")

    # Gemini (Google - LLM-as-judge)
    gemini_model: str = os.getenv("TRIVAL_GEMINI_MODEL", "gemini-2.5-flash")
    gemini_max_output_tokens: int = int(os.getenv("TRIVAL_GEMINI_MAX_TOKENS", "2000"))

    # Ensemble aggregation
    ensemble_voices: tuple[str, ...] = ("bart", "sbert", "gemini")
    tie_breaker: str = "weighted_score_sum"  # or "random", "first_voice"

    # Classification task
    multi_label: bool = True
    high_confidence_threshold: float = 0.8


@dataclass
class AppConfig:
    stage1: Stage1Config = field(default_factory=Stage1Config)
    stage2: Stage2Config = field(default_factory=Stage2Config)


# Global singleton (importable as `from trival.config import CFG`)
CFG = AppConfig()
