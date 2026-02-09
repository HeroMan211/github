"""
Day 18 Activity: Binning Practice

Tasks:

1) Load age dataset

2) Apply equal-width bins, equal-frequency bins, and domain bins

3) One-hot encode bins and compare

"""

 

import pandas as pd

 

# TODO: Load data from data/day18_binning.csv

df18 = pd.read_csv("day18_binning.csv")

 
# TODO: Apply pd.cut and pd.qcut
bin_edges = [0, 18, 35, 50, 100]
labels = ["Child", "YoungAdult", "Adult", "Senior"]
df18["age_bins_width"] = pd.cut(df18["age"], bins=bin_edges, labels=labels, right=False)

# TODO: Create domain bins
df18["age_bins_quantiles"] = pd.qcut(df18["age"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])

# TODO: Compare value counts

print(df18["age_bins_width"].value_counts())
print(df18["age_bins_quantiles"].value_counts()) 


