"""
Day 7 Activity: Imputation Practice
Tasks:
1) Implement fit_imputer(train_df) returning medians/modes
2) Implement transform_imputer(df, params)
3) Add missing indicators optionally
4) Compare behavior with/without indicators
"""

import pandas as pd


train = pd.DataFrame({
    "age": [25, None, 40, 33],
    "city": ["NY", "SF", None, "NY"],
})

test = pd.DataFrame({
    "age": [None, 50],
    "city": ["SF", None],
})

def fit_imputer(train_df, num_cols, cat_cols):
    medians = (train_df[num_cols].median())
    modes = (train_df[cat_cols].mode())
    return medians, modes

medians, modes = fit_imputer(train,'age', 'city')
print(modes)
train['age'] = train['age'].fillna(medians)
train['city'] = train['city'].fillna(modes)




    


def transform_imputer(df, params, add_indicators=True):
    num, cat = params
    df[num] = df[num].fillna(medians)
    df[cat] = df[cat].fillna(modes[0])
    return df

train = transform_imputer(train, ("age", "city"))

print(train)