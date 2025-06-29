from collections import deque
import sys

input = sys.stdin.readline
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

visited = set()

def dfs(node):
    if node in visited:
        return
    else:
        visited.add(node)
        print(node,end=' ')
    
    for neighbor in graph[node]:
        dfs(neighbor)

def bfs(start):
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node,end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

