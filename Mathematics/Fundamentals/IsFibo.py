#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n):
    fib1,fib2 = 0,1
    while n>fib2:
        fib1, fib2 = fib2, fib1+fib2
    return("IsFibo" if fib2==n else "IsNotFibo")
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

