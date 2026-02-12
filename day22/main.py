"""
Day 22 Activity: Interaction Features

Tasks:

1) Load interaction dataset

2) Create multiplicative, additive, and logical interactions

3) Compute correlations with target

"""

 

import pandas as pd

 

# TODO: Load data from data/day22_interactions.csv

df = pd.read_csv("day22_interactions.csv")

# TODO: Create interaction features
df["multiplicative"] = df["feature1"] * df["feature2"]
df["additive"] = df["feature1"] + df["feature2"]

# TODO: Compute correlations with target

correlations = df.corr(numeric_only=True)["target"]

print(df)
print(correlations)