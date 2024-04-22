n,q = map(int,input().split())
data = [int(s) for s in input().split()]
data.sort()
res = [1]*n

for i in data:
  if res[i-1] == 1:
    res[i-1] = 0
  else:
    res[i-1] = 1

print(sum(res))
