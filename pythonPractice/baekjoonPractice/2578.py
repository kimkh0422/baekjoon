import sys
input = sys.stdin.readline

csBingo = [list(map(int, input().split())) for _ in range(5)]  # 철수 빙고판
Bingo = [[False] * 5 for _ in range(5)]  # 사회자가 부른 숫자 체크

numbers = [list(map(int, input().split())) for _ in range(5)]  # 사회자가 부른 숫자


def Bingo_Check_row():  # 가로 빙고 체크
    count = 0
    for i in range(5):
        if all(Bingo[i]):
            count += 1
    return count


def Bingo_Check_column():  # 세로 빙고 체크
    count = 0
    for j in range(5):
        if all(Bingo[i][j] for i in range(5)):
            count += 1
    return count


def Bingo_Check_cross():  # 대각선 빙고 체크
    count = 0
    if all(Bingo[i][i] for i in range(5)):
        count += 1
    if all(Bingo[i][4 - i] for i in range(5)):
        count += 1
    return count


callCount = 0
found = False

for x in range(5):
    for y in range(5):
        number = numbers[x][y]
        callCount += 1

        # 철수 빙고판에서 숫자 위치 찾아서 True로 표시
        for i in range(5):
            for j in range(5):
                if csBingo[i][j] == number:
                    Bingo[i][j] = True

        # 빙고 개수 확인
        totalBingo = Bingo_Check_row() + Bingo_Check_column() + Bingo_Check_cross()

        if totalBingo >= 3:
            print(callCount)
            found = True
            break
    if found:
        break
