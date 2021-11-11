
import math
import os
import random
import re
import sys

print((lambda k, x: (lambda y: k // y * y)(next((i for i in range(2, int(pow(x, 0.5)) + 1) if not x % i), x)))(int(input().split()[1]), __import__("functools").reduce(lambda x, y, gcd=(lambda x, y, gcd: gcd(y % x, x, gcd) if x else y): gcd(x, y, gcd), set(map(int, input().split())))))
