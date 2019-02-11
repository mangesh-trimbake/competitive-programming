import functools as ft
import math as m

for _ in range(int(input())):
    n = int(input())
    array = [int(temp) for temp in input().split()]
    print('YES' if ft.reduce(m.gcd, array) == 1 else 'NO')
