#!/usr/bin/python3

# math.py
# a main program creating a mathClass object and testing its three methods
# U. Raich 26.5.2019
# this program is part of the workshop on IoT at the
# African Internet Summit 2019, Kampala, Uganda
# the program is released under GPL

from mathClass import MathFuncs

myMath = MathFuncs()
print("Trying fibonacci(0)")
try:
    myMath.fibonacci(0)
except ValueError as e:
    print(str(e))
    
print("Fibonacci(25)")
try:
    myMath.fibonacci(25)
except ValueError as e:
    print(str(e))

print("Factorial(10):")

print(myMath.factorial(10))

for i in range(0,10000):
    if myMath.prime(i):
        print (i)

