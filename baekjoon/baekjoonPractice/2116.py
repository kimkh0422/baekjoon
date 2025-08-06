import sys
input = sys.stdin.readline

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

#마주보는 면 인덱스 정의하기
opposite = {0:5,1:3,2:4,3:1,4:2,5:0}

result = []

for i in range(6):  # 첫 주사위 바닥면 인덱스 경우가 0~5인 경우 모두를 비교하기 위해 
    bottom = dice[0][i]   #첫 주사위 바닥 
    top = dice[0][opposite[i]] #첫 주사위 탑

    total = 0
    for d in dice:
        # 현재 주사위에서 bottom의 인덱스를 찾아서 윗면 인덱스를 구함
        for j in range(6):
            if d[j] == bottom:   #현재 bottom값일때
                b_idx = j      #그 bottom의 인덱스 값
                t_idx = opposite[j]   #마주보는거 이용해서 top의 인덱스값
                break
        bottom = d[t_idx]  # 다음 주사위에서의 바닥면에 현재 나온 d[t_idx]값
        side_max = max([d[k] for k in range(6) if k != b_idx and k != t_idx]) #사이드값중 가장 큰 값을 구하는데 top이랑 bottom에 가는건 제외 
        total += side_max  # 🔁 여기서 total을 누적

    result.append(total)  # 🔁 주사위 바닥면 인덱스0~5인 경우 모두 저장

print(max(result))        #그중 가장 큰 경우 출력


