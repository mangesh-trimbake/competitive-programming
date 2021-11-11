#!/bin/python3

import os
import sys
import math
from math import factorial


# Complete the solve function below.
def solve(n, m):
    k=math.factorial(n+m-1)
    a=math.factorial(n)*math.factorial(m-1)
    k=k//a
    return (k%1000000007)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

