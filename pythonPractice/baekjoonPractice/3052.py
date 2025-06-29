nList = []

for i in range(10):
    n = int(input())
    insertN = n%42
    nList.append(insertN)
    
    
nSet = set(nList)

totalList = list(nSet)

count = len(totalList)  
print(count)