#!/bin/python3

import os
import sys

# Complete the solve function below.

c = 10**9+7
def fact(n):
    result = 1
    while n >= 2:
        result = ((result)*(n%c))%c
        n -= 1
    return result
    
def fastEXP(base, exp, modulus):
    base %= modulus
    result = 1
    
    while exp > 0:
        if exp & 1:
            result = (result * base) % modulus
        base = (base*base)%modulus
        exp >>= 1
        
    return result


def solve(x, y):
    amodc = fact(x+y-2)
    bmodc = fact(x-1)*fact(y-1)
    return ((amodc%c)*(fastEXP(bmodc, (c-2), c)))%c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

