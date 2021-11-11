from math import *
for _ in range(input()):
  n,k=[int(x) for x in raw_input().split()]
  d=n**2 - 4*n*k
  if d<=0:
    print(n-1)
  else:
    print(2* int((n-ceil(sqrt(d)))/2))
