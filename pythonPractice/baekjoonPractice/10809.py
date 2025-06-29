word = input()
result = [-1 for i in range(26)]

for i in range(len(word)):
    idx = ord(word[i])-ord('a') # 각 word에 나오는 알파벳의 인덱스값 예를들어 a = 0, b = 1
    if result[idx] == -1:
        result[idx] = i
        
print(*result)