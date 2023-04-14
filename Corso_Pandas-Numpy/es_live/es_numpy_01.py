# Write a function which standardizes the values in a given
# numeric vector, i.e., rescales its elements so that the resulting vector is of mean and standard deviation of 1. 
# Note: this is also called "Z-score computing". (lavorare su ndim=1)

import numpy as np
import scipy.stats as stats

def standard(data):
    dev_standard = np.std(data)
    media = np.mean(data)

    data_sd = (data-media)/dev_standard
    return data_sd


data = np.array([1,2,3,4,7,9,10,12,13])
data_std = standard(data)
print(data_std)
print(np.mean(data_std))
print(np.std(data_std))

#print(stats.zscore(data))




