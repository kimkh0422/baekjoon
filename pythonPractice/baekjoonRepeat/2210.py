from collections import deque
import sys
input = sys.stdin.readline

numbers = []
result = set()

for _ in range(5):
    number = list(map(str,input().split()))
    numbers.append(number)

def bfs(x,y):
    queue = deque()
    queue.append((x,y,numbers[x][y]))

    while queue:
        x,y,path = queue.popleft()
        if len(path)>=6:
            result.add(path)
            continue

        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = dx+x
            ny = dy+y
            if 0<=nx<5 and 0<=ny<5:
                queue.append((nx,ny,path+numbers[nx][ny]))

for i in range(5):
    for j in range(5):
        bfs(i,j)

print(len(result))
