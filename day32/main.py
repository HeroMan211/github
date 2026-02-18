"""

Day 32 Activity: Relationship Plots

Tasks:

1) Create scatterplot encoding >=3 variables

2) Create relplot with facet

"""

 

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

 

# TODO: Load data from data/day32_relationships.csv

df = pd.read_csv('day32_relationships.csv')

 

# TODO: sns.scatterplot with hue/style
sns.scatterplot(x='x', y='y', hue='category', style='size', data=df)
plt.show()
# TODO: sns.relplot with col or row
sns.relplot(x='x', y='y', col='category', data=df)
plt.show()