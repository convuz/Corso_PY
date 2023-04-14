# - creare una funzione che prenda come input una lista di stringhe e restituisca un dizionario con 
# chiavi date dalle varie stringhe e valori dati dalle stringhe scritte al contrario (es. "ciao": "oaic")

def createrevstr(list1):
    dict = {}
    for i in list1:
         dict.update({i: i[::-1]})
    return dict

list1 = ["ciao", "come", "stai"]
dict1 = createrevstr(list1)
print(dict1)