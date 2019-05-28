#!/usr/bin/python3
# prime.py

import sys
if len(sys.argv) != 2:
    print("prime.py needs 1 argument: the number to be tested")
    sys.exit()
    
prime = int(sys.argv[1])
for i in range(2,prime//2):
    if (prime%i == 0):
        print("Not a prime number")
        print("You can divide it by %d" %i)
        sys.exit()
print("%d is a prime number" %prime)

    
