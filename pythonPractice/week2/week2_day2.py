count = int(input("문자를 몇개 입력할지 적어주세요: "))
words = []

for i in range(count):
    name = input("이름을 입력해주세요: ")
    score = int(input("점수를 입력해주세요: "))
    
    words.append((name,score))


sorted_words = sorted(words,key=lambda x:(-x[1],x[0]))
print(sorted_words)
