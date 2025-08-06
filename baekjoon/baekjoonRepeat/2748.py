import sys
input = sys.stdin.readline

n = int(input())
result = [0] * (n + 1)

def fib(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    if result[N] != 0:
        return result[N]
    
    result[N] = fib(N - 1) + fib(N - 2)
    return result[N]

print(fib(n))
