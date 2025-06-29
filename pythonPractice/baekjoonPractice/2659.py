import sys
input = sys.stdin.readline

def get_clock_number(numberList):
    min_clock = float('inf')
    for idx in range(4):
        rotate = []
        for i in range(4):
            rotateIdx = (idx + i) % 4
            rotate.append(numberList[rotateIdx])
        rotateNumber = int(''.join(rotate))
        min_clock = min(min_clock, rotateNumber)
    return min_clock

# 입력
numberList = input().split()
target = get_clock_number(numberList)

# 시계수 후보를 찾고 순서 세기
visited = set()
count = 0

for num in range(1111, 10000):
    str_num = list(str(num))

    if '0' in str_num:
        continue

    clock = get_clock_number(str_num)
    if clock not in visited:
        visited.add(clock)
        count += 1

    if clock == target:
        print(count)
        break
