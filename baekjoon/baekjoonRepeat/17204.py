import sys
input = sys.stdin.readline

N, K = map(int, input().split())
students = [int(input()) for _ in range(N)]
visited = [False] * N

idx = 0
count = 0

while True:
    if idx == K:
        print(count)
        break
    if visited[idx]:
        print(-1)
        break
    visited[idx] = True
    idx = students[idx]
    count += 1
