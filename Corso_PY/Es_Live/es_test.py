#ragionamento:
#se effettivamente si può associare a delle variabili un return di una funzione scritto in quel modo allora esce 1 
#altrimenti penso esca errore
def swap(a, b):
    return b, a

a, b = 1, 2
a, b = swap(a, b)
print(a-b)


#ragionamento:
#se [False] vale come stringa allora stringa_non_vuota == True perciò stampa "no" altrimenti stampa "ciao"
ab= "ciao"
if False or [False] or (False):
    ab = "no"

print(ab)



cc = None
print(type(cc))
