import sys
input = sys.stdin.readline

N,K = map(int,input().split())
people = []
visited = [False]*N

for _ in range(N):
    a = int(input())
    people.append(a)

count = 0
current = 0

while True:
    if visited[current]==False:
        visited[current]=True
        current=people[current]
        count+=1
    elif visited[current]==True:
        print(-1)
        break

    if current==K:
        print(count)
        break


