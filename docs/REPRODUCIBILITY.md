# Reading & Reproducing the Archive

[Portfolio](../README.md) · [Evidence register](PROJECT_EVIDENCE.md) · [Complete artifact catalog](NOTEBOOK_CATALOG.md)

This guide separates **reading the preserved work** from **restoring an execution environment**. The original projects are from 2021; the October 2026 documentation pass inspected source and saved outputs without executing training, crawling, or database-writing cells.

## Choose your route

| Goal | Suggested route |
|---|---|
| Understand the projects | Read the four project READMEs and their linked representative notebooks. |
| Inspect the results | Read existing outputs together with the [evidence register](PROJECT_EVIDENCE.md); verify what each metric measures. |
| Restore a representative experiment | Establish the matching input data, model artifacts, package/API compatibility, and a working-copy path configuration first. |
| Rebuild a web prototype or service | Treat it as separate restoration work; the complete historical web application and deployment configuration are not included here. |

### Notebook viewing

The `.ipynb` files can be inspected as notebook artifacts without rerunning their cells. For local viewing, an isolated JupyterLab environment is a possible starting point:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install jupyterlab
jupyter lab
```

These are suggested viewer setup commands, not a claim that the 2021 model dependencies have been installed or validated. Do not select “Run All” merely to read the notebooks.

## Dependency map

Imports provide candidate dependency groups; this table is **not a lockfile**. Some imports occur only in experimental cells.

| Collection | Candidate package groups observed | Compatibility considerations |
|---|---|---|
| EV analysis | pandas, NumPy, Matplotlib, Requests, BeautifulSoup (`bs4`), Selenium | Browser/driver pairing, historical selectors and browser APIs, Excel engine, Korean plotting font. |
| Health prediction | pandas, NumPy, Matplotlib, Seaborn, SciPy, statsmodels, scikit-learn, Graphviz | Old model argument names, rendering dependencies, CP949 input, and transformation/evaluation order. |
| Cryptocurrency research | Above analytical packages plus TensorFlow/Keras, NLTK, Plotly, Cufflinks, pyecharts, PyMySQL, SQLAlchemy | External language resources, model formats, notebook state, historical plotting/database APIs, and Colab imports. |
| Korean NLP / integration | TensorFlow/Keras, scikit-learn, KoNLPy/Okt, tqdm, Requests, BeautifulSoup, PyMySQL, SQLAlchemy; `yahoo_fin` in the example file | Java-backed morphological analysis, external model/array files, Excel inputs, legacy training APIs, and crawler effects. |

The inspected local Python interpreter was **3.11.5** at setup. That observation does not establish compatibility with the project's original environment. Version pins should be derived from a tested restoration rather than guessed from the year or current interpreter.

## Electric vehicle analysis

**Start reading:** [project overview](../Electric_vehicle_trend-Visualization_Analysis/README.md), then the two `portfolio_team1` notebooks.

| Referenced input | Purpose | Repository availability |
|---|---|---|
| One-year EV country-ranking Excel export | Short-window country comparison | Not in the original tracked files. |
| Five-year EV country-ranking Excel export | Longer-window country comparison | Not in the original tracked files. |
| Long-term global EV-topic CSV | Monthly series beginning in 2004 | Not in the original tracked files. |
| ChromeDriver and Google Trends page | Browser-based collection | External tooling and service. |

Historical examples include `electric_vehicle_serach_ranktoday%201-y.xlsx`, `electric_vehicle_serach_ranktoday%205-y.xlsx`, and `17년 세계전기차주제 검색 상대적 추의.csv` under `c:/My_data/`.

Before rebuilding the charts:

1. Recover or newly export data with a recorded topic, geography, time range, and retrieval date.
2. Keep historical exports separate from fresh exports; a new download is not the 2021 snapshot.
3. Match countries by name/code instead of using row count alone.
4. Review the original repeated-lag smoothing expression and define the intended moving average for any new result.
5. Use a Korean-capable font and record the source/export normalization context.

Original figures are preserved in `assets/readme/`; their provenance is in [SOURCES.md](../assets/readme/SOURCES.md). Google explains the normalized nature of Trends data in its [official FAQ](https://support.google.com/trends/answer/4365533?hl=en).

## Health prediction

**Start reading:** [project overview](../BP_BG_prediction-Machine_Deep_Learning/README.md), then `Data_overview_천준.ipynb` and the consolidated glucose notebook.

| Referenced input or artifact | Purpose | Current status |
|---|---|---|
| `NHIS_OPEN_GJ_2017_v1.1.csv` | Representative health-model input | Referenced by source; matching file not tracked. |
| Local `DataSets/` CSV files with 2020 filenames | Existing local material | Preserved on disk and ignored from routine Git staging; compatibility and usage conditions not verified. |
| Parameter-search result CSVs | Saved forest/tree comparison tables | Referenced under historical local paths; not tracked in the original repository inventory. |
| Standalone PNG figures | Exploratory visualizations | Six original figures are tracked in the health folder. |

The representative source reads CP949 text and expects Korean columns for age/sex/region, body measurements, lifestyle indicators, glucose, and related health fields. Do not replace the input with a different year without checking field definitions, coding, missingness, and sampling.

For a new evaluation, retain a separate working copy and:

- Establish whether the task is continuous prediction or a specified threshold classification.
- Split before fitting preprocessing, including scaling and any learned feature transformations.
- Preserve label definitions and target units.
- Use validation for parameter selection and a final holdout for reporting.
- Report class frequencies, a simple baseline, confusion matrices, and relevant errors rather than accuracy alone.
- Verify the `absi` formula's units and reverse any target scaling correctly.

These are restoration/evaluation requirements. No such rerun or clinical validation is claimed by the updated README.

## Cryptocurrency research

**Start reading:** [research overview](../cryptocurrency_sentiment-Deep_Learning/README.md), then the design note and English optimization notebook.

| Required material | Referenced examples | Why it matters |
|---|---|---|
| English text data | `mbsa.csv`, prepared `text2.csv` | Matching labels and preprocessing determine the model's task. |
| Tokenizer and sequence artifacts | Saved word indices and `X_train`, `X_test`, `y_train`, `y_test` NumPy files | Several cells reload arrays; their consistency with the earlier split is not established by source inspection. |
| Model files | External `history10.h5` and other checkpoints | Saved evaluation cells load these files; weights are not bundled. |
| Historical price inputs | Coin CSVs including `Bitcoin.csv` | Date ordering, cleaning, and source snapshot affect price features. |
| Database tables | Coin price/sentiment tables and recommendation summaries | Required by graph and recommendation prototypes. |

Before evaluating the sentiment model, inspect the output order: in the representative logged calls, **index 0 is loss and the logged `acc` field is accuracy**. Read the [metric reconciliation](PROJECT_EVIDENCE.md#cryptocurrency-research) before quoting a printed result.

Before evaluating forecasting or recommendation work:

1. Establish chronological order and confirm each feature uses only information available at its prediction time.
2. Review rolling shifts in the context of that order; do not assume their direction alone proves causality.
3. Fit scaling on the training segment and preserve its parameters.
4. Separate training, validation, and final test sequences.
5. Distinguish sentiment labels, transformed-price losses, preference matching, and market-direction outcomes.
6. Verify the recommendation's asset list, globals, overwritten definitions, and external-table contracts.

Restoring historical tables does not authorize access to a former shared database. Use an explicitly owned test environment and avoid copying connection information into documentation.

## Cryptocurrency integration

**Start reading:** [integration overview](../crypto_market_prediction_project-DB_DL_combined/README.md), then the K갈대 notebook as text.

| Required material | References in the code |
|---|---|
| Korean labeled spreadsheets | `alt.xlsx`, `btc.xlsx`, `eth.xlsx`, `xrp.xlsx` under an external `crypto_labeling_Korean` directory. |
| Prepared arrays | Three-class NumPy sequence and target files saved/reloaded by the model notebook. |
| Vocabulary dictionary | Saved tokenizer word-index JSON. |
| Trained classifier | External `.h5` checkpoints used by evaluation and inference cells. |
| NLP tooling | KoNLPy/Okt and a compatible Java environment. |
| Database | Deliberately configured test connections and a known append destination. |

### Crawler execution boundary

`coinpan_crawling.py` and `coinpan_index_c.py` contain top-level network calls and SQL append paths. They are **not safe read-only import targets**. The longer variant specifies pages 1–1200; the shorter variant uses `range(0,10)`.

Before any execution, review the current source interface, request scope, write destination, and connection placeholders. A user-authorized documentation cleanup is not authorization to collect current site data or append to a live database.

### Model execution boundary

The notebook writes dictionaries/arrays, trains/checkpoints models, and loads external files. Match text preprocessing, label mapping, vocabulary size, padded length, and model architecture before running inference or reporting reproduced accuracy.

## Files preserved and files ignored

The original notebooks, checkpoint notebooks, Python files, figures, and notes remain in place. The root `.gitignore` excludes local virtual environments, caches, environment files, and the existing local health `DataSets/` directory.

Ignoring `.ipynb_checkpoints/` prevents newly generated checkpoint files from routine staging; it does **not** remove the 13 already tracked checkpoint notebooks. The ignore rules do not delete or relocate the local CSV files.

Do not assume an unrestricted dataset redistribution license or a repository-wide software license. Establish permission and attribution before packaging source data or third-party material for redistribution.

## What was actually checked

- Notebook JSON structure for all 67 original tracked notebooks.
- Source and selected outputs for representative analytical/model/collection paths.
- Relative documentation links, image provenance, Markdown structure, and local presentation previews.
- The change boundary: documentation/assets/ignore rules versus the original project artifacts.

Training, statistical reanalysis, browser crawling, database access, historical model restoration, and remote GitHub publication remain separate operations. Their absence from this review is stated so that the portfolio can be read accurately.

## 2026-10-20 maintenance follow-up

Publication was authorized after the original review. Two `.py` exports now keep
notebook-only installation commands as comments, allowing ordinary Python to
parse them. Data/dependency preparation, effect inspection and model restoration
are still required. Run `python tools/validate_documentation.py` for structure
and local links; see [REPAIRS.md](REPAIRS.md) for the verification boundary.
