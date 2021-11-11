#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd

def solve(n,a):
    if (n == 1):
        print(a[0] + 1)
    
    leftGCDs = [0 for i in range(0,n)]
    leftGCDs[0] = a[0]
    for i in range(1,n): 
        leftGCDs[i] = gcd(leftGCDs[i - 1], a[i])    
    # print("left ",leftGCDs)
    rightGCDs = [0 for i in range(0,n)]
    rightGCDs[n - 1] = a[n - 1];
    for i in range(n-2,0,-1):
        # print("i",i)
        rightGCDs[i] = gcd(rightGCDs[i + 1], a[i])
    # print("right ",rightGCDs)
    i = 0
    while(True):
        if(i == 0):
            # print("v ",rightGCDs[i + 1])
            if (a[i] % rightGCDs[i + 1] != 0):
                return rightGCDs[i + 1]

        elif(i == n-1):
            if (a[i] % leftGCDs[i - 1] != 0):
                return leftGCDs[i - 1]
        else:
            otherGCD = gcd(leftGCDs[i - 1], rightGCDs[i + 1])
            if (a[i] % otherGCD != 0):
                return otherGCD
        i = i+1


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    # Write Your Code Here
    print(solve(n,a))
    

    
    
