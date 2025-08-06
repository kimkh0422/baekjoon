import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    words = []

    for _ in range(n):
        word = input().strip()
        words.append(word)
    words.sort(key= lambda x: x.lower())
    print(words[0])