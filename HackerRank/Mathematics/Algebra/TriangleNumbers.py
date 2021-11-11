#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n):
    if n%2!=0:
        return 2
    n-=4
    n//=2
    if n%2==0:
        return 3
    return 4

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()

