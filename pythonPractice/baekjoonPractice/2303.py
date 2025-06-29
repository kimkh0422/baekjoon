import sys
input = sys.stdin.readline

N = int(input())
index = -1  # 지금까지의 최고 1의 자리 수
winner = 0  # 현재 승자 번호

for i in range(N):
    numbers = list(map(int, input().split()))
    onevalue = -1  # 이 참가자의 최대 1의 자리 수

    for a in range(5):
        for b in range(a + 1, 5):
            for c in range(b + 1, 5):
                total = numbers[a] + numbers[b] + numbers[c]
                totalOneValue = total % 10

                if totalOneValue > onevalue:
                    onevalue = totalOneValue #각 참가자 최고점수가 onevalue에 들어감

    if onevalue >= index:
        index = onevalue
        winner = i + 1  # 가장 마지막 번호로 갱신

print(winner)
