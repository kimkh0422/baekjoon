count = int(input())

for i in range(count):
    repeat, word = input().split()
    repeat = int(repeat)
    result = ""
    for char in word:
        result += char*repeat
        
    print(result)