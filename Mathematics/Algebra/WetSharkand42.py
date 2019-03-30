#!/bin/python

import os
import sys

# Complete the solve function below.
def solve(s):
    MOD = 10**9 + 7
    twenties = s // 20
    rem = s % 20
    if rem == 0:
        return((42 * twenties - 2) % MOD)
    else:
        return((42 * twenties + 2 * rem) % MOD)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        s = int(raw_input())

        result = solve(s)

        fptr.write(str(result) + '\n')

    fptr.close()


    
