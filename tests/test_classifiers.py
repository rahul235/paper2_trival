"""Tests for Stage 2 classifiers (all mocked - no external API calls here)."""
import pytest


@pytest.mark.integration
def test_bart_classify_returns_normalized_scores():
    """Integration test: downloads BART weights. Run with pytest -m integration."""
    pytest.skip("not implemented yet")


def test_sbert_normalization_range():
    """TODO: verify SBERT scores are mapped to [0, 1]."""
    pytest.skip("not implemented yet")


def test_gemini_prompt_builder_is_pure():
    """TODO: verify _build_prompt produces deterministic output for same inputs."""
    pytest.skip("not implemented yet")
