# IBM Data Science Capstone — SpaceX Falcon 9

Reproducible project files for exploring historical Falcon 9 first-stage landing outcomes, using the IBM Skills Network prepared datasets.

## Contents
- `01_Data_Collection_and_Wrangling.ipynb` — loads and inspects the prepared dataset; **not a live API/scraping implementation**.
- `02_EDA_Visualization.ipynb` — launch site, payload, orbit and annual trend plots.
- `03_SQL_Analysis.ipynb` — SQLite queries on the prepared dataset.
- `04_Folium_Launch_Sites.ipynb` — interactive map of launch sites.
- `05_Machine_Learning.ipynb` — logistic regression, SVM, decision tree and KNN model comparison.
- `SpaceX_Dash_App.py` — interactive Plotly Dash application.
- `SpaceX_SQL_Reproduced.sql` — additional SQL queries.
- `SpaceX_Folium_Actual_Map.html` — generated Folium map.
- `dataset_part_2.csv`, `dataset_part_3.csv` — IBM Skills Network prepared datasets.
- `figures/` — report visualizations.
- `SpaceX_Capstone_Presentation.pdf` — the earlier 15-page report (not an assertion that all rubric criteria are met).

## Run
Install dependencies with `pip install -r requirements.txt`.
Launch JupyterLab and run the notebooks in numerical order.
For the Dash app: `python SpaceX_Dash_App.py`.

## Data and methodology
Historical sample: 90 launches; 83 prepared model features. The modeling notebook uses an 80/20 split (`random_state=2`), 5-fold GridSearchCV and scaling within each cross-validation pipeline.

## Limitations
The supplied course lab templates had no executed outputs, so this repository contains independently written **reproductions based on prepared datasets**, not falsely labeled completed original API and Wikipedia scraping labs. Folium proximity distances to roads/rail/coast have not been calculated. The report is not guaranteed to satisfy every grading criterion.

## Execution status (2026-10-11)
All five notebooks were executed successfully and their code outputs were saved. The machine-learning notebook reports 15/18 = 83.33% held-out accuracy for its selected model under the recorded split and grid-search settings. Plotly chart HTML files are exported reproducible outputs from the same dataset; the Dash Python app itself has not been launched in this environment. API/web scraping and geographic proximity measurements remain incomplete and are **not claimed as finished**.

## Notebook links
- [Data preparation](01_Data_Collection_and_Wrangling.ipynb)
- [EDA](02_EDA_Visualization.ipynb)
- [SQL](03_SQL_Analysis.ipynb)
- [Folium](04_Folium_Launch_Sites.ipynb)
- [Classification](05_Machine_Learning.ipynb)
- [Dash application source](SpaceX_Dash_App.py)
