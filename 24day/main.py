"""
Day 24 Activity: Feature Selection

Tasks:
1) Load dataset
2) Remove highly correlated features
3) Compare model performance before/after
"""
import pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
df = pd.read_csv('day24_selection.csv')
X = df.drop(columns=['target'])
y = df['target']
selector = VarianceThreshold(threshold=0.0)  
X_var = selector.fit_transform(X)
corr_matrix = X.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
X_reduced = X.drop(columns=to_drop)
model = LinearRegression()
score_before = cross_val_score(model, X, y, cv=2, scoring='r2')
score_after = cross_val_score(model, X_reduced, y, cv=2, scoring='r2')
print("Before feature selection: R² = {:.3f}".format(score_before.mean()))
print("After feature selection:  R² = {:.3f}".format(score_after.mean()))
