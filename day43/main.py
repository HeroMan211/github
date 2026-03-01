"""

Day 43 Activity: Probability Computation with SciPy

Tasks:

1) Compute CDF-based probability for a range

2) Use PPF for quantiles

3) Verify with Monte Carlo

"""

 

import numpy as np

from scipy import stats

 

# TODO: Define distribution
dist = np.random.normal(loc=0, scale=1, size=1000)

# TODO: Compute P(a<=X<=b)
print("CDF at x=1:", stats.norm.cdf(1)) 

# TODO: Compare with Monte Carlo
print("Monte Carlo estimate:", np.mean(dist <= 1))