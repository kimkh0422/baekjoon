count = int(input())
words = []

for i in range(count):
    name, str_a, str_b, str_c = input().split()
    a = int(str_a)
    b = int(str_b)
    c = int(str_c)
    words.append((name,a,b,c))

sorted_words = sorted(words,key=lambda x: (-x[1],x[2],-x[3],x[0]))

for name in sorted_words:
    print(name[0])