# Now create a function for John Doe and his family that greets every one in the family.
# Since it will usually John Doe the name and surname parameter must be defaulted
# and when someone else comes it has to greet the new comer with name surname parameters which were overwritten. Make it possible.
# The function have to print "Hello John Doe" where John and Doe is parametric
# Greet each our John first then the people in the list with for loop and the function
# What you have to use

# for loop
# function
# string operation
# list index
# Output format

# Hello John Doe!
# Hello Tristram Mcbride!
# Hello Baldwin Preston!
# Hello Wally Collins!

def greetings(*items):
    a = ()
    if items == ():
        #a = "Input vuoto"
        print("Hello John Doe!")
    else:
        name = items[0]
        surname = items[1]
        print(f"Hello {name} {surname}!")

list = [("John", "Doe"), ("Tristram", "Mcbride"), ("Baldwin", "Preston"), ("Wally", "Collins")]

for i in list:
    if i[0] == "John" and i[1] == "Doe":
        greetings()
    else:
        greetings(i[0],i[1])