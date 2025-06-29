import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = map(int,input().split())

visited = set()


def backtrack(path):
    if len(path) == M:
        print(' '.join(map(str,path)))
        return
    
    for i in range(1,N+1):
        if i not in visited:
            path.append(i)
            visited.add(i)
            backtrack(path)

            visited.remove(i)
            path.pop()


backtrack([])

