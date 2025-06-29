
n = int(input())
numbers = list(map(int,input().split()))

maxNumber = max(numbers)
minNumber = min(numbers)

print(f"{minNumber} {maxNumber}")