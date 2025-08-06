import sys
input = sys.stdin.readline

N, K = map(int,input().split())

people = []
result = []

for i in range(1,N+1): #사람번호가 1부터라
    people.append(i)

index = 0
while people:
    index = (index+K-1) % len(people) #-1을 하는 이유는 숫자 1번인 사람은 0번 인덱스이기 때문이다.
    result.append(people.pop(index))


print("<"+", ".join(map(str,result))+">")

