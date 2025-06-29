N = int(input())

dp = [0]*(N+1)

def fib(i):
    if i==1:
        return 1
    if i ==2:
        return 1
    if dp[i]!=0:
        return dp[i]
    dp[i] = fib(i-1)+ fib(i-2)
    return dp[i]

print(fib(N))