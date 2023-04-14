import numpy as np
import matplotlib.pyplot as plt


arr2 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
arr2_copy = arr2.copy()
print(arr2.shape)
print(arr2_copy)
print(np.median(arr2))

s = np.random.normal(loc=3, scale=4, size=(100))
#plt.plot(s)
plt.hist(s)
plt.show()