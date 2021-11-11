#!/bin/python

from __future__ import print_function

import os
import sys
import math

#
# Complete the divisors function below.
#
def divisors(n):
    #
    # Write your code here.
    #
    count = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0 and i%2==0:
            # i is even
            count+=1
        if n%(n//i)==0 and (n//i)%2==0:
            # n//i is even and n's factor
            count+=1
        if i==n//i and i%2==0 and n%i==0:
            # if i is sqrt reduce by 1
            count-=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())
        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()

