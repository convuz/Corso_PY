# In this exercise, you’ll define a class, Scoop, that represents a single scoop of ice cream. 
# Each scoop should have a single attribute, flavor, a string that you can initialize when you create the instance of Scoop. 
# Once your class is created, write a function (create_scoops) that creates three instances of the Scoop class, 
# each of which has a different flavor. Put these three instances into a list called scoops. 
# Finally, iterate over your scoops list, printing the flavor.

class Scoop():
    def __init__(self,flavor:str):
        self.flavor = flavor

def create_scoops():
    scoop_list = []
    flavor_list = ["Limone", "Arancia", "Mango"]
    for i in flavor_list:
        a = Scoop(i)
        scoop_list.append(a.flavor)
    return scoop_list

print(create_scoops())
