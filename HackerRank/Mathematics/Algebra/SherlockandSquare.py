#!/bin/python

import os
import sys

# Complete the solve function below.
m=10**9+7
def mpow(a,n):
    if n==0: return 1
    elif n==1: return a
    p=mpow(a,n/2)
    if (n&1):
        return (p*p*a)%m
    else: return (p*p)%m

def solve(n):
    return (4+2*(mpow(2,n)-1))%m


  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()

