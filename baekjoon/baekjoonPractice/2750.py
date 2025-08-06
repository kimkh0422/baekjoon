count = int(input())
numbers = []

for i in range(count):
    number = int(input())
    numbers.append(number)
    
numbers.sort()

for number  in numbers:
    print(number)