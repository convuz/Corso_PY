import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Write a Pandas program to select consecutive columns and also 
# select rows with Index label 0 to 9 with some columns from world alcohol consumption dataset.

df = pd.read_csv("world_alcohol.csv")
print(df.loc[0:9, "Year":"Country"])
