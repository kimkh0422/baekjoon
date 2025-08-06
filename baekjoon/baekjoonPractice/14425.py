n, m = map(int, input().split())
nSet = set()

count = 0

for i in range(n):
    nWord = input()
    nSet.add(nWord)
    
for j in range(m):
    word = input()
    if word in nSet:
        count+=1
        
print(count)