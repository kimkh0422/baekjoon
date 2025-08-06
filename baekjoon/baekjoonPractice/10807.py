n = int(input())
List = input().split()
v = int(input())
count = 0

nList = list(map(int,List))

for i in nList:
    if i == v:
        count+=1
        
print(count)