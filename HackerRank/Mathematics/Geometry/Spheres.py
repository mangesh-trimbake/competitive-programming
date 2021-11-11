#!/bin/python

import os
import sys
import math
from decimal import *


def inner(list1, list2):
    res = 0
    for i in range(3):
        res += list1[i] * list2[i]
    return res


def P(dete, Dacc, Dpos):
    return inner(Dacc,Dacc)/4*(dete*dete) + inner(Dacc,Dpos)*dete + inner(Dpos,Dpos)

def solve(r1, r2, p1, a1, p2, a2):
    
    k = r1 + r2
    
    Dacc = list() 
    
    Dpos = list() 
    Dacc.append(a1[0]-a2[0])
    Dacc.append(a1[1]-a2[1])
    Dacc.append(a1[2]-a2[2])
    Dpos.append(p1[0]-p2[0])
    Dpos.append(p1[1]-p2[1])
    Dpos.append(p1[2]-p2[2])

    
    if inner(Dpos, Dpos) <=k:
        return "YES"

    

    a = inner(Dacc, Dacc)/4
    b = inner(Dacc, Dpos)
    c = inner(Dpos, Dpos) - k*k

    
    if (b*b - 4*a*c) < 0:
        return "NO"

    sol1 =  (-1*Decimal(b) + Decimal(b*b - 4*a*c).sqrt())

    if sol1 <0:
        return "NO"
        
    value1 = P(float(sol1), Dacc, Dpos)
    
    if value1<k*k:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        r1R2 = input().split()

        r1 = int(r1R2[0])

        r2 = int(r1R2[1])

        position1 = list(map(int, input().rstrip().split()))

        acceleration1 = list(map(int, input().rstrip().split()))

        position2 = list(map(int, input().rstrip().split()))    

        acceleration2 = list(map(int, input().rstrip().split()))

        result = solve(r1, r2, position1, acceleration1, position2, acceleration2)

        

        fptr.write(result + '\n')

    fptr.close()

