import sys
input = sys.stdin.readline

N, K = map(int,input().split())
numebrs = list(range(1,N+1))
result = []
idx = 0
while numebrs:
    idx = (idx+K-1)%len(numebrs)
    result.append(numebrs.pop(idx))


print("<"+", ".join(map(str,result))+">")