# Enter your code here. Read input from STDIN. Print output to STDOUT
p=0
n=input()
assert n<=10**6
assert n>=1
a=map(int,raw_input().split())
for i in range(n):
    assert a[i]<=10**9
    assert a[i]>= (-1)*10**9
    p+=a[i]*(i+1)
max_p=p
sigma=sum(a)
for i in range(n):
    p+=sigma
    p-=a[-1-i]*(n)
    if p>max_p:
        max_p=p
print max_p
    

