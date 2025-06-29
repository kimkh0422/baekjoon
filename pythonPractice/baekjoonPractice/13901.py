import sys
input = sys.stdin.readline

R, C = map(int, input().split())
room = [['*' for _ in range(C)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    room[br][bc] = 'x'

sr, sc = map(int, input().split())
wayList = [d-1 for d in map(int, input().split())]

# ↑ ↓ ← →
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def robot(x, y):
    visited[x][y] = True

    dir_idx = 0  # 현재 방향 인덱스
    d = wayList[dir_idx]  # 시작 방향

    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != 'x' and not visited[nx][ny]:
            # 이동 가능
            visited[nx][ny] = True
            x, y = nx, ny
            # 방향 유지
        else:
            # 막혔으면 다음 방향 우선순위로 전환
            moved = False
            for i in range(1, 5):  # 최대 4방향까지 시도
                dir_idx = (dir_idx + 1) % 4
                d = wayList[dir_idx]
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != 'x' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    x, y = nx, ny
                    moved = True
                    break
            if not moved:
                print(x, y)
                return

robot(sr, sc)
