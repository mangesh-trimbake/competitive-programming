import math

def triangular(num):
    if math.sqrt(8*num+1)%1 == 0:
        return math.floor(math.sqrt(8*num+1)/2)

testcases = int(input())
for x in range(testcases):
    num = int(input())
    result = triangular(num)
    if result: print("Go On Bob", result)
    else: print("Better Luck Next Time")
