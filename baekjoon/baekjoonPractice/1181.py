import sys
input = sys.stdin.readline

words = []
count = int(input())

for _ in range(count):
    word = input().strip()
    words.append(word)


setWords = set(words)
newWords = list(setWords)


sorted_words = sorted(newWords, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
