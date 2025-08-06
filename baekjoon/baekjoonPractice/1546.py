N = int(input())

result = list(map(int,input().split()))
maxScore = max(result)
total = 0

for score in result:
    newScore = score/maxScore*100
    total+=newScore

print(total/N)