N,M = map(int,input().split())

bagune = [0]*N

for number in range(1,N+1):
    bagune[number-1] = number

for _ in range(M):
    i,j = map(int,input().split())
    bagune[i-1],bagune[j-1] =bagune[j-1],bagune[i-1]

print(' '.join(map(str,bagune)))