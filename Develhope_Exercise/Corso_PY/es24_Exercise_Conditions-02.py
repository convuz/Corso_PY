# check if number1 is greater than number 2 and print number1 is greater than number2 then check and if number 2 is greater than number 1 
# and print number2 is greater than number1 finally at the end if both conditions incorrect print number2 equals to number1


number1 = 66
number2 = 66

if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number2 > number1:
    print(f"{number2} is greater than {number1}")    
else:
    print(f"{number1} equals to {number2}")