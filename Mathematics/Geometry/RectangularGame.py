X, Y = [], []
for i in range(int(input())):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)
print(min(X) * min(Y))
