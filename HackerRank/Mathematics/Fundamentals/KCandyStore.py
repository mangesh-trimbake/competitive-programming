import os
import sys
from collections import defaultdict

ans = defaultdict(lambda:0)

ans[(1,0)] = 1
ans[(1,1)] = 1

def compute_ncr(n,r):
    p = 1000000000
    for i in range(2,n+1):
        for j in range(i+1):
            ans[i,j] = (ans[(i-1,j)]%p + ans[(i-1,j-1)]%p)%p

compute_ncr(1999,999)

for _ in range(int(input())):
    n = int(input())
    r = int(input())
    
    print(ans[(n+r-1,n-1)])

