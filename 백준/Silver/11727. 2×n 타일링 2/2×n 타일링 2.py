import sys

n = int(sys.stdin.readline())

dp = [0] * 1001
dp[0], dp[1] = 1, 3
for i in range(2, n):
    dp[i] = (2 ** (i) + dp[i - 2]) % 10007

print(dp[n-1])