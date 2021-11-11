#!/bin/python3

import os
import sys
import math as m
from math import hypot
from itertools import combinations, islice
# Complete the solve function below.

def solve(coordinates):
    li=[]
    xmax,xmin,ymax,ymin=[0,0,0,0]
    for i in coordinates:
        x,y=i[0],i[1]
        if(i==0):
                xmax=x
                xmin=x
                ymax=y
                ymin=y
        else:
            if(x>xmax):
                xmax=x
            if(x<xmin):
                xmin=x
            if(y>ymax):
                ymax=y
            if(y<ymin):
                ymin=y

    li.append(xmax-xmin)
    li.append(ymax-ymin)
    li.append(m.sqrt(xmax*xmax+ymax*ymax))
    li.append(m.sqrt(xmax*xmax+ymin*ymin))
    li.append(m.sqrt(xmin*xmin+ymax*ymax))
    li.append(m.sqrt(xmin*xmin+ymin*ymin))
    return(max(li))

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()

