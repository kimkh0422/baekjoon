import sys
input = sys.stdin.readline


dp = [(1,0),(0,1)]+[(0,0)]*39

for i in range(2,41):
    zero = dp[i-1][0] + dp[i-2][0]
    one = dp[i-1][1] + dp[i-2][1]
    dp[i] = (zero,one)


T = int(input())
for _ in range(T):
    N = (int(input()))
    print(dp[N][0], dp[N][1])