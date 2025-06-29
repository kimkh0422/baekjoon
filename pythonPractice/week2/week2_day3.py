N = int(input())
fruits = input().split()
fruits.sort()

target = input()

left = 0
right = len(fruits)-1
found = False

while left<=right:
    mid = (left+right)//2
    if target == fruits[mid]:
        found = True
        break  # 찾았으니 바로 종료
    elif target > fruits[mid]:
        left = mid +1
    else:
        right = mid -1

if found == True:
    print("존재합니다")
else:
    print("없습니다")
