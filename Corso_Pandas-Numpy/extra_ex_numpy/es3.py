import numpy as np


np.random.seed(6)
x = np.round(np.random.normal(size=20), 2)
print(x)
#for i in x:
    #if i in range(x[1::17]):
        #print(i)
#Print the number and the proportion of nonnegative elements in x.

nonnegative=np.count_nonzero(x>=0)
print(nonnegative)
print(np.mean(x>=0))

#Compute the arithmetic mean of absolute values.

x_abs=np.absolute(x)
print(np.mean(x_abs))

#Determine elements in x which are the least and the most distant from 0.

#Determine 3 elements in x which are the most distant from the arithmetic mean of x.

print(x[np.argsort(np.abs(x-np.mean(x)))[-3:]])

