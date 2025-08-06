from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int,input().split())

graph=[[]for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

visited_dfs = set()
visited_bfs = set()

def dfs(node):
    if node in visited_dfs:
        return
    else:
        visited_dfs.add(node)
        print(node, end=' ')
    for neighbor in graph[node]:
        dfs(neighbor)

def bfs(start):
    queue = deque([start])
    visited_bfs.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited_bfs:
                queue.append(neighbor)
                visited_bfs.add(neighbor)

dfs(V)
print()
bfs(V)
