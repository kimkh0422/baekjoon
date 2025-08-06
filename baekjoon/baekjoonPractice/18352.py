import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)  
result = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    queue = deque()
    queue.append((start,0))
    visited[start]=True

    while queue:
        node, depth = queue.popleft()
        if depth ==K:
            result.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor]=True
                queue.append((neighbor,depth+1))
        


bfs(X)

if not result:
    print(-1)
else:
    result.sort()
    for city in result:
        print(city)
