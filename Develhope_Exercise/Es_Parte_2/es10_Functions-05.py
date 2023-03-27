# Import random function
# Create a function random_list_summer creates n elemented list with min value = -100 max value = 100 
# it has to print the list first and sum all the elements of it default element number is 15
# Don't forget to call the function
# for some features and functions you might have to search on the internet do it don't lose your courage

import random

def random_list_summer():
    range_list = random.randrange(1, 15)
    list_number = []
    for i in range(range_list):
        list_number.append(random.randrange(-100, 100))
    print(list_number)
    sum_of_list = 0
    for i in list_number:
        sum_of_list += i
    print(sum_of_list)

random_list_summer()