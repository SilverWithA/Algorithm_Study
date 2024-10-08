import sys

n = int(sys.stdin.readline())

dp = [0] * 1001
dp[0], dp[1] = 1, 2
for i in range(2, n):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n-1])