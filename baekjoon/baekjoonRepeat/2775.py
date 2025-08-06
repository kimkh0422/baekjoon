import sys
input = sys.stdin.readline

T = int(input())

def number(k,n):
    if k==0:
        return n
    if n==1:
        return 1
    
    if rooms[k][n]!=0:
        return rooms[k][n]
    
    rooms[k][n] = number(k-1,n) + number(k,n-1)
    return rooms[k][n]

for _ in range(T):
    k = int(input()) #층
    n = int(input()) #호
    rooms = [[0]*(n+1) for _ in range(k+1)]
    print(number(k,n))




