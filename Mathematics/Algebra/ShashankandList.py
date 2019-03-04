#!/bin/python3

import os
import sys
from functools import reduce

# Complete the solve function below.
def solve(A):
    m = 10 ** 9 + 7
    ans = reduce(lambda a, b: a * b % m, [1 + pow(2, int(x), m) for x in A], 1)-1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()

