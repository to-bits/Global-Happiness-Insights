# World Happiness Report Analysis

> A complete **Exploratory Data Analysis (EDA)** project on the World Happiness Report dataset using **Python, NumPy, Pandas, Matplotlib, and Seaborn**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![NumPy](https://img.shields.io/badge/NumPy-Mathematics-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualization-green)
![License](https://img.shields.io/badge/License-MIT-success)

---

# Overview

The **World Happiness Report** is an annual publication that ranks countries based on the happiness of their citizens. The report evaluates multiple social and economic factors that influence overall life satisfaction.

This project performs a complete **Exploratory Data Analysis (EDA)** to discover patterns, relationships, and trends in the dataset using Python's most popular data science libraries.

The primary objective is to strengthen practical skills in data analysis, visualization, and storytelling using real-world data.

---

# Objectives

- Load and inspect a real-world dataset
- Clean and preprocess the data
- Handle missing values
- Perform statistical analysis
- Explore relationships between variables
- Create meaningful visualizations
- Identify the major factors affecting happiness
- Practice professional data analysis workflows

---

# Dataset

The dataset contains country-wise happiness statistics from the World Happiness Report.

### Main Features

| Feature | Description |
|----------|-------------|
| Country | Country Name |
| Happiness Score | Overall Happiness Score |
| GDP per Capita | Economic Prosperity |
| Social Support | Social Support Index |
| Healthy Life Expectancy | Average Healthy Life |
| Freedom | Freedom to Make Life Choices |
| Generosity | Generosity Score |
| Perceptions of Corruption | Corruption Index |
| Region | Geographic Region (if available) |

---

# Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# Project Structure

```text
World-Happiness-Analysis/
│
├── data/
│   └── world_happiness.csv
│
├── notebooks/
│   └── World_Happiness_EDA.ipynb
│
├── images/
│   ├── heatmap.png
│   ├── histogram.png
│   ├── scatterplot.png
│   ├── boxplot.png
│   └── pairplot.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Exploratory Data Analysis

The notebook includes:

## Data Loading

- Import dataset
- Display first and last records
- Check dataset shape

## Data Inspection

- Data types
- Missing values
- Duplicate records
- Unique values

## Data Cleaning

- Handle missing values
- Remove duplicates
- Rename columns
- Format data

## Statistical Analysis

- Mean
- Median
- Mode
- Standard Deviation
- Variance
- Minimum & Maximum
- Quartiles

## Data Visualization

Various charts were created including:

- Histogram
- Count Plot
- Box Plot
- Scatter Plot
- Line Plot
- Pie Chart
- Bar Chart
- Violin Plot
- Pair Plot
- Correlation Heatmap

---

# Key Insights

Some important findings from the analysis:

- Countries with higher GDP generally have higher happiness scores.
- Social support is strongly correlated with happiness.
- Healthy life expectancy significantly contributes to happiness.
- Freedom to make life choices positively impacts overall well-being.
- Countries with lower corruption tend to report higher happiness.
- Generosity has a weaker correlation compared to GDP and social support.

---

# Sample Visualizations

Add your generated plots inside the `images/` folder.

Example:

```text
images/
├── heatmap.png
├── histogram.png
├── scatterplot.png
├── boxplot.png
└── pairplot.png
```

---

# Getting Started

## Clone the repository

```bash
git clone https://github.com/your-username/world-happiness-analysis.git
```

## Navigate to the project directory

```bash
cd world-happiness-analysis
```

## Install required packages

```bash
pip install -r requirements.txt
```

## Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
World_Happiness_EDA.ipynb
```

---

# Requirements

```text
numpy
pandas
matplotlib
seaborn
jupyter
```

Install them with:

```bash
pip install -r requirements.txt
```

---

# Skills Demonstrated

This project demonstrates practical knowledge of:

- Data Cleaning
- Data Manipulation
- Exploratory Data Analysis (EDA)
- Data Visualization
- Correlation Analysis
- Statistical Analysis
- Feature Engineering Basics
- Storytelling with Data

---

# Future Improvements

Possible future enhancements include:

- Interactive dashboard using Plotly
- Streamlit web application
- Machine Learning model for Happiness Score prediction
- Time-series analysis
- Geographic visualization using GeoPandas
- Power BI dashboard

---
