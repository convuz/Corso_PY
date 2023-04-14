import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

#plot in base all'età di chi è sopravvissuto e chi no
# df_alive = df.loc[df.Survived == 1, "Age"].hist()
# plt.show()
# df_dead = df.loc[df.Survived == 0, "Age"].hist()
# plt.show()

#percentuali di maschi e femmine vivi e morti
# dfm=df.loc[df.Sex=="male"].shape
# print("maschi tot:",dfm)
# dff=df.loc[df.Sex=="female"].shape
# print("femmine tot:",dff)
# print("------")
# dfm1=df.loc[(df.Sex=="male") & (df.Survived==0)].shape
# print("morti: ",dfm1)
# dfm2=df.loc[(df.Sex=="male") & (df.Survived==1)].shape
# print("vivi: ",dfm2)
# dfmperc=(df.loc[(df.Sex=="male") & (df.Survived==1)].shape[0])/(df.loc[df.Sex=="male"].shape[0])
# print("percentuale di maschi vivi: ",dfmperc)


#distribuzione di maschi e femmine con groupby

df11=df.groupby("Sex").count()
print(df11["PassengerId"])

df22=df.groupby(["Sex","Survived"]).count()
print(df22["PassengerId"])

print((df22["PassengerId"][1])/df11["PassengerId"][0])
print((df22["PassengerId"][3])/df11["PassengerId"][1])
df33=df22.div(df11, axis=0, level="Sex")
print(df33["PassengerId"])

dfprova=df.groupby(["Sex","Survived","Pclass"]).count()
dfv=dfprova.div(df11, axis=0, level="Sex")
print(dfv["PassengerId"])