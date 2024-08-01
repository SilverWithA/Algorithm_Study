import sys

n = int(sys.stdin.readline())

dp = [None] * 11
dp[0], dp[1], dp[2] = 1,1,2

for _ in range(n):
    a = int(sys.stdin.readline())
    for i in range(3, a+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[a])