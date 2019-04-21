#!/bin/python

from __future__ import print_function

import os
import sys
from functools import reduce
from fractions import gcd


#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    lcm_a = reduce(lambda x,y: x*y//gcd(x,y), a)
    gcd_b = reduce(gcd, b)
    return(sum(1 for x in range(lcm_a,gcd_b+1,lcm_a) if gcd_b%x==0))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

