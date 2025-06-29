import sys
# 1. 문제의 input을 받습니다.
N, A, B = map(int, sys.stdin.readline().split())
oneTile = list(map(int,sys.stdin.readline().split()))
twoTile = list(map(int,sys.stdin.readline().split()))

# 2. 각 타일을 크기가 큰 순서대로 정렬합니다.
oneTile.sort(reverse=True)
twoTile.sort(reverse=True)
total = 0
idx1 = 0
idx2 = 0

if N%2==1:
    total+=oneTile[0]
    oneTile.pop(0)

for _ in range(N//2):
    case1,case2 = 0,0

    if len(oneTile)>=2:
        case1 += oneTile[0]+oneTile[1]

    
    if len(twoTile)>=1:
        case2 += twoTile[0]

    if case1>case2:
        total+=case1
        oneTile.pop(0)
        oneTile.pop(0)
    else:
        total+=case2
        twoTile.pop(0)

print(total)
