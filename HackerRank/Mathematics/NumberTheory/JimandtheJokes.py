#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(dates):
    counts = [0]*100

    for m,d in dates:
        print(m,d)
        try:counts[int(str(d),m)]+=1
        except:pass

    return(sum(c*(c-1)//2 for c in counts))
    # print(dates)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    dates = []

    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))

    result = solve(dates)

    fptr.write(str(result) + '\n')

    fptr.close()

