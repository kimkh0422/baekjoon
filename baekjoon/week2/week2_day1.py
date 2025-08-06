#사용자로부터 단어 5개를 입력받아,
#길이가 4 이상인 단어만 필터링해서 출력하세요.
words = []

for i in range(5):
    word = input()
    if len(word) >= 4:
        words.append(word)
        
print(words)