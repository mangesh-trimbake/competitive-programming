#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n, m):
    return ((pow(10, n, 9 * m) - 1) % (9 * m) // 9)

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

