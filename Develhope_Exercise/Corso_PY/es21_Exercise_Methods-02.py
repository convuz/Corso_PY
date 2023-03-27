# the number types can be converted to each other wit the int() float() complex() methods also float numbers 
# can be rounded with the method round()

# convert num1 to float and assign to itself
# convert num2 to int and assign to itself
# convert num3 to complex and assign to itself
# use round method for num4 and assign to itself
# use round method for num5 and assign to itself
# print them all
# print their types

num1 = 1.3
num2 = 2.3
num3 = 1j 
num4 = 1.4 
num5 = 1.5

print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))
print(num1, '', num2, '', num3, '', num4, '', num5)

num1 = float(num1)
num2 = int(num2)
num3 = complex(num3)
num4 = round(num4)
num5 = round(num5)

print('\n')
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))
print(num1, '', num2, '', num3, '', num4, '', num5)
