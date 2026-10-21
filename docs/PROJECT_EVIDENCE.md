# Project Background & Evidence Register

[Portfolio](../README.md) · [Reproduction guide](REPRODUCIBILITY.md) · [Complete catalog](NOTEBOOK_CATALOG.md)

This register explains where the updated project descriptions come from. Review date: **2026-10-12**. Source code, saved outputs, author-provided background, and fresh execution are different evidence levels.

| Label | Meaning in this documentation |
|---|---|
| **Code inspected** | A method, parameter, field, or external effect is visible in the saved source. |
| **Saved output** | A historical notebook output contains the value or figure; execution was not repeated. |
| **Author record** | A résumé, CV, or retrospective project brief records the claim. This verifies the record's contents, not an independent reconstruction of the underlying outcome. |
| **Interpretation** | A methodological assessment or explanation based on those observations. |
| **Not established / 미확인** | Evidence needed for the stronger claim is absent from this review. |

In maintainer communication, `[팩트]` identifies observations, `[추론]` identifies interpretation, and `[주의]` identifies material operational risks. The public READMEs use the explicit provenance descriptions above so that reported outcomes are not mistaken for freshly reproduced results.

## Author-provided background

The owner authorized reading several résumé versions to understand the projects. Relevant local records were consulted without copying the original PDFs, contact details, or private filesystem paths into this repository.

| Record | Relevant pages reviewed | What it contributes |
|---|---|---|
| **Joon Chun - Resume-F2026.pdf** | Pages 1–2 | MultiCampus Data Science & Engineering Professional Program, K-Digital Training, 844 hours, July–December 2021; the three project themes and leadership/analytical responsibilities. |
| **Joon Chun - Resume-F2024.pdf** | Project section, page 2, visually inspected | Cryptocurrency project, October–December 2021; health project, August–October 2021; historical contribution and performance wording. |
| **Joon (Jeremy) Chun CV 2023.pdf** | Pages 1–2 | July–December 2021 MultiCampus training; Excellent Project Achievement entries for the health modeling and EV analysis/visualization projects. |
| **Analysis_of_the_Electric_Vehicle_Market_in_Korea.pdf** | Pages 1–3 | July–August 2021, lead-analyst/search-trend contribution, and broader team context. |
| **Blood_Pressure_and_Glucose_Level_Prediction.pdf** | Pages 1–4 | September–October 2021, team leadership and blood-pressure contribution, component division, and reported outcome table. |
| **Cryptocurrency_Market_Forecast_via_Sentiment_and_Statistical_Analysis.pdf** | Pages 1–4 | October–December 2021, framework/statistical/AI collaboration, reported hybrid comparison, and web-platform concept. |

Some additional résumé versions were located but did not provide extractable text during the initial pass. They are not used as independent corroboration here.

### Reconciliation decisions

- **Three projects, four folders:** the two cryptocurrency collections belong to the same final project. This is presented as three portfolio projects and four code collections.
- **Health period:** the brief says September–October; the 2024 résumé says August–October. The project title uses “Autumn 2021,” with both source dates explained in the body.
- **Individual versus team role:** the EV notebook contains a direct named role list. Health and cryptocurrency leadership comes from author records; those roles do not establish sole implementation of all archived work.
- **Awards:** the CV records two Excellent Project Achievement entries. An institutional award certificate was not independently checked for this documentation pass.
- **Web context:** the author records describe broader web-prototype work. A complete frontend or deployed service is not preserved among the original tracked artifacts.
- **Database technology:** the cryptocurrency brief mentions MongoDB/AWS, while the examined archive includes MySQL interfaces. The README distinguishes broader team context from the actual local code.

## Electric vehicle analysis

| Claim or observation | Evidence location | Level |
|---|---|---|
| Team framing includes charging infrastructure and policy readiness. | [Comparison portfolio notebook](<../Electric_vehicle_trend-Visualization_Analysis/portfolio_team1 천준_5y-1y비교.ipynb>), cells 1–2 | Code/document text inspected |
| Joon Chun / 천준 is assigned global/country/Korean Google search-trend analysis. | Same notebook, cells 2–4 | Direct contributor record |
| Other named team roles and 홍효석 as team leader. | Same notebook, cell 2 | Direct contributor record |
| Country collection and pagination; Excel inputs and Korea color assignment. | Same notebook, cells 12 and 17–20 | Code inspected |
| Six five-year rows are removed before plotting. | Same notebook, cell 28 | Code inspected |
| Side-by-side country-interest figure. | Same notebook, cell 29 | Saved output |
| Long-term series uses a 2004 start label and an intended twelve-month smoother. | [Global portfolio notebook](<../Electric_vehicle_trend-Visualization_Analysis/portfolio_team1 천준_세계추의.ipynb>), cells 10–19 | Code and saved output |
| Smoothing expression repeats `a3` and divides by twelve. | Global notebook, cell 16 | Code inspected |
| Django ownership-cost interface and adoption prediction appear as unrealized extensions. | Comparison notebook, cell 35; global notebook, cell 25 | Historical reflection |

**Interpretation:** the country rankings support a discussion of relative interest, not absolute search counts or EV purchases. Google's normalization guidance supports that distinction: [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en).

**Interpretation:** the global figure's red line is a historical implementation with a repeated lag. The README retains the original graphic, explains the issue, and avoids presenting it as a corrected or revalidated moving average.

## Health prediction

| Claim or observation | Evidence location | Level |
|---|---|---|
| Input is `NHIS_OPEN_GJ_2017_v1.1.csv`, read with CP949 encoding. | [Consolidated notebook](<../BP_BG_prediction-Machine_Deep_Learning/(종합)혈당수치예측_천준.ipynb>), cell 6 | Code inspected |
| Demographic, measurement, lifestyle, and health fields are mapped. | Same notebook, cell 11 | Code inspected |
| BMI and the archived ABSI feature are constructed. | Same notebook, cell 19 | Code inspected |
| Glucose labels use `[99,125,200,999]`, `[125]`, and `[99]`. | Same notebook, cell 45 | Code inspected |
| Linear baseline RMSE is 22.334012770818042. | Same notebook, cells 54–57 | Code and saved output |
| Extended OLS RMSE is 22.332217021095655. | Same notebook, cells 66–69 | Code and saved output |
| Binary logistic score is 0.9228056898123462. | Same notebook, cells 177–181, using `fbs_L2` | Code and saved output |
| Standardized-target forest MSE is 0.9105971380759728. | [Compact forest study](../BP_BG_prediction-Machine_Deep_Learning/Data_modeling_the_best_model_천준.ipynb), cells 37–41 | Code and saved output |
| Scalers are fitted during preparation before later train/test splitting. | Consolidated notebook, cells 48–49 and 54; compact forest study, scaling preparation and cells 37–39 | Code inspected |
| A compact-study cell multiplies MSE by a target standard deviation. | Compact forest study, cell 42 | Code inspected; not a verified RMSE inversion |
| Team leadership and blood-pressure responsibility. | Health project brief, pages 1 and 3–4 | Author record |
| 79% blood-pressure and 91% glucose accuracy; listed precision/recall/F1 and RMSE values. | Health project brief, page 3 | Author record |

**Interpretation:** the reported outcome table combines classification metrics and continuous prediction errors without a full label/split specification. Its values are preserved as reported outcomes and are not treated as reconstructions from the example notebooks.

**Interpretation:** a fresh evaluation should fit transformations on training data, reserve validation for model selection, and preserve a final untouched test set. Standardized MSE is not original-unit RMSE; a proper conversion requires the appropriate square root and scale. The original calculation is not silently corrected in the notebook.

**Not established:** clinical validation, device equivalence, current model reproducibility, and the archived implementation of the reported final LightGBM component. The local 2020 CSVs are not verified replacements for the referenced 2017 dataset.

## Cryptocurrency research

| Claim or observation | Evidence location | Level |
|---|---|---|
| English text cleaning functions cover handles, URLs, emoji, tags, and related text patterns. | [English preprocessing exploration](<../cryptocurrency_sentiment-Deep_Learning/(eng) sentiment analysis_mbsa-천준님.ipynb>), cells 18–19 | Code inspected |
| Representative LSTM optimization credits 김승현. | [English optimization notebook](<../cryptocurrency_sentiment-Deep_Learning/갈대 AI/(eng)AI최적화mbsa3.ipynb>), cell 1 | Direct collaborator attribution |
| Stratified 80/20 split, `random_state=1004`; padding length 30. | Same notebook, cells 10 and 31–32 | Code inspected |
| Prepared arrays are reloaded from external files before model work. | Same notebook, cell 35 | Code inspected |
| Embedding 400, LSTM 256, three-way softmax; RMSprop and sparse cross-entropy. | Same notebook, cells 40–42 | Code inspected |
| `evaluate()[0]` is printed as accuracy in cells 43–47. | Same notebook, cells 43–47 | Code inspected |
| Cell 45 logs loss 0.8045 and actual `acc` 0.6961. | Same notebook, cell 45 | Saved output; the printed 0.8045 is loss |
| Corresponding mislabeled output also appears in the Korean-named English optimization variant. | [갈대AI_최적화_mbsa3.ipynb](<../cryptocurrency_sentiment-Deep_Learning/갈대 AI/갈대AI_최적화_mbsa3.ipynb>), corresponding evaluation cells | Code and saved output |
| Candidate sentiment/count formulas use equal coefficients. | [XRP index notebook](<../cryptocurrency_sentiment-Deep_Learning/Sentiment_index/감정지수화(XRP).ipynb>), cells 62, 69, 77 | Code inspected |
| MA14 model uses 28-observation sequences, LSTM 128, and MSE. | [MA14 notebook](<../cryptocurrency_sentiment-Deep_Learning/Price_prediction_AI/Time_series_analysis_cryptocurrency_LSTM_AI_MA14(GPU).ipynb>), cells 39–47 | Code inspected |
| Train/test loss is 0.0018862022552639246 / 0.09945763647556305. | Same notebook, cell 50 | Saved output on transformed target |
| Later training/validation curves diverge. | Same notebook, cell 48 | Saved figure |
| Negative shifts, whole-series scaling, and test data used during fitting are present. | Same notebook, cells 20, 23, 33, 35, 47 | Code inspected |
| Recommendation matches a desired amplitude level to a ranking. | [Recommendation prototype](../cryptocurrency_sentiment-Deep_Learning/Recommendation/Final_Recommendation_system_cryptocurrency1.ipynb), cells 6 and 9–11 | Code inspected |
| Repeated BTC entries and revised function definitions remain. | Same notebook, cells 4, 10–11 | Code inspected |
| Price plus English/Korean positive ratios are plotted. | [XRP graph notebook](<../cryptocurrency_sentiment-Deep_Learning/가격,감정 그래프/Copy of XRP_그래프_2차_시각화밎html저장.ipynb>), cell 13 onward | Code inspected |

### Reported capstone comparison

The cryptocurrency brief, page 3, reports sentiment-only success in the 40% range, statistical-only success in the 50% range, and combined success of 80%, with a 24-hour timeframe. Its comparison also reports different trade frequencies across methods.

The 2024 résumé instead uses wording about prediction accuracy improving by more than 70%. These statements do not specify matching definitions, samples, or denominators, so they are not combined into a new precise metric.

**Interpretation:** the capstone market-success claims and the sentiment classifier's accuracy answer different questions. Neither the printed loss values nor the MA14 regression loss corroborates an 80% market-success result.

**Interpretation:** date order must be established before judging the rolling shifts' causal meaning. The observed negative shifts are a review requirement, not automatic proof of look-ahead leakage in every notebook. Whole-series scaling and use of test sequences during fitting also limit the saved evaluation's independence.

**Not established:** a canonical final model, a matched set of weights/tokenizer/data, prospective trading results, net-of-cost performance, full top-ten coverage in a restored service, or a current deployment.

## Cryptocurrency integration

| Claim or observation | Evidence location | Level |
|---|---|---|
| Longer crawler targets XRP, pages 1–1200, and SQL append to `coinpan_xrp`. | [coinpan_crawling.py](../crypto_market_prediction_project-DB_DL_combined/coinpan_crawling.py), lines 16–30 and append call | Code inspected |
| Shorter crawler uses `range(0,10)` and the same table name. | [coinpan_index_c.py](../crypto_market_prediction_project-DB_DL_combined/coinpan_index_c.py), line 27 and append call | Code inspected |
| Crawlers contain top-level network/database work and connection placeholders. | Both crawler scripts | Code inspected; not executed |
| Four external labeled Excel files are read; class 3 is excluded. | [K갈대 notebook](<../crypto_market_prediction_project-DB_DL_combined/갈대 AI/K갈대_AI_최적화.ipynb>), cells 6 and 12 | Code inspected |
| Labels are described as positive 0, neutral 1, negative 2. | Same notebook, preparation notes | Code/document text inspected |
| Stratified 20% test split, `random_state=2045`; padding length 100. | Same notebook, cells 21 and 54–55 | Code inspected |
| Three-class LSTM model, parameter loop, checkpoint loading. | Same notebook, cells 68–73 | Code inspected |
| Loaded-model evaluation logs loss 1.1295 and accuracy 0.5391. | Same notebook, cell 73 | Saved output |
| Final displayed loop evaluation logs loss 1.0226 and accuracy 0.5571. | Same notebook, cell 68 output | Saved output; not a best-model claim |
| Inference preparation function is present. | Same notebook, cell 75 onward | Code inspected |

## Documentation-review boundary

[팩트] The original tracked inventory contains 67 notebooks, four Python scripts, six PNG files, and three Markdown files. All 67 notebook files were parsed as JSON. Representative code and selected saved outputs were then reviewed in detail.

[팩트] This pass changes documentation, adds presentation assets, and adds local ignore rules. The original notebooks, scripts, outputs, and datasets are preserved. Notebook execution, model training, crawler requests, database writes, Git commits, and GitHub pushes are not part of this completed documentation pass.

The source register is deliberately explicit about missing validation. It supports accurate portfolio explanations without replacing the historical artifacts or implying that reported project outcomes have been independently rerun.

## 2026-10-20 publication follow-up

The earlier boundary describes the 2026-10-12 review. Publication was subsequently
authorized. The remote README additions were compared with the prepared guides;
existing remote commits are preserved. Two Python exports received the limited
notebook-command syntax repair in [REPAIRS.md](REPAIRS.md). Notebook contents and
historical outputs were not regenerated. See the
[current handoff](handoffs/HANDOFF_2026-10-20_documentation_publication.md) for publication status.
