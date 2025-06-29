import sys
input = sys.stdin.readline

N, K = map(int,input().split())
people = list(map(int,input().split()))
people.sort()  # 꼭 정렬 필요!

peopleDiff = []
for i in range(N - 1):
    peopleDiff.append(people[i + 1] - people[i])

peopleDiff.sort(reverse=True)

# 가장 큰 K-1개를 제거 (한 번만)
peopleDiff = peopleDiff[K - 1:]

print(sum(peopleDiff))
