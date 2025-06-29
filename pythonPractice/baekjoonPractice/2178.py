import sys
from collections import deque
input = sys.stdin.readline


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    

    while queue:
        x,y = queue.popleft()
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = dx + x
            ny = dy + y
            if 0<=nx<M and 0<=ny<N and graph[ny][nx]==1:
                graph[ny][nx] = graph[y][x]+1
                queue.append((nx,ny))


N,M = map(int,input().split())

graph = [list(map(int,input().strip())) for _ in range(N)]

bfs(0,0)

print(graph[N-1][M-1])
