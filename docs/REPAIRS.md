# Maintenance and validation — 2026-10-20

The detailed portfolio documentation prepared on 2026-10-12 is now reviewed for
publication on top of the existing remote history. The prior two remote README
commits remain in Git history. Their project subjects and reported results are
covered by the detailed guides, with stronger unsupported claims replaced by
explicit source/evaluation boundaries.

## Focused source repairs

| File | Observed issue | Change | Verification boundary |
|---|---|---|---|
| [yahoo_fin_ex.py](<../crypto_market_prediction_project-DB_DL_combined/갈대 AI/yahoo_fin_ex.py>) | Ten notebook-only `!pip` commands cause ordinary Python syntax errors. | Preserve those commands as comments; clarify that standard-library names are not pip requirements. | Source parses. Network APIs and third-party compatibility were not exercised. |
| [갈대_AI_LSTM_최적화.py](<../crypto_market_prediction_project-DB_DL_combined/갈대 AI/갈대_AI_LSTM_최적화.py>) | Eight notebook-only `!pip` commands and a commented-out format continuation prevent Python parsing. | Preserve commands as comments and restore the threshold-report formatting expression. | Source parses; two focused helper cases pass without importing the script. File loads, training, model writes and trained-model inference were not run. |

All other original Python files and all notebooks, saved outputs, original
figures and datasets retain their contents. Commenting notebook shell commands
does not make these top-level scripts safe import targets: they still contain
external actions. Read the [execution guide](REPRODUCIBILITY.md) first.

The export's standalone Windows-path literal is now a raw string, preventing an
invalid-escape warning while preserving its displayed path. The threshold helper
still assumes a nonempty collection, matching its teaching use; its test is not
a model or dataset evaluation.

## Checks performed

- Read-only structure/link check: `python tools/validate_documentation.py`.
- Python AST parsing for all four original scripts; no script was imported.
- Two offline threshold-report cases: `python -m unittest discover -s tests -v`.
- JSON structure for all 67 original notebooks, including 13 tracked checkpoints.
- Markdown local targets, image references, anchors, UTF-8 and SVG structure.
- Byte comparison of the four extracted PNGs against their notebook image output.
- Git diff, explicit staged paths and exclusion of local health datasets.
- Original-worktree preservation baseline and remote SHA verification during publication.

These are documentation and syntax checks, not model validation. Reported
project results, saved notebook metrics and a new run remain distinct. No
training, crawler requests, DB access, source-data redistribution or environment
installation was performed.

Historical limitations remain documented: the EV repeated-lag smoother,
pre-split health scaling, sentiment loss/accuracy labeling and price-model
evaluation protocol were not silently reinterpreted as corrected experiments.

## Observed validation result

The final local structure check parsed six Python files (four original exports
plus the new validator/test), 67 notebook JSON files, 24 Markdown files, 353 local
references and five SVGs without errors. Both isolated helper tests passed.
Four extracted PNGs match the original output bytes; the root README was rendered
locally and visually inspected. The 77 original tracked files outside the root
README and two repaired exports remain unchanged relative to the remote base.
