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

sns.histplot(data=df, x="age", hue="segment", kde=True)
plt.show()
sns.kdeplot(data=df, x="age", hue="segment")
plt.show()
sns.boxplot(data=df, x="segment", y="age")
plt.show()
sns.countplot(data=df, x="segment")
plt.show()