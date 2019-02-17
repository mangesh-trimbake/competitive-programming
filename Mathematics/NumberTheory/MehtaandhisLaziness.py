#!/bin/python

from __future__ import print_function

import os
import sys
import math
from fractions import Fraction

# Complete the solve function below.
def solve(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            divisors.append(i)
            if(n//i != i):
                divisors.append(n//i)
    divisors.sort()
    count = 0
    for i in divisors:
        if i%2==0 and math.sqrt(i)==math.ceil(math.sqrt(i)):
            count+=1
    if count == 0:
        return "0"
    else:
        return str(Fraction(count,len(divisors)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

