#!/usr/bin/python3
# fibonacci.py
# calculates the fibonacci numbers up to an iteration of 20
# U. Raich 26.5.2019
# this program is part of the workshop on IoT at the
# African Internet Summit 2019, Kampala, Uganda
# the program is released under GPL

noOfLoops = 20
a=0
b=1
print("Fibonacci numbers of to an interation of 20")
print("%d %d "%(a,b),end='')

for i in range (0,noOfLoops):
    c=a+b
    print("%d " % c, end='')
    a=b
    b=c
print()
