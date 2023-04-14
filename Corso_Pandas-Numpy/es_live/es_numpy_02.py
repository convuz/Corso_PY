# Write a function which standardizes the values in each column of
# a given matrix (separately). (lavorare su ndim=2)

import numpy as np
import scipy.stats as stats

def standard(data):
    dev_standard = np.std(data, axis=0)
    media = np.mean(data, axis=0)

    data_sd = (data-media)/dev_standard
    return data_sd


matrice = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrice_std = standard(matrice)
print(matrice_std)
print("standard deviation= ", np.std(matrice_std, axis =0))
print("media= ", np.mean(matrice_std, axis=0))

print(stats.zscore(matrice))