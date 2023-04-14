# (Usare l'ereditarietà)

# For the purposes of these exercises, you are the director of IT at a zoo. 
# The zoo contains several different kinds of animals, and for budget reasons, 
# some of those animals have to be housed alongside other animals.

# We will represent the animals as Python objects, with each species defined as a distinct class. 
# All objects of a particular class will have the same species and number of legs, 
# but the color will vary from one instance to another.

# We’re going to assume that our zoo contains four different types of animals: sheep, wolves, snakes, and parrots. 
# (The zoo is going through some budgetary difficulties, so our animal collection is both small and unusual.) 
# Create classes for each of these types, such that we can print each of them and get a report on their color, species, and number of legs.

class Animals():
    def __init__(self,species:str, n_of_legs:int, color:str):
        self.species = species
        self.n_of_legs = n_of_legs
        self.color = color

    def get_Attributes(self):
        list = [self.species,self.n_of_legs,self.color]
        return list

class Sheep(Animals):
    def __init__(self, color:str):
        super().__init__(color=color, species = "Sheep", n_of_legs = 4)

# class Wolves(Animals):
#     def __init__(self, n_of_legs: int, color:str):
#         self.species = "Wolves"
#         super().__init__(n_of_legs, color)

# class Snake(Animals):
#     def __init__(self, n_of_legs: int, color:str):
#         self.species = "Snake"
#         super().__init__(n_of_legs, color)

# class Parrot(Animals):
#     def __init__(self, n_of_legs: int, color: str):
#         self.species = "Parrot"
#         super().__init__(n_of_legs, color)

pecora1 = Sheep("Brown")
pecora2 = Sheep("Black")
pecora3 = Sheep("White")
# serpente1 = Snake(0, "Red")
# serpente2 = Snake(0, "Black")
# pappagallo1 = Parrot(2, "Blue")
# pappagallo2 = Parrot(2, "Green")
# pappagallo3 = Parrot(2, "Blue")
# pappagallo4 = Parrot(2, "Red")
# lupo1 = Wolves(4, "White")
# lupo2 = Wolves(4, "White")
# lupo3 = Wolves(4, "White")
# lupo4 = Wolves(4, "White")
# lupo5 = Wolves(4, "Black")
print("1* animale: ",pecora1.get_Attributes())
print("2* animale: ",pecora2.get_Attributes())
print("3* animale: ",pecora3.get_Attributes())
# print("4* animale: ",serpente1.get_Attributes())
# print("5* animale: ",serpente2.get_Attributes())
# print("6* animale: ",pappagallo1.get_Attributes())
# print("7* animale: ",pappagallo2.get_Attributes())
# print("8* animale: ",pappagallo3.get_Attributes())
# print("9* animale: ",pappagallo4.get_Attributes())
# print("10* animale: ",lupo1.get_Attributes())
# print("11* animale: ",lupo2.get_Attributes())
# print("12* animale: ",lupo3.get_Attributes())
# print("13* animale: ",lupo4.get_Attributes())
# print("14* animale: ",lupo5.get_Attributes())        
