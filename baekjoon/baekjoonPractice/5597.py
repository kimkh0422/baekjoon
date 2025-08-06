
people = [False]*30

for _ in range(28):
    n = int(input())
    people[n-1] = True
    
for idx in range(30):
    if people[idx]==False:
        print(idx+1)