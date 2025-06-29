import sys
input = sys.stdin.readline

n = int(input())
nSet = set(map(int, input().split()))


m = int(input())
mList = list(map(int,input().split()))

numbers = []

for number in mList:
    if number in nSet:
        numbers.append("1")
    else:
        numbers.append("0")

print(*numbers)