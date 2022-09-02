N = int(input())
dp = [1, 3] + [0] * N
MODVAL = 9901

for i in range(2, N + 1):
    dp[i] = (2 * dp[i - 1] + dp[i - 2]) % MODVAL
print(dp[N])
