import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Trees = list(map(int, input().split()))

start = 0
end = max(Trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in Trees:
        if tree > mid:
            total += tree - mid

    if total >= M:
        result = mid  # 현재 높이는 가능하므로 저장하고, 더 높은 쪽 탐색
        start = mid + 1
    else:
        end = mid - 1

print(result)
