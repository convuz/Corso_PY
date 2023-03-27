# Let's see what is your user name on your computer
# to do that we are going to use os module which is a built in module in python
# and has many built in functions in it

# to be able to use os functions
# import os then call getlogin method of the module
# then assign the output to user variable and print the user

import os

user = os.getlogin()
print(user)