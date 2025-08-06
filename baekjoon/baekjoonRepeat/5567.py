import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

friends = [[] for _ in range(n + 1)]  
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def invite(start):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True
    count = 0

    while queue:
        node, depth = queue.popleft()
        if depth > 2:
            continue
        if depth > 0:
            count += 1
        for neighbor in friends[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, depth + 1))
    return count

print(invite(1))
