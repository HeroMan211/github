"""

Day 36 Activity: Vectors

Tasks:

1) Create feature and weight vectors

2) Compute vector addition and scalar multiplication

3) Compute norms and inspect shapes

"""

 

import numpy as np

 

# Provided vectors (edit if you want different values)

feature = np.array([30.0, 50.0, 10.0])

weights = np.array([0.05, 0.8, -0.1])

 

# TODO: Compute addition, scaling, and norms

print("feature shape:", feature.shape)

print("weights shape:", weights.shape)

print("feature + weights:", feature + weights)

print("2 * feature:", 2 * feature)
print("Norm of feature:", np.linalg.norm(feature))
print("Norm of weights:", np.linalg.norm(weights))