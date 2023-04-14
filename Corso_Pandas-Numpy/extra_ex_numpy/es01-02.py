import numpy as np
from scipy import stats

x = np.array([1,2,4,5,6])
y = np.array([-1,-4,4,7,9])

my_rho = np.corrcoef(x, y)

print(stats.spearmanr(x, y, axis=0, nan_policy='propagate', alternative='two-sided'))

print(my_rho)

np.random.seed(6)
x = np.round(np.random.normal(size=20), 2)
print(x)
print(x[-2:-1], x[1:2])
print
