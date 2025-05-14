# 485_MultiStation_Compare.ipynb and XGBoost.ipynb

## Overview
This Jupyter Notebook, `485_MultiStation_Compare.ipynb`, is designed to analyze and compare data from multiple stations. It provides insights into trends, correlations, and differences across datasets collected from various sources.
The `XGBOOST.ipynb` notebook contains our lane-by-lane spatiotemporal traffic prediction model using **XGBoost**. The goal is to forecast traffic flow every 5 minutes using time, location, and recent flow patterns across multiple stations and lanes.
This notebook trains separate models for each lane, evaluates accuracy using RMSE and R², and includes residual analysis, geospatial error mapping, and feature importance plots.

---

##  Features

- **Data Loading**: Import and preprocess data from multiple stations.
- **Visualization**: Generate comparative plots to identify trends and anomalies.
- **Statistical Analysis**: Perform statistical tests to evaluate relationships between datasets.
- **Customizable**: Easily adapt the notebook for different datasets or analysis requirements.
- **Data Filtering**: Select specific time ranges (e.g., Week 1 or entire 3 weeks)
- **Per-Lane Modeling**: Trains a separate XGBoost model for each traffic lane
- **Lag-Based Learning**: Incorporates short-term memory (`lag1`, `lag2`) to simulate traffic trend awareness
- **Evaluation Metrics**: Calculates RMSE and R² for each model
- **Visualization**:
  - Actual vs Predicted scatter plots
  - Residual histograms
  - Geospatial residual maps
  - Feature importance charts

---

## Requirements

Ensure the following dependencies are installed:

- Python 3.8+
- Jupyter Notebook
- Required Python libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `xgboost`
  - `geopandas`
  - `contextily`
  - `scikit-learn`
  - `scipy`


Install dependencies using:
```bash
pip install pandas numpy matplotlib seaborn xgboost geopandas contextily scikit-learn scipy
```

## Usage
1. Clone the repository:
     ```bash
     git clone <repository_url>
     ```
2. Navigate to the project directory:
     ```bash
     cd FinalProject/models
     ```
3. Open the notebook:
     ```bash
     jupyter notebook 485_MultiStation_Compare.ipynb
     jupyter notebook XGBoost.ipynb
     ```
4. Follow the instructions in the notebook to load your data and perform the analysis.


