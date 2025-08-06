import sys
from collections import Counter

input = sys.stdin.readline  # input 재정의 (속도 개선)

count = int(input())
numbers = [int(input()) for _ in range(count)]

numbers.sort()

# 산술평균
avg = round(sum(numbers) / count)

# 중앙값
median = numbers[count // 2]

# 최빈값
counter = Counter(numbers)
freq = counter.most_common()
max_freq = freq[0][1]
modes = [num for num, cnt in freq if cnt == max_freq]
modes.sort()
mode_val = modes[1] if len(modes) > 1 else modes[0]

# 범위
range_val = numbers[-1] - numbers[0]

# 출력
print(avg)
print(median)
print(mode_val)
print(range_val)
