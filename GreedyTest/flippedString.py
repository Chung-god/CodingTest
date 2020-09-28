#문자열을 뒤집어서 모두 동일한 수가 되게 만들기 
S = input()
print(S)
standard0 =' '. join(S.split('0')).split()
standard1 =' '. join(S.split('1')).split()
#print(standard0)
#print(standard1)
if len(standard0) >= len(standard1) :
    print(len(standard1))
else:
    print(len(standard0))