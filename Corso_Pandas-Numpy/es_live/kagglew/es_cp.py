import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

#una lista dei nomi delle colonne quantitative

df_lista=df.dtypes
df1=df_lista.loc[df_lista != "object"]
lista_colonne=list(df1.index)
print(lista_colonne)

#su queste colonne vogliamo sapere la differenza tra il 3 iq e il 1
df_descr=df.describe()
df_iqr=(df_descr.loc["75%"])-(df_descr.loc["25%"])

q1=df_descr.loc["25%"]
q3=df_descr.loc["75%"]

#calcola i valori anomali
#lower=q1-1,5*iqr
#upper=q3+1,5*iqr
lower=q1-(1.5*df_iqr)
upper=q3+(1.5*df_iqr)
# print(lower)
# print(upper)

#Trova gli Outliers(delle colonne Fare e Age)
def get_outliers(x):
    lower = x.quantile(0.25) - (x.quantile(0.75) - x.quantile(0.25))*1.5
    upper = x.quantile(0.75) + (x.quantile(0.75) - x.quantile(0.25))*1.5
    return x[ ((x<lower) | (x>upper))]
age_outliers = df[['Age']].apply(get_outliers)
fare_outliers = df[['Fare']].apply(get_outliers)

print(age_outliers)
print("---------------------")
print(fare_outliers)