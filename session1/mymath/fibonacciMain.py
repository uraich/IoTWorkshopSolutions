#!/usr/bin/python3

from fibonacci import fibonacci
print("The first 25 Fibonacci numbers are:")
try:
    fib = fibonacci(25)
except ValueError as e:
    print(str(e))
    
