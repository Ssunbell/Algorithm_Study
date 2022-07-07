n = int(input())

dp = [0] * 100000

dp[0] = 3
dp[1] = 7

for i in range(2,n):
    dp[i] = (2*dp[i-1] + dp[i-2]) % 9901

print(dp[n-1])

