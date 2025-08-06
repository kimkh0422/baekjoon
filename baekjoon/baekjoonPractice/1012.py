from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx, ny))

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                bfs(x, y)
                count += 1

    print(count)
