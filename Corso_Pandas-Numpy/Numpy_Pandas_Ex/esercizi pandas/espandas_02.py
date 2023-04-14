import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Write a Pandas program to filter those records where WHO region matches with multiple values 
# (Africa, Eastern Mediterranean, Europe) from world alcohol consumption dataset

df = pd.read_csv("world_alcohol.csv")
df = df.drop_duplicates('WHO region')
print(df)
