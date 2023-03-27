# Create a lambda function that returns 2nd power of given number if its even
# and run it on the given list
# then print the result to the screen

my_list= [*range(5)] 
x = lambda n : pow(n,2)
print(my_list)
for i in my_list:
    print(x(i))