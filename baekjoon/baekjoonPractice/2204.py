while True:
    n = int(input())
    if n == 0:
        break

    words = []
    for _ in range(n):
        word = input()
        words.append(word)

    words.sort(key=lambda x: x.lower())  # 대소문자 구분 없이 정렬
    print(words[0])
