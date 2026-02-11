"""

Day 21 Activity: Domain-Driven Features

Tasks:

1) Load housing data

2) Create price_per_sqft safely

3) Propose at least two additional domain features

4) Compare basic model behavior (or summaries) with/without domain features

"""

 

import pandas as pd

import numpy as np

 

# TODO: Load data from data/day21_housing.csv

df = pd.read_csv('day21_housing.csv')

 
# TODO: Create price_per_sqft with safe division
df['price_per_sqft'] = df['price'] / (df['sqft'].replace(0, np.nan))  
# TODO: Create additional domain features
df['price_per_room'] = df['price'] / (df['bedrooms'] + df['bathrooms'].replace(0, np.nan)) 
# TODO: Print summary or model comparison
print(df)