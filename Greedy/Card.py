N,M = map(int,input().split())
minArr = []
while N > 0:
  data = list(map(int,input().split()))
  minArr.append(min(data))
  N -= 1

print(max(minArr))