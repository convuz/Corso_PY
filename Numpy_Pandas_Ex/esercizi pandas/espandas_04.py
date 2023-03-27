import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Write a Pandas program to filter all records where the average consumption of beverages per person from 
# .5 to 2.50 in world alcohol consumption dataset

df = pd.read_csv("world_alcohol.csv") 
print(df.loc[(df["Display Value"]>0.5) & (df["Display Value"]<2.5)])


