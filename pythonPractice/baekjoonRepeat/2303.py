import sys
input = sys.stdin.readline

n = int(input())

winner = 0
highNumber = 0

for person in range(1,n+1):
    maxNumber = 0
    numbers = list(map(int,input().split()))

    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                total = numbers[i]+numbers[j]+numbers[k]
                resultNumber = total%10
                maxNumber = max(maxNumber,resultNumber)
    
    if highNumber<=maxNumber:
        highNumber=maxNumber
        winner = person
print(winner)

