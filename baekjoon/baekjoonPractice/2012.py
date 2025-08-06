import sys
input = sys.stdin.readline

N = int(input())

people = []
people.append(0)

for _ in range(N):
    hopeGrade = int(input())
    people.append(hopeGrade)

people.sort()

total = 0
for i in range(N+1):
    total += abs(people[i]-i)


print(total)
