import sys
input = sys.stdin.readline

n = int(input())
H = list(map(int, input().split()))  #처음 나무 높이
A = list(map(int, input().split()))  #나무가 자라는 속도
total = 0
trees = []

for i in range(n):
    trees.append((A[i],H[i]))

trees.sort(key= lambda x: x[0])

for day in range(n):
    a, h = trees[day]
    total += h + (a*day)

print(total)

