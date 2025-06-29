import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = map(int,input().split())

visited = set()


def backtrack(path,start):
    if len(path) == M:
        print(' '.join(map(str,path)))
        return
    
    for i in range(start,N+1):
        if i not in visited:
            path.append(i)
            visited.add(i)
            backtrack(path,i+1)

            visited.remove(i)
            path.pop()


backtrack([],1)

