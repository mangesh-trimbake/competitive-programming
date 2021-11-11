#!/bin/python

import os
import sys

# Complete the solve function below.
def solve(s):
    m=10**9+7
    li = [int(s[-k - 1]) * pow(2, len(s) - k - 1, m) * pow(11, k, m) % m for k in xrange(len(s))]
    return sum(li)%m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(str(result) + '\n')

    fptr.close()


