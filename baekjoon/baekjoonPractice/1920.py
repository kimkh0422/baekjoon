import sys
input = sys.stdin.readline



n = int(input())
nList = list(map(int,input().split()))
nSet = set(nList)

m = int(input())
mList = list(map(int,input().split()))


for number in mList:
    if number in nSet:
        print("1")
    else:
        print("0")