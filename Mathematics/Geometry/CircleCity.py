#!/bin/python

from __future__ import print_function

import os
import sys

# Complete the solve function below.
def solve(d, k):
    
    r2, k = d,k

    required = 0
    r = r2 ** 0.5

    for x in xrange(0, int(r) + 1):
        low = 0
        high = int(r) + 1
        while low <= high:
            mid = (low + high) / 2
            if x * x + mid * mid == r2:
                if mid == 0 or x == 0:
                    required += 2
                else:
                    required += 4
                if required > k: return "impossible"
                break
            elif x * x + mid * mid < r2:
                low = mid + 1
            else:
                high = mid - 1

    if required > k: return "impossible"

    return "possible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        dk = raw_input().split()

        d = int(dk[0])

        k = int(dk[1])

        result = solve(d, k)

        fptr.write(result + '\n')

    fptr.close()

