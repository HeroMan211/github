import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import PowerTransformer

# Load data
df19 = pd.read_csv("day19_transform.csv")

# Inspect raw data
print("Raw spend summary:")
print(df19["spend"].describe())
print("Skew:", df19["spend"].skew())
print()

df19["spend_log1p"] = np.log1p(df19["spend"])

df19["spend_sqrt"] = np.sqrt(df19["spend"])

pt = PowerTransformer(method="yeo-johnson")
df19["spend_yeojohnson"] = pt.fit_transform(df19[["spend"]])

summary = df19[["spend", "spend_log1p", "spend_sqrt", "spend_yeojohnson"]].describe()

print(summary)
print(df19[["spend", "spend_log1p", "spend_sqrt", "spend_yeojohnson"]].skew())

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

sns.histplot(df19["spend"], ax=axes[0, 0], kde=True)
axes[0, 0].set_title("Raw Spend")

sns.histplot(df19["spend_log1p"], ax=axes[0, 1], kde=True)
axes[0, 1].set_title("Log1p Spend")

sns.histplot(df19["spend_sqrt"], ax=axes[1, 0], kde=True)
axes[1, 0].set_title("Sqrt Spend")

sns.histplot(df19["spend_yeojohnson"], ax=axes[1, 1], kde=True)
axes[1, 1].set_title("Yeo-Johnson Spend")

plt.tight_layout()
plt.show()
