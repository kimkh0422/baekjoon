import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
start, finish = map(int,input().split())
m = int(input())

visited = [False]*(n+1)
family = [[] for _ in range(n+1)]

def bfs(start, target):
    queue = deque()
    queue.append((start,0))
    visited[start]=True


    while queue:
        node,count = queue.popleft()
        if node == target:
            return count
        for neighbor in family[node]:
            if visited[neighbor]==False:
                queue.append((neighbor,count+1))
                visited[neighbor]=True
    return -1
               

for _ in range(m):
    x,y = map(int,input().split())
    family[x].append(y)
    family[y].append(x)

print(bfs(start,finish))