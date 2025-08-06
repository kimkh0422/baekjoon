woods = list(map(int, input().split()))

while woods != [1, 2, 3, 4, 5]:
    for i in range(4):  
        if woods[i] > woods[i + 1]:
            woods[i], woods[i + 1] = woods[i + 1], woods[i]
            print(" ".join(map(str, woods)))
