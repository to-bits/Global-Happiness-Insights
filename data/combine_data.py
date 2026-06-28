import pandas as pd
import numpy as np
import os

# Define file mappings based on the approved implementation plan
mappings = {
    "2015.csv": {
        "Year": lambda df: 2015,
        "Happiness Rank": "Happiness Rank",
        "Country": "Country",
        "Happiness Score": "Happiness Score",
        "GDP per Capita": "Economy (GDP per Capita)",
        "Social Support": "Family",
        "Healthy Life Expectancy": "Health (Life Expectancy)",
        "Freedom to make life choices": "Freedom",
        "Generosity": "Generosity",
        "Perceptions of Corruption": "Trust (Government Corruption)",
        "Dystopia + Residual": "Dystopia Residual"
    },
    "2016.csv": {
        "Year": lambda df: 2016,
        "Happiness Rank": "Happiness Rank",
        "Country": "Country",
        "Happiness Score": "Happiness Score",
        "GDP per Capita": "Economy (GDP per Capita)",
        "Social Support": "Family",
        "Healthy Life Expectancy": "Health (Life Expectancy)",
        "Freedom to make life choices": "Freedom",
        "Generosity": lambda df: np.nan,
        "Perceptions of Corruption": lambda df: np.nan,
        "Dystopia + Residual": lambda df: np.nan
    },
    "2017.csv": {
        "Year": lambda df: 2017,
        "Happiness Rank": "Happiness.Rank",
        "Country": "Country",
        "Happiness Score": "Happiness.Score",
        "GDP per Capita": "Economy..GDP.per.Capita.",
        "Social Support": "Family",
        "Healthy Life Expectancy": "Health..Life.Expectancy.",
        "Freedom to make life choices": "Freedom",
        "Generosity": "Generosity",
        "Perceptions of Corruption": "Trust..Government.Corruption.",
        "Dystopia + Residual": "Dystopia.Residual"
    },
    "2018.csv": {
        "Year": lambda df: 2018,
        "Happiness Rank": "Overall rank",
        "Country": "Country or region",
        "Happiness Score": "Score",
        "GDP per Capita": "GDP per capita",
        "Social Support": "Social support",
        "Healthy Life Expectancy": "Healthy life expectancy",
        "Freedom to make life choices": "Freedom to make life choices",
        "Generosity": "Generosity",
        "Perceptions of Corruption": "Perceptions of corruption",
        "Dystopia + Residual": lambda df: np.nan
    },
    "2019.csv": {
        "Year": lambda df: 2019,
        "Happiness Rank": "Overall rank",
        "Country": "Country or region",
        "Happiness Score": "Score",
        "GDP per Capita": "GDP per capita",
        "Social Support": "Social support",
        "Healthy Life Expectancy": "Healthy life expectancy",
        "Freedom to make life choices": "Freedom to make life choices",
        "Generosity": "Generosity",
        "Perceptions of Corruption": "Perceptions of corruption",
        "Dystopia + Residual": lambda df: np.nan
    },
    "2020.csv": {
        "Year": lambda df: 2020,
        "Happiness Rank": lambda df: df["Ladder score"].rank(ascending=False, method="min").astype(int),
        "Country": "Country name",
        "Happiness Score": "Ladder score",
        "GDP per Capita": "Explained by: Log GDP per capita",
        "Social Support": "Explained by: Social support",
        "Healthy Life Expectancy": "Explained by: Healthy life expectancy",
        "Freedom to make life choices": "Explained by: Freedom to make life choices",
        "Generosity": "Explained by: Generosity",
        "Perceptions of Corruption": "Explained by: Perceptions of corruption",
        "Dystopia + Residual": "Dystopia + residual"
    },
    "2021.csv": {
        "Year": lambda df: 2021,
        "Happiness Rank": lambda df: df["Ladder score"].rank(ascending=False, method="min").astype(int),
        "Country": "Country name",
        "Happiness Score": "Ladder score",
        "GDP per Capita": "Explained by: Log GDP per capita",
        "Social Support": "Explained by: Social support",
        "Healthy Life Expectancy": "Explained by: Healthy life expectancy",
        "Freedom to make life choices": "Explained by: Freedom to make life choices",
        "Generosity": "Explained by: Generosity",
        "Perceptions of Corruption": "Explained by: Perceptions of corruption",
        "Dystopia + residual": "Dystopia + residual"
    },
    "2022.csv": {
        "Year": lambda df: 2022,
        "Happiness Rank": "RANK",
        "Country": "Country",
        "Happiness Score": "Happiness score",
        "GDP per Capita": "Explained by: GDP per capita",
        "Social Support": "Explained by: Social support",
        "Healthy Life Expectancy": "Explained by: Healthy life expectancy",
        "Freedom to make life choices": "Explained by: Freedom to make life choices",
        "Generosity": "Explained by: Generosity",
        "Perceptions of Corruption": "Explained by: Perceptions of corruption",
        "Dystopia + Residual": "Dystopia (1.83) + residual"
    }
}

dfs = []
standard_cols = [
    "Year",
    "Happiness Rank",
    "Country",
    "Happiness Score",
    "GDP per Capita",
    "Social Support",
    "Healthy Life Expectancy",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of Corruption",
    "Dystopia + Residual"
]

for filename, mapping in sorted(mappings.items()):
    if not os.path.exists(filename):
        print(f"Warning: File {filename} not found.")
        continue
    
    print(f"Processing {filename}...")
    # 2022.csv uses comma as decimal separator
    if filename == "2022.csv":
        df_raw = pd.read_csv(filename, decimal=",")
    else:
        df_raw = pd.read_csv(filename)
    
    # Clean column names by stripping spaces to avoid mapping mismatches
    df_raw.columns = [col.strip() for col in df_raw.columns]
    
    df_new = pd.DataFrame()
    
    # Process Year first since standard columns depends on it
    if callable(mapping["Year"]):
        df_new["Year"] = [mapping["Year"](df_raw)] * len(df_raw)
    else:
        df_new["Year"] = df_raw[mapping["Year"]]
        
    for col in standard_cols:
        if col == "Year":
            continue
        
        # Determine the source key
        # Handle 2021 special case if Dystopia + residual has different case
        source_key = mapping.get(col) or mapping.get(col.replace("Residual", "residual"))
        
        if source_key is None:
            df_new[col] = np.nan
        elif callable(source_key):
            df_new[col] = source_key(df_raw)
        else:
            if source_key in df_raw.columns:
                df_new[col] = df_raw[source_key]
            else:
                print(f"  Warning: Column '{source_key}' not found in {filename}. Filling with NaN.")
                df_new[col] = np.nan
                
    # Clean up ranks to be integers where possible
    df_new["Happiness Rank"] = pd.to_numeric(df_new["Happiness Rank"], errors="coerce").astype('Int64')
    
    # Coerce all numeric feature columns to float64
    numeric_cols = [
        "Happiness Score",
        "GDP per Capita",
        "Social Support",
        "Healthy Life Expectancy",
        "Freedom to make life choices",
        "Generosity",
        "Perceptions of Corruption",
        "Dystopia + Residual"
    ]
    for col in numeric_cols:
        df_new[col] = pd.to_numeric(df_new[col], errors="coerce")
    
    # Fill Year
    df_new["Year"] = df_new["Year"].astype(int)
    
    dfs.append(df_new)

# Combine all datasets
merged_df = pd.concat(dfs, ignore_index=True)

# Sort by Year and Rank
merged_df = merged_df.sort_values(by=["Year", "Happiness Rank"]).reset_index(drop=True)

# Save result
output_filename = "world happiness data 2015-2022.csv"
merged_df.to_csv(output_filename, index=False)
print(f"Successfully created combined dataset: '{output_filename}' with {len(merged_df)} rows and {len(merged_df.columns)} columns.")
