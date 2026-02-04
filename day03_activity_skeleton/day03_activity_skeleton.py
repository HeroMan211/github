"""
Day 3 Activity: Use lambda and .apply() to clean a dataset.
Tasks:
1) Clean price (remove $ and commas)
2) Fill missing quantity with 0
3) Create total = price * quantity
4) Categorize price: low / med / high
"""

import pandas as pd

# Sample dataset
raw = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}


df = pd.DataFrame(raw)





# TODO: Clean price column using .apply with lambda. X
replace = lambda x: float(x.replace('$', '').replace(',', ''))
df['price'] = df['price'].apply(replace)

# TODO: Fill missing quantity with 0. X
df = df.fillna(0)

# TODO: Create total column.
df['total'] = df['price'] * df['quantity']

# TODO: Add price_category column (low/med/high).
def price_category(price):
    if price < 600:
        return 'low'
    elif price < 1500:
        return 'med'
    else:
        return 'high'

df['price_category'] = df['price'].apply(price_category)

print(df)
