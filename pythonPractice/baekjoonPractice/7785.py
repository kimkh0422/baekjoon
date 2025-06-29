import sys
input = sys.stdin.readline

n = int(input())
people = dict()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        people[name] = True
    else:
        if name in people:
            del people[name]

sorted_people = sorted(people.keys(), reverse=True)

for person in sorted_people:
    print(person)
