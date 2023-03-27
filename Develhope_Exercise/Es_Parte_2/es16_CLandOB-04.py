# Let's inherit Dog class from Animal add name(private) attribute to Dog class and then bark method to print woof woof

# print name_of_dog make it bark count the legs

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

class Dog(Animal):
    def __init__(self, number_of_legs, name_of_dog):
        super().__init__(number_of_legs)
        self.__name_of_dog = name_of_dog
    
    def bark(self):
        print("woof woof")

    def return_name_of_dog(self):
        return self.__name_of_dog

user = Dog(4,"Holly")
user.bark()
print(user.return_name_of_dog())
print(user.return_legs())