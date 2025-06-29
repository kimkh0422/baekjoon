import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    count = 0
    queue = deque()
    queue.append((start,0))
    visited[start] = True

    while queue:
        node,depth = queue.popleft()
        if depth>=2:
            continue
        for neighbor in graph[node]:
            if visited[neighbor]==False:
                visited[neighbor]=True
                count +=1
                queue.append((neighbor,depth+1))

    return count

print(bfs(1))