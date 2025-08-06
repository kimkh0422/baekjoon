import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)



def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[y][x]=0
    house_count = 1

    while queue:
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = dx + x
            ny = dy + y
            if 0<=nx<N and 0<=ny<N and graph[ny][nx]==1:
                graph[ny][nx]=0
                queue.append((nx,ny))
                house_count+=1
    return house_count



N = int(input())

graph = [list(map(int,input().strip()))for _ in range(N)]

total_count = 0
houseList = []
for y in range(N):
    for x in range(N):
        if graph[y][x]==1:
            houseList.append(bfs(x,y))
            total_count +=1
print(total_count)

for count in sorted(houseList):
    print(count)