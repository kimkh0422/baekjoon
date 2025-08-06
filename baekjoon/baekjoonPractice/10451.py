import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
from collections import deque

T = int(input())

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        next_node = graph[node]
        if not visited[next_node]:
            visited[next_node] = True
            queue.append(next_node)

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    graph = [0] + numbers  
    visited = [False] * (N + 1)
    count = 0

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
            count += 1

    print(count)
