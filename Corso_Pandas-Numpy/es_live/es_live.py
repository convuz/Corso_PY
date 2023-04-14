import numpy as np


np.random.seed(6)
x = np.round(np.random.normal(size=20), 2)
print(x)

print(x[(x>-2) & (x<-1) | (x>1) & (x<2)])