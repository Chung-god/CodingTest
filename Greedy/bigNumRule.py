N,M,K = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse = True)
bigOne = arr[0]
bigTwo = arr[1]
print(bigOne,bigTwo)

#total = bigOne * K + bigTwo 
#time = M / (K+1)
#plus = (M % (K+1)) / bigOne

#ans = total * time + plus * bigOne
#ans = 반복되는 구간 * 반복되는 횟수 + 나머지는 큰수로 채움 
ans = (bigOne * K + bigTwo) * int(M / (K+1)) + (M % (K+1)) * bigOne
print(int(ans))


