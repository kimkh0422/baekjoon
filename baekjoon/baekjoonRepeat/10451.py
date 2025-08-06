import sys
input = sys.stdin.readline


T = int(input())

def dfs(node):
    visited[node]=True
    nextNode = numbers[node]

    if visited[nextNode]==False:
        dfs(nextNode)
        


for _ in range(T):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    count = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            count += 1
    print(count)
