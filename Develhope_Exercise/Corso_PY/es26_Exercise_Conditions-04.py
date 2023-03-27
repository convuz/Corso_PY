# Compare those 2 numbers' absolute values and write X's absolute value greater than Y's absolute value Use abs function to do that
# eg.
# abs(-5) -> 5
# abs function makes all numbers positive

import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print(f"X'absolute value greater than Y'absolute value")
elif abs(number2) > abs(number1):
    print(f"Y'absolute value greater than X'absolute value")    
else:
    print(f"X'absolute value equals to Y'absolute value")
    