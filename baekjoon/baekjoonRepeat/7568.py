import sys
input = sys.stdin.readline

N = int(input())

people = []

for _ in range(N):
    x, y = map(int,input().split())
    people.append((x,y))


for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        a, b = people[i]
        c, d = people[j]
        if a < c and b < d:
            rank += 1
    print(rank, end=' ')

