import sys
input = sys.stdin.readline

members = []

count = int(input())

for i in range(count):
    str_age, name = input().split()
    age = int(str_age)
    
    members.append((age,name))

sorted_members = sorted(members, key= lambda x: x[0])

for age, name in sorted_members:
    print(age,name)