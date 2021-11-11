#!/bin/python3

import os
import sys

#
# Complete the closestNumber function below.
#
def closestNumber(a, b, x):
    #
    # Write your code here.
    #
    c=(a**b)//x
    if(abs((a**b)-(x*c))>abs((a**b)-(x*(c+1)))):
        return int(x*(c+1))
    else:
        return int(x*c) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = closestNumber(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()

