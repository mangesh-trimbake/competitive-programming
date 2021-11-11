#!/bin/python

import os
import sys

# Complete the solve function below.
def solve(n, k):
    
    loop = n // k
    r = n % k
    pair = k * (loop - 1) * loop // 2 + (r + (k - 1) // 2) * loop
    if r > k // 2:
        pair += r - k // 2
    return(pair)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nk = raw_input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = solve(n, k)

        fptr.write(str(result) + '\n')

    fptr.close()

