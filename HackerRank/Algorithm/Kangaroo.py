#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def kangaroo(x1, v1, x2, v2):
    X = [x1, v1]
    Y = [x2, v2]
    back = min(X, Y)
    fwd = max(X, Y)
    dist = fwd[0] - back[0]

    while back[0] < fwd[0]:
        back[0] += back[1]
        fwd[0] += fwd[1]
        if fwd[0] - back[0] >= dist:
            break

    return ["NO", "YES"][back[0] == fwd[0]]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

