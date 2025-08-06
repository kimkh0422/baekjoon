import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)  # 정답을 저장할 배열

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if visited[neighbor]==False:
            parent[neighbor] = node  # 부모 저장
            dfs(neighbor)

dfs(1)  # 1번 노드를 루트로 탐색 시작

# 2번 노드부터 부모 출력
for i in range(2, N + 1):
    print(parent[i])
