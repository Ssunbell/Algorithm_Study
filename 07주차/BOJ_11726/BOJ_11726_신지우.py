# n = 1 2x1 -> 1
# n = 2 2x2 -> 2
# n = 3 2x3 -> 3
# n = 4 2x4 -> 5
# n = 5 2x5 -> 8
# n = 6 2x6 -> 13
# ...

n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n]%10007)