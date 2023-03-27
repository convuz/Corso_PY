import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Write a Pandas program to filter rows 
# based on row numbers ended with 0, like 0, 10, 20, 30 from world alcohol consumption dataset.

df = pd.read_csv("world_alcohol.csv")
df = df.filter(like = "0", axis=0)
print(df)
