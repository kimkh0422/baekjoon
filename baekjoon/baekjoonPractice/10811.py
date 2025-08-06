import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bagune = [i for i in range(1, N + 1)]  

for _ in range(M):
    i, j = map(int, input().split())
    bagune[i-1:j] = reversed(bagune[i-1:j])  

print(' '.join(map(str,bagune))) 
