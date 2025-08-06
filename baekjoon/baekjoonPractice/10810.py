n,m = map(int,input().split())

ballList = [0]*n

for _ in range(m):
    i,j,k = map(int,input().split())
    for idx in range(i,j+1):
        ballList[idx-1] = k

print(' '.join(map(str,ballList)))