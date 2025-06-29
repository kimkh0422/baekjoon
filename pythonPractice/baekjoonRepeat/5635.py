import sys
input = sys.stdin.readline

N = int(input())

result = []

for _ in range(N):
    name, dd, mm, yyyy = input().split()
    result.append((name,yyyy,mm,dd))

#나이가 적은 사람 출력이니 yyyy,mm,dd순으로 대소비교 해서 가장 큰걸 처음 출력 즉 오름차순 정렬했을때 가장 뒤에 오는 사람 이름이 나이가 적은 사람
result.sort(key= lambda x: (x[1],x[2],x[3]))

print(result[-1][0])
print(result[0][0])

