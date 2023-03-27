# Implement Fibonacci sequence as recursive function and print first 5 elements.

def Fibonacci_ricorsiva(n):
    if n > 1:
        return Fibonacci_ricorsiva(n-1) + Fibonacci_ricorsiva(n-2)
    return n

n = 5

for i in range(1, n+1):
    print(Fibonacci_ricorsiva(i))