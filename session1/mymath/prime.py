#!/usr/bin/python3
# prime.py
    
def prime(testPrime):
    for i in range(2,testPrime//2):
        if (testPrime%i == 0):
            print("Not a prime number")
            print("You can divide it by %d" %i)
            return False
    print("%d is a prime number" %prime)
    return True
    
