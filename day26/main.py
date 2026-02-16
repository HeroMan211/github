"""
Day 26 Activity: Data Distributions

Tasks:

1) Load numeric dataset

2) Plot histograms and KDEs

3) Compute mean, median, std, skew

4) Apply log1p to a skewed feature and replot
"""

 

import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

#TODO: Load data from data/day26_distributions.csv

df = pd.read_csv('day26_distributions.csv')

# TODO: Plot histogram and KDE for each numeric column

plot = plt.figure(figsize=(6, 4))
df["transactions"].hist(bins=45, alpha=0.5, density=True, label="Histogram")
sns.kdeplot(df["transactions"], color="red", label="KDE")
plt.legend(); plt.title("Transactions — Histogram + KDE")

# TODO: Compute summary stats

print (df.describe())

# TODO: Apply log1p to skewed feature and replot

np.log1p(df)

plt.show()