import sys
input = sys.stdin.readline

R,C = map(int,input().split())  #R 세로길이 즉 행 C는 가로길이 즉 열

city = [list(input().strip()) for _ in range(R)]

dx = [-1,0,1,0] 
dy = [0,-1,0,1]


for i in range(R):
    for j in range(C):
        if city[i][j]=='.':  #이제 상하좌우 탐색할차례임
            #상하좌우 탐색코드
            wall = 0
            for d in range(4):
                nx = j + dx[d]  
                ny = i + dy[d]

                if nx<0 or ny<0 or nx>=C or ny>=R or city[ny][nx] == 'X':
                    wall+=1
            if wall >= 3:
                print(1)
                sys.exit()

print(0)