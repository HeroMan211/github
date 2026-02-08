"""
Day 17 Activity: Scaling Practice
Tasks:
1) Load numeric dataset
2) Apply Min-Max, Standard, and Robust scaling
3) Compare distributions or summary stats
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

# TODO: Load data from data/day17_scaling.csv
df = pd.read_csv("day17_scaling.csv")

# TODO: Fit scalers on numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns
MinMax =  MinMaxScaler()
Standard =  StandardScaler()
Robust = RobustScaler()


# TODO: Transform and compare summaries
scaled_minmax = MinMax.fit_transform(df[numeric_cols])
scaled_standard = Standard.fit_transform(df[numeric_cols])
scaled_robust = Robust.fit_transform(df[numeric_cols])

print(scaled_minmax.mean())
print(scaled_standard.mean())
print(scaled_robust.mean())
print(df.mean())