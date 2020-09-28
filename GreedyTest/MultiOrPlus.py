'''
+ 와 * 으로 가장 큰 수 출력 
'''
N = list(map(int,input()))
N.sort()
print(N)

result = 0

for i in N:
    print(i)
    if i == 0:
        continue
    else:
        if result == 0:
            result += i
        else:
            result = result * i

print(result)
