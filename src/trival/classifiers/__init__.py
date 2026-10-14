"""Stage 2 ensemble voices.

Each classifier exposes a `classify(abstract, candidate_labels)` function
that returns a dict `{label: score}` with scores normalized to [0, 1].
"""
