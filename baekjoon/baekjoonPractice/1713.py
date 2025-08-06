import sys
input = sys.stdin.readline

N = int(input())  # 사진틀 개수
R = int(input())  # 총 추천 횟수
recommand = list(map(int, input().split()))

frame = {}  # key: 학생 번호, value: (추천수, 시간)
time = 0

for number in recommand:  #추천받은 학생의 번호
    if number in frame:
        vote,t = frame[number]
        frame[number] = (vote+1,t)

    else:
        if len(frame)<N:
            frame[number] = (1,time)
        else:
            deleteTarget = sorted(frame.items(),key=lambda x: (x[1][0],x[1][1]))[0][0]
            del frame[deleteTarget]
            frame[number] = (1,time)
    time+=1

print(' '.join(map(str,sorted(frame.keys()))))