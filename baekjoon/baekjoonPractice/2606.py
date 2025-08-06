from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
count = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(count):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
def dfs(node):
    if node in visited:
        return
    else:
        visited.add(node)
        
    for neighbor in graph[node]:
        dfs(neighbor)


def bfs(start):
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


dfs(1)
print(len(visited)-1)