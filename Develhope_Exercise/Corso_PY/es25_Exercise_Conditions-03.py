# Compare those 2 numbers and write X greater than Y But be sure you are making the check for all the conditions

import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

# Compare the numbers to eachother

#print(f"number1: {number1} and number2: {number2}")

if number1 > number2:
    print(f"X is greater than Y")
elif number2 > number1:
    print(f"Y is greater than X")    
else:
    print(f"X equals to Y")