numbers = []

for i  in range(5):
    num = int(input(f"{i+1}번째 숫자를 입력하세요: "))
    numbers.append(num)

maxNum = max(numbers)
minNum = min(numbers)
sumNum = sum(numbers)
avgNum = sumNum/len(numbers)
avg = round(avgNum,1)

#최대 40, 최소 10, 평균 25.0
print(f"최대 {maxNum}, 최소{minNum}, 평균{avg}")