import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  #전체 사람 수수
a, b = map(int,input().split())
m = int(input())  #관계 개수

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, target):
    
    queue = deque()
    queue.append((start,0))
    visited[start]=True

    while queue:
        node,depth = queue.popleft()
        if node == target:
            return depth
        for neighnor in graph[node]:
            if visited[neighnor]==False:
                visited[neighnor]=True
                queue.append((neighnor,depth+1))
    return -1
print(bfs(a,b))