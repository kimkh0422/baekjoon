word = input().upper()
wordDict = {}
count = 0
result = ''

for char in word:
    if char in wordDict:
        wordDict[char] += 1
    else:
        wordDict[char] = 1
        
maxCount = max(wordDict.values()) 

for key in wordDict:
    if wordDict[key] == maxCount:
        count +=1
        result = key
        
if count >1:
    print('?')
else:
    print(result) 
