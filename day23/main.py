"""
Day 23 Activity: Polynomial Features

Tasks:
1) Load regression dataset
2) Add polynomial features (degrees 1,2,5)
3) Compare model fits or visualize predictions
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
for i in 10:
df = pd.read_csv("day23_poly.csv")

X = df[['x']]         
y = df['y']

print("Original shape:", X.shape)

for d in [1, 2, 5]:
    poly = PolynomialFeatures(degree=d, include_bias=False)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    scores = cross_val_score(model, X_poly, y, cv=5, scoring='r2')

    print(f"Degree {d}")
    print("  Expanded shape:", X_poly.shape)
    print("  CV R²: {:.3f} (std {:.3f})".format(scores.mean(), scores.std()))

plt.scatter(X, y, color='black', label='Data')

x_range = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)

for d in [1, 2, 5]:
    poly = PolynomialFeatures(degree=d, include_bias=False)
    X_poly = poly.fit_transform(X)
    
    model = LinearRegression()
    model.fit(X_poly, y)

    x_range_poly = poly.transform(x_range)
    y_pred = model.predict(x_range_poly)
