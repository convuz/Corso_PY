import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Write a Pandas program to filter those records which not appears in a given list from world alcohol consumption dataset.

df = pd.read_csv("world_alcohol.csv")
print(df.loc[~df["WHO region"].isin(["Americas", "Africa"])])





