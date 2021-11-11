#!/bin/python

import os
import sys
import math

# Complete the solve function below.
def solve(x):
    d = 4*(x+1)
    n = math.ceil((math.sqrt(d) - 2)/2)
    if(int(n)%2 == 0):
        return 'even'
    else:
        return 'odd'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        i = int(raw_input())

        result = solve(i)

        fptr.write(result + '\n')

    fptr.close()

