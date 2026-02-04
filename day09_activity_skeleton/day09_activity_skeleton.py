"""
Day 9 Activity: Data Types Practice
Tasks:
1) Identify numeric-like, currency-like, datetime-like columns
2) Convert to proper dtypes
3) Validate conversions by checking NaN counts
"""

import pandas as pd

raw = {
    "age": ["25", "30s", "unknown"],
    "income": ["$50,000", "$60,000", None],
    "signup": ["2024-01-01", "01/05/2024", "not a date"],
}

df = pd.DataFrame(raw)

df['age'] = pd.to_numeric(df['age'], errors='coerce')

counter = 0
for i in df['income']:
    if type(i) == str:
        df['income'][counter] = df['income'][counter].replace('$',',').replace(',','')
    counter += 1

df['income'] = pd.to_numeric(df['income'] , errors='coerce')

df['signup'] = pd.to_datetime(df['signup'], errors='coerce')
print(df)
# TODO: Implement normalize_schema(df) to convert types safely
