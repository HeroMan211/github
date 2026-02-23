
"""

Day 37 Activity: Dot Product

Tasks:

1) Compute dot product of two vectors

2) Compute cosine similarity

3) Interpret results

"""

 

import numpy as np

 

# Provided vectors (edit if you want different values)

a = np.array([1.0, 2.0, 3.0])

b = np.array([0.5, 1.0, 1.5])

 

# TODO: Compute dot and cosine similarity

ab = a @ b

a_norm = np.linalg.norm(a)
b_norm = np.linalg.norm(b)
cosine_similarity = ab / (a_norm * b_norm) if a_norm != 0 and b_norm != 0 else 0.0

# Print results
print(f"Dot Product: {ab}")
print(f"Cosine Similarity: {cosine_similarity}")