import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

dp = [0] * 1000000
dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n-1])