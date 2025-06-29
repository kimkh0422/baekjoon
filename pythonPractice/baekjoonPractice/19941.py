import sys
input = sys.stdin.readline

N, K = map(int,input().split())

visited = [False]*(N)

graph = list(input().strip())


count = 0
for i in range(N):
    if graph[i]=='P':
        for j in range(i-K,i+K+1):
            if 0<=j<N and graph[j]=='H' and visited[j]==False:
                visited[j]=True
                count+=1
                break

print(count)
