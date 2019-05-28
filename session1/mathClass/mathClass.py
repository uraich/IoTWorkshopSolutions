#!/usr/bin/python3

# mathClass.py
# a Python class with 3 mathematical methods:
# prime, fibonacci and factorial
# U. Raich 26.5.2019
# this program is part of the workshop on IoT at the
# African Internet Summit 2019, Kampala, Uganda
# the program is released under GPL

class MathFuncs:
    #
    # the methodod calculating the factorial of a number
    #
    def factorial(self,number):
        if number < 0:
            raise ValueError("number must be positive")
        if number == 0:
            return 0        
        fact = 1
        for i in range(1,number+1):
            fact=fact*i
        print("Factorial of %d: %d"%(number,fact))
        return fact
    #
    # the method testing if a number is a prime number
    #
    def prime(self,testPrime):
        if testPrime < 0:
            return False
        if testPrime < 4:
            return True
        for i in range(2,testPrime//2+1):
            if (testPrime%i == 0):
                # print("%d is not a prime number"%testPrime)
                # print("You can divide it by %d" %i)
                return False
        # print("%d is a prime number" %testPrime)
        return True
    #
    # the method calculating the Fibonacci series
    #
    def fibonacci(self,noOfIterations):
        if noOfIterations < 1:
            raise ValueError("no of iterations too small")
        fib=[]
        fib.append(0)
        if noOfIterations == 1:
            print("%d"%0)
            return fib
        fib.append(1)
        if noOfIterations == 2:
            print("%d %d"%(0,1))
            return fib
        print("Fibonacci numbers of to an interation of 20")
        print("%d %d "%(fib[0],fib[1]),end='')

        for i in range (0,noOfIterations-2):
            fib.append(fib[i] + fib[i+1])
            print("%d " % fib[i+2], end='')
            
        print()
        return fib

