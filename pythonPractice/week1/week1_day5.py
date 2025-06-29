number = input("공백으로 숫자 여러개를 입력하세요:  ")
result = []

# split()으로 공백 기준 나누기
lists = list(map(int, number.split()))

# 짝수만 골라서 result에 담기
for word in lists:
    if word % 2 == 0:
        result.append(word)

# 오름차순 정렬
result.sort()

print(result)
