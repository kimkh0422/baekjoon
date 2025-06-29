import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[list(map(str,input().strip()))] for _ in range(N)]

def bfs(x,y):
    queue = deque();
    queue.append((x,y))
    graph[y][x]=0

    while queue:
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<M and 0<ny<N and graph[ny][nx]==1:
                graph[ny][nx]=0
                queue.append((nx,ny))

