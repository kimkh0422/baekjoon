count = int(input())
people = {}

for i in range(count):
    name, exist = input().split()
    people[name] = exist

sorted_people = sorted(people.items(), key= lambda x: (x[1]=='enter',-x[0]))

print(sorted_people)