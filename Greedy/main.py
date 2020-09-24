list = [500,100,50,10]

N = int(input())
t = 0
coin = 0
while N != 0:
  if N >= list[t]:
    N -= list[t]
    print(list[t])
    coin += 1
  else: 
    t += 1

print(coin)