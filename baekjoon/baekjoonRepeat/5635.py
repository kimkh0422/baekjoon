import sys
input = sys.stdin.readline

N = int(input())

result = []

for _ in range(N):
    name, dd, mm, yyyy = input().split()
    result.append((name, int(yyyy), int(mm), int(dd)))

# 나이가 적은 사람은 생일이 가장 늦은 사람
result.sort(key=lambda x: (x[1], x[2], x[3]))  # 생년월일 오름차순

print(result[-1][0])  
print(result[0][0])   
