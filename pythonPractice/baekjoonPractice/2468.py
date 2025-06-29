from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y, rain_height, visited):
    queue = deque()
    queue.append((x, y))
    visited.add((x, y))

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if (nx, ny) not in visited and graph[ny][nx] > rain_height:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

max_safe_area = 0

for rain in range(0, 101):  # 강수량 0부터 100까지
    visited = set()
    count = 0

    for y in range(N):
        for x in range(N):
            if (x, y) not in visited and graph[y][x] > rain:
                bfs(x, y, rain, visited)
                count += 1

    max_safe_area = max(max_safe_area, count)

print(max_safe_area)
