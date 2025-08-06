from itertools import combinations
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
numbers = list(map(int,input().split()))

count=0
for i in range(1,N+1):
    for comb in combinations(numbers,i):
        if sum(comb)==S:
            count+=1

print(count)