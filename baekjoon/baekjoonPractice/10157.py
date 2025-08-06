import sys
input = sys.stdin.readline

C, R = map(int, input().split())  # C: 가로, R: 세로
K = int(input())

# 전체 좌석 개수보다 K가 더 크면 불가능
if K > R * C:
    print(0)
    sys.exit()

board = [[0] * C for _ in range(R)]

#우선 방향설정을 하자
dx = [0,1,0,-1]
dy = [-1,0,1,0]

x,y = 0,R-1
dir = 0
num = 1
board[y][x] = num

while num<K:
    nx = x+dx[dir]
    ny = y+dy[dir]

    if nx<0 or nx>=C or ny<0 or ny>=R or board[ny][nx]!=0:
        dir = (dir+1)%4
        continue

    num+=1
    x,y = nx,ny
    board[y][x]=num

print(x+1,R-y)