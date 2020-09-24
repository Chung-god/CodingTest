N,K = map(int,input().split())
time = 0
while N != 1:
	rest = N % K
	time += rest
	N -= rest
	N = int(N/K)
	time+=1

print(time)