import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Write a Pandas program 
# to find number of consumption of wine per person greater than 2 in world alcohol consumption dataset

df = pd.read_csv("world_alcohol.csv")
print(df.loc[(df["Display Value"]>2)&(df["Beverage Types"]=="Wine")])

