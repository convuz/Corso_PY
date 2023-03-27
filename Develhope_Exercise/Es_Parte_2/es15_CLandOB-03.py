# Again let's keep talking on Animal class we have.
# with 3 methods we just reached the number of legs
# to prevent direct interacting with the class variables
# most of the other programming languages have encapsulation.
# But in python we don't have it instead we use _ prefix for it as convention
# it is also same for the methods

# _legs this shows us not to touch this variable its up to you if you want to change it you can but _ asks you politely not to do it.

# Change the number_of_legs to conventional private variable and call from another method

class Animal():
    def __init__(self, number_of_legs):
        self.__number_of_legs = number_of_legs
        #print("Animal object was created")
          
    def runs(self):
        print("Running started")

    def count_legs(self):
        print(self.__number_of_legs)

    def return_legs(self):
        return self.__number_of_legs

    def returnPRvariable(self):
        return self.__number_of_legs

user = Animal(4)
print(user.returnPRvariable())
print(user.return_legs())
user.count_legs()