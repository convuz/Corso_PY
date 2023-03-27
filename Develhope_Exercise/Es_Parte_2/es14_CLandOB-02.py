# Ora continua con la classe Animale che avevamo usato prima

# Aggiungi un metodo per contare le gambe count_legs che stampa il numero di gambe

# Aggiungi un metodo per contare le gambe return_legs che restituisca il numero di gambe

# stampa il numero di gambe direttamente dalla number_of_legs variabile dell'oggetto

class Animal():
    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs
        #print("Animal object was created")
          
    def runs(self):
        print("Running started")

    def count_legs(self):
        print(self.number_of_legs)

    def return_legs(self):
        return self.number_of_legs

user = Animal(4)
print(user.number_of_legs)
print(user.return_legs())
user.count_legs()