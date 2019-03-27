#!/bin/python

import os
import sys
from collections import Counter

# Complete the solve function below.
def solve(n,A):
    
    return(A[2] * (A[2] - 1) // 2 + A[1] * (n - 1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = map(int, input().rstrip().split())

        result = solve(a_count,Counter(a))

        fptr.write(str(result) + '\n')

    fptr.close()

