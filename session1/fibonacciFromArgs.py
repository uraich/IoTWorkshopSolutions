#!/usr/bin/python3

# fibonacciFromArgs.py
# calculates the fibonacci numbers up to a number of iterations
# read from the command line
# U. Raich 26.5.2019
# this program is part of the workshop on IoT at the
# African Internet Summit 2019, Kampala, Uganda
# the program is released under GPL

import sys
if len(sys.argv) != 2:
    print("fibonacciFromArgs.py needs 1 argument: the number of iterations")
    sys.exit()
noOfLoops = int(sys.argv[1])
if noOfLoops < 1:
    print("no of iterations must be at least 1")
    sys.exit()
elif noOfLoops == 1:
    print("%d"%0)
    sys.exit()
elif noOfLoops == 2:
    print("%d %d"%(0,1))
    sys.exit()
a=0
b=1
print("Fibonacci numbers of to an interation of 20")
print("%d %d "%(a,b),end='')

for i in range (0,noOfLoops-2):
    c=a+b
    print("%d " % c, end='')
    a=b
    b=c
print()
