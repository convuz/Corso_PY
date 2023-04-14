# Estrarre l'anno dalla precedente variabile in un modo che non dipenda dalla posizione dell'anno all'interno della stringa.

s6 = "REDDITO_DIPENDENTE_DELL_ANNO_2021"
s6_split = s6.split("_")

#VERSIONE 1
for position in range(len(s6_split)):
    if s6_split[position] == "2021":
        print("Versione 1: " + s6_split[position])

#VERSIONE 2
for i in s6_split:
    if i.isdigit():
        print("Versione 2: " + i)
