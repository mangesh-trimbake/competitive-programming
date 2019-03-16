#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pythagoreanTriple function below.
def pythagoreanTriple(n):
    if n == 4:
        return 3, 4, 5
    elif n % 2 == 0:
        a, b, c = pythagoreanTriple(n//2)
        return a*2, b*2, c*2
    else:
        return n, (n**2 - 1)//2, (n**2 + 1)//2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input())

    triple = pythagoreanTriple(a)

    fptr.write(' '.join(map(str, triple)))
    fptr.write('\n')

    fptr.close()

