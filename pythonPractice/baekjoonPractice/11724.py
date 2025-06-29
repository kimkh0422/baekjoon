import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

N, M = map(int,input().split())
visited = [False]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start]=True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor]==False:
                visited[neighbor]=True
                queue.append(neighbor)

count = 0
for i in range(1,N+1):
    if visited[i]==False:
        bfs(i)
        count+=1
print(count)