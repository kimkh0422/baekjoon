import sys
input = sys.stdin.readline

R, C = map(int, input().split())
dadoSea = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

to_change = []  # 지워질 X 위치들 저장

# 먼저 바꿔야 할 좌표 저장
for i in range(R):
    for j in range(C):
        if dadoSea[i][j] == 'X':
            sea_count = 0
            for dir in range(4):
                nx = i + dx[dir]
                ny = j + dy[dir]
                if nx < 0 or ny < 0 or nx >= R or ny >= C or dadoSea[nx][ny] == '.':
                    sea_count += 1
            if sea_count >= 3:
                to_change.append((i, j))

# 한꺼번에 변경
for x, y in to_change:
    dadoSea[x][y] = '.'

# 최소/최대 범위 구해서 필요한 부분만 출력
min_row, max_row = R, 0
min_col, max_col = C, 0

for i in range(R):
    for j in range(C):
        if dadoSea[i][j] == 'X':
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)

# 혹시라도 전부 바다(.)인 경우 예외 처리
if min_row > max_row or min_col > max_col:
    print('x') 
else:
    for i in range(min_row, max_row + 1):
        print(''.join(dadoSea[i][min_col:max_col + 1]))
