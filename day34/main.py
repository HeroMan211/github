"""

Day 34 Activity: Pattern Discovery

Tasks:

1) Create faceted plots (row/col)

2) Add trend overlays or grouped plots

3) Identify non-obvious pattern

"""

 

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

 

# TODO: Load data from data/day34_patterns.csv

df = pd.read_csv('day34_patterns.csv')

 

# TODO: Faceted relplot or catplot
sns.relplot(data=df, x='time', y='value', col='segment')
plt.show()
sns.catplot(data=df, x='segment', y='value', kind='box')
plt.show()
# TODO: Trend overlay
sns.regplot(data=df, x='time', y='value', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.show()

sns.lmplot(data=df, x='time', y='value', hue='segment', scatter_kws={'alpha':0.5}, line_kws={'linewidth':2})
plt.show()