import sys

count = int(sys.stdin.readline())
numbers = [0]*10001

for _ in range(count):
    number = int(sys.stdin.readline())
    numbers[number] += 1
    
for i in range(1,10001):
    for _ in range(numbers[i]):
        print(i)