# Global Happiness Insights

A complete Exploratory Data Analysis (EDA) project on the World Happiness Report dataset using Python, NumPy, Pandas, Matplotlib, and Seaborn.

[![Python](https://camo.githubusercontent.com/b547c40e7cc5b2a89d2a6d7b78b90c8249769fc46e874f1b558233e9caa31004/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31312d626c7565)](https://www.python.org)
[![Pandas](https://camo.githubusercontent.com/f38aeeadbd3081c0fdd44355b9553183c23288db9583cbf75f74064ac94e0aae/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50616e6461732d44617461253230416e616c797369732d6f72616e6765)](https://pandas.pydata.org)
[![NumPy](https://camo.githubusercontent.com/452d4545bb5cfd9d28634903292af637975e7661b5be21edd6c1286f4b49545b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e756d50792d4d617468656d61746963732d626c7565)](https://numpy.org)
[![Matplotlib](https://camo.githubusercontent.com/a701b36596183b0910e5e303bec3de04038ca3eb6db79224c8580498d008b1ee/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d6174706c6f746c69622d56697375616c697a6174696f6e2d726564)](https://matplotlib.org)
[![Seaborn](https://camo.githubusercontent.com/70b638c5d8ca873fa664b3d5ceff40107e6b65593da70d9264fc4b3f20bcd99a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f536561626f726e2d537461746973746963616c25323056697375616c697a6174696f6e2d677265656e)](https://seaborn.pydata.org)

Exploratory Data Analysis (EDA) on World Happiness Report datasets (2015—2022).


---

**Quick links:**
- Combined dataset: [data/cleaned_readytoworkDataset.csv](data/cleaned_readytoworkDataset.csv)
- Combine script: [data/combine_data.py](data/combine_data.py)
- Notebooks: [analysis.ipynb](analysis.ipynb), [data_cleaning.ipynb](data_cleaning.ipynb)

---

## What this repo does

- Reads annual World Happiness Report CSVs (2015–2022) from the `data/` folder
- Normalizes differing column names across years into a consistent schema
- Coerces numeric fields and ranks, and concatenates all years into a single CSV
- Provides notebooks that demonstrate EDA and visualizations on the merged dataset

## Dataset

The dataset contains country-wise happiness statistics from the World Happiness Report.

### Main Features

| Feature | Description |
|---------|-------------|
| Country | Country Name |
| Happiness Score | Overall Happiness Score |
| GDP per Capita | Economic Prosperity |
| Social Support | Social Support Index |
| Healthy Life Expectancy | Average Healthy Life |
| Freedom | Freedom to make life choices |
| Generosity | Generosity Score |
| Perceptions of Corruption | Corruption Index |
| Dystopia + Residual | Dystopia + Residual Score |


---

## Project structure

```
Global-Happiness-Insights/
├── analysis.ipynb
├── data_cleaning.ipynb
├── data/
│   ├── 2015.csv
│   ├── 2016.csv
│   ├── 2017.csv
│   ├── 2018.csv
│   ├── 2019.csv
│   ├── 2020.csv
│   ├── 2021.csv
│   ├── 2022.csv
│   ├── combine_data.py
│   └── cleaned_readytoworkDataset.csv
├── image/
├── README.md
└── .gitignore
```

---

## How to reproduce the combined dataset

Make sure you are in the repository root and the individual yearly CSV files are present inside the `data/` folder. Then run:

```bash
python data/combine_data.py
```

This will produce `world happiness data 2015-2022.csv` in the repository root and also the project includes a cleaned dataset at [data/cleaned_readytoworkDataset.csv](data/cleaned_readytoworkDataset.csv).

Notes about `combine_data.py`:
- The script maps column names from each year's CSV into a common schema (Year, Happiness Rank, Country, Happiness Score, GDP per Capita, Social Support, Healthy Life Expectancy, Freedom to make life choices, Generosity, Perceptions of Corruption, Dystopia + Residual).
- It coerces numeric columns, handles missing columns by filling NaN, and saves the merged output as CSV.

---

## Notebooks

- `data_cleaning.ipynb` — shows cleaning steps and column normalization used to prepare the merged dataset.
- `analysis.ipynb` — contains the main EDA, visualizations, and key observations.

Open them with Jupyter or JupyterLab:

```bash
jupyter notebook
```

---

## Requirements

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install pandas numpy matplotlib seaborn jupyter
```

You can also create a `requirements.txt` by running:

```bash
pip freeze > requirements.txt
```

---

## Key insights (summary)

- GDP per capita, social support, and healthy life expectancy show strong positive relationships with reported Happiness Score.
- Freedom and perceptions of corruption also correlate with happiness but with varying strength across years.
- Generosity tends to show weaker correlation compared to the other factors.

These are demonstrated in `analysis.ipynb` with correlation heatmaps and year-by-year comparisons.

---

## Next steps / Improvements

- Add automated tests that validate column mappings and merged output
- Add a small CLI to control output filename and input folder
- Provide interactive dashboards (Streamlit / Plotly Dash)

---

If you'd like, I can (1) run the combine script, (2) update the repo to save the merged CSV to `data/`, or (3) add a `requirements.txt`. Tell me which you'd prefer.

