# In this exercise, we’re going to create a password-generation function. Actually, we’re going to create a factory for password-generation 
# functions. That is, I might need to generate a large number of passwords, all of which use the same set of charac- ters. 
# (You know how it is. Some applications require a mix of capital letters, lowercase letters, numbers, and symbols; 
# whereas others require that you only use letters; and still others allow both letters and digits.) 
# You’ll thus call the function create_password_generator with a string. 
# That string will return a function, which itself takes an integer argument. 
# Calling this function will return a password of the specified length, using the string from which it was created;

# alpha_password = create_password_generator('abcdef') 
# symbol_password = create_password_generator('!@#%') 
# print(alpha_password(5)) # efeaa 
# print(alpha_password(10)) # cacdacbada 
# print(symbol_password(5)) # @!%%
# print(symbol_password(10)) # @!%%%%#

import random

def create_password_generator(str1):    
    def create_pass(n1):
        password=''
        ran=random.randint(0,n1)

        for i in range(ran):
            elem=random.choice(str1)
            password+=elem
            
        return password

    return create_pass

alpha_password = create_password_generator('abcdef') 
symbol_password = create_password_generator('!@#%') 
print(alpha_password(5)) # efeaa 
print(alpha_password(10)) # cacdacbada 
print(symbol_password(5)) # @!%%
print(symbol_password(10)) # @!%%%%#