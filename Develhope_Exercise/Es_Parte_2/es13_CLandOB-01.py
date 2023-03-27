# Let's create Animal class and then create the animal object that runs and having 4 legs

# create animal object with leg count when created print "Animal object was created" and then 
# call runs method of it and it prints "Running started"


class Animal():
    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs
        print("Animal object was created")
          
    def runs(self):
        print("Running started")

user = Animal(4)
user.runs()