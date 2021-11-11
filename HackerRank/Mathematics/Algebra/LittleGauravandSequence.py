#!/bin/python3

import os
import sys
import math

# Complete the solve function below.
def solve(n):
    x=math.log(n)/math.log(2);
    y=int(x+1);
    s=0;
    if(y==1):
        s=2
    else:
        s=(y-1)*6;
    a=s%10;
    b=5;
    if(n%2==0):
        b=1;
    c=(a*b)%10;
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()

