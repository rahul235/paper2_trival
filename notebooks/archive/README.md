# Archived original notebooks

These are the Colab notebooks that the `src/trival/` package was refactored from.
Keep for reference; they are **not maintained** going forward.

| Notebook | What it does | Status |
|---|---|---|
| `TRIVALStage1.ipynb` | BERTopic + LLaMA2-13B topic naming (Colab, GPU) | Superseded by `src/trival/stage1.py` + Claude API |
| `TRIVALStage2.ipynb` | Illustrative: 2 hardcoded abstracts vs 33 themes | Superseded by `src/trival/stage2.py` (ensemble) |
| `TRIVALStage2_996Article.ipynb` | Full-corpus BART + SBERT method classification | Superseded by `scripts/run_stage2_methods.py` |

Live code location:
- Modules: `src/trival/`
- Entry points: `scripts/run_stage1.py`, `scripts/run_stage2_themes.py`, `scripts/run_stage2_methods.py`

Original folder on disk: `/Users/Rahul/Documents/RahulOffice/Research/Thesis/RQ1 & RQ 2/Paper2/Paper2_Condensed/BertWithLlama2/`.
