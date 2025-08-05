N = int(input())

result = N * 100  
papers = []


for _ in range(N):
    x, y = map(int, input().split())
    papers.append((x, y))


for i in range(N):
    x1, y1 = papers[i]
    for j in range(i + 1, N):
        x2, y2 = papers[j]

        
        xLen = max(0, min(x1 + 10, x2 + 10) - max(x1, x2))
        yLen = max(0, min(y1 + 10, y2 + 10) - max(y1, y2))

        area_len = xLen * yLen
        result -= area_len

print(result)
