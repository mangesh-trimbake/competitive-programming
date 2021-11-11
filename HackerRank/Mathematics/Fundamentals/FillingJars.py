n,m = map(int, input().split())
candies=0
for _ in range(m):
    a,b,k = map(int, input().split())
    candies += (b-a+1)*k
print(candies//n)
