"""
Day 11 Activity: Outlier Strategies
Tasks:
1) Load numeric data with outliers
2) Implement percentile capping (winsorization)
3) Implement removal strategy
4) Compare summary stats before/after
"""

import pandas as pd
import numpy as np

# TODO: Load data from data/day11_income.csv
df = pd.read_csv("day11_income.csv")

# TODO: Implement winsorize_series(s, lower_q, upper_q)\

def winsorize_series(s: pd.Series, lower_q=0.01, upper_q=0.99) -> pd.Series:
    lower, upper = s.quantile(lower_q), s.quantile(upper_q)
    return s.clip(lower=lower, upper=upper)
df["income_cap_1_99"] = winsorize_series(df["income"], 0.01, 0.90)

# TODO: Implement remove_upper_tail(s, upper_q)
upper_99 = df["income"].quantile(0.80)
mask_keep = df["income"] <= upper_99
df11_removed = df[mask_keep].copy()


# TODO: Compare summary stats and print results
print("Original rows:", len(df), "After removal:", len(df11_removed))