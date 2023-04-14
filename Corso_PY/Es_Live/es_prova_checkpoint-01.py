# - creare una funzione che prenda come input due liste di stessa lunghezza e restituisca un dizionario con 
# chiave e valori dati dagli elementi appaiati delle due liste

def createdict(list1, list2):
    dict = {}
    if len(list1) == len(list2):
        for i in range(len(list1)):
            dict.update({list1[i]: list2[i]})
        return dict
    else:
        return "le liste sono di diversa lunghezza"

list1 = ["cane", "gatto", "coniglio", "criceto"]
list2 = [4, 5, 8, 7]
dict1 = createdict(list1, list2)
print(dict1)
