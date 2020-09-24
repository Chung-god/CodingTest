N,M = map(int,input().split())

result = 0

#한 줄씩 입력받아 확인
for i in range(N):
  	data = list(map(int, input().split()))
  	#현재 줄에서 가장 작은 수 작기
		min_value = 10001
  	for a in data:
			min_value = min(data,min_value)
		result = max(result,min_value)

print(result)