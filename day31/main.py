"""

Day 31 Activity: Seaborn Visualizations

Tasks:

1) Load dataset

2) Recreate histplot, kdeplot, boxplot, countplot

"""

 

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

 

# TODO: Load data from data/day31_seaborn.csv

df = pd.read_csv("day31_seaborn.csv")

 

# TODO: sns.histplot, sns.kdeplot, sns.boxplot, sns.countplot

sns.histplot(data=df, x="value", hue="category", kde=True)
plt.show()
sns.kdeplot(data=df, x="value", hue="category")
plt.show()
sns.boxplot(data=df, x="category", y="value")
plt.show()
sns.countplot(data=df, x="category")
plt.show()