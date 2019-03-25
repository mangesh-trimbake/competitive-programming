

n=input()
a=map(int,raw_input().split())
mod=1000000007
x=a[0]
for i in range(1,n):
    c=a[0]
    d=a[i]
    a[0]=(c+d+c*d)%mod
print a[0]

