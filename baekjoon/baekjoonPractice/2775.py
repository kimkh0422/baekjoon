import sys
input = sys.stdin.readline

T = int(input())

def people(a,b):  # a는 층 b는 호
    if a==0:
        return b
    if b==1:
        return 1
    if rooms[a][b] != -1:
        return rooms[a][b]
    else:
        rooms[a][b] = people(a-1,b)+people(a,b-1)
        return rooms[a][b]


for _ in range(T):
    k = int(input())  #층 즉 행임
    n = int(input())  #호 즉 열임
    rooms = [[-1]*(n+1) for _ in range(k+1)]
    print(people(k,n))
