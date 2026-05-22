# Traffic Flow Forecasting — I-5 Corridor

Forecasting lane-level traffic flow on the I-5 corridor using Caltrans PeMS sensor data, comparing XGBoost against ARIMA/SARIMA baselines.

## Results

| Model | RMSE |
|---|---|
| ARIMA baseline | 278–345 |
| XGBoost (per-lane) | **1.04–3.76** |

XGBoost outperformed the ARIMA baseline by over 98% on held-out data across 3 weeks and 10 highway stations.

## Key decisions

- Engineered spatiotemporal lag features: 5-min and 10-min lags, hour-of-day, day-of-week, station coordinates
- Trained separate XGBoost models per lane — lag features confirmed as dominant predictors
- Validated spatial consistency with geospatial residual maps in GeoPandas — no high-error clusters

## Stack
Python · XGBoost · ARIMA/SARIMA · GeoPandas · Caltrans PeMS API

---
*Group project — original repo:[CSCI485_Spring25_Group2] [https://github.com/DrewsCodeLife/CSCI485_Spring25_Group2]*
