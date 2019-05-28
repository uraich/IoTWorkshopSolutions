#!/usr/bin/python3

# factorial.py
# calculates the factorial of a number
# U. Raich 26.5.2019
# this program is part of the workshop on IoT at the
# African Internet Summit 2019, Kampala, Uganda
# the program is released under GPL

def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact=fact*i
    print("Factorial of %d: %d"%(number,fact))
    return fact

if __name__ == "__main__":
    fact = factorial(4)
          
