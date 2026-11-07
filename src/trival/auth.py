"""API-key loading (via python-dotenv).

Usage:
    from trival.auth import get_anthropic_key, get_gemini_key
"""
from __future__ import annotations

import os

import trival.config  # noqa: F401  (importing config loads .env from the project root)


class MissingAPIKeyError(RuntimeError):
    """Raised when a required API key is not set in the environment."""


def _require(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise MissingAPIKeyError(
            f"{name} is not set. Add it to .env or export it in your shell."
        )
    return value


def get_anthropic_key() -> str:
    """Return the Anthropic API key or raise."""
    return _require("ANTHROPIC_API_KEY")


def get_gemini_key() -> str:
    """Return the Google Gemini API key or raise."""
    return _require("GEMINI_API_KEY")


def get_hf_token() -> str | None:
    """Return the HuggingFace token if set, otherwise None (public models work without one)."""
    return os.getenv("HF_TOKEN")
