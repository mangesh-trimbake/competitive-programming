#!/bin/python

import math
import os
import random
import re
import sys

def getSumOfDigit(n):
    strn = str(n)
    nl = [int(x) for x in strn]
    # print (n,sum(nl))
    return sum(nl)

def divisors(n):
    divs = [1]
    large = 1
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
            # print(i,getSumOfDigit(i))
            if(getSumOfDigit(i)>getSumOfDigit(large)):
                large = i
                # print(large)
            # print(n/i,getSumOfDigit(n/i))
            if(getSumOfDigit(n/i)>getSumOfDigit(large)):
                large = n/i
                # print(large)
    divs.extend([n])
    if(getSumOfDigit(n)>getSumOfDigit(large)):
        large = n
        # print(large)
    
    return list(set(divs)),large

if __name__ == '__main__':
    n = int(raw_input())
    # print(divisors(n))
    setl,ans = divisors(n)
    print(ans)
    

