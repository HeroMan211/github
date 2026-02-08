"""
Day 16 Activity: Encoding Practice
Tasks:
1) Load categorical dataset
2) Apply label encoding and one-hot encoding
3) Compare model behavior or summary stats
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('day16_encoding.csv')

le = LabelEncoder()
df['city_label_encoded'] = le.fit_transform(df['city'])
df_onehot = pd.get_dummies(df, columns=['city'], prefix='city')
print(df_onehot)
print(df)