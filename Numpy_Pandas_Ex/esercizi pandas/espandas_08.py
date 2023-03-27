import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Write a Pandas program to 
# filter all records starting from the 2nd row, access every 5th row from world alcohol consumption dataset.

df = pd.read_csv("world_alcohol.csv")
print(df.filter(regex="[2, 7]$", axis=0))
