import sys
import heapq

input = sys.stdin.readline

# 도시 수, 버스 수 입력
N = int(input())
M = int(input())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))  # u → v로 가는 비용이 cost

# 시작 도시, 도착 도시
start, end = map(int, input().split())

# 최단 거리 저장 배열 (무한대로 초기화)
INF = float('inf')
distance = [INF] * (N + 1)

def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        dist, now = heapq.heappop(heap)
        
        if dist>distance[now]:
            continue

        for neighbor, cost in graph[now]:
            totalCost = cost + dist
            if totalCost<distance[neighbor]:
                distance[neighbor]=totalCost
                heapq.heappush(heap,(totalCost,neighbor))

dijkstra(start)

# 결과 출력
print(distance[end])
