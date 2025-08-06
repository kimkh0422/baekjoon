
N = int(input())

dp = [0]*(N+1)

def fib(N):
    if N == 1:
        return 1
    if N == 2:
        return 1
    
    if dp[N]!=0:
        return dp[N]
    
    dp[N] = fib(N-1)+fib(N-2)
    return dp[N]

print(fib(N))
