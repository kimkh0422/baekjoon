# 숫자를 입력받아, 자릿수 기준 내림차순 정렬된 수로 출력하세요.
# 예: 입력: 2143 → 출력: 4321

number = input("원하는 숫자를 입력하세요: ")

numbers=list(map(int,number))
numbers.sort(reverse=True)

newNumbers = int(''.join(map(str,numbers)))
print(newNumbers)

