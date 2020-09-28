'''
문제 - 모험가 길드
내용 : 공포도의 값과 같은 모임 생성, 최대 모임 출력 
'''
n = int(input())
player = list(map(int,input().split()))
player.sort()
n = n -1
result = 0
while True:
    if n < 0: 
        break
    n -= player[n]
    result += 1

print(result)