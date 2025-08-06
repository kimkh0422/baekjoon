n = int(input())
people = set()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        people.add(name)
    else:  # leave
        people.discard(name)  # 안전하게 제거

# 이름을 내림차순 정렬 후 출력
for name in sorted(people, reverse=True):
    print(name)
