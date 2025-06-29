from collections import deque
import sys

input = sys.stdin.readline

n, m = 3, 4
graph = [
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return
    elif graph[x][y]==0:
        return
    else:
        graph[x][y]=0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y]=0

    while queue:
        x,y  = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))

       
        
