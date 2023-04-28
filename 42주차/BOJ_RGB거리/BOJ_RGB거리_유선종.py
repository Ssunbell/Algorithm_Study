N = int(input())

dp = [[0] * 3 for _ in range(N+1)]
dp[1] = list(map(int, input().split()))
for i in range(2, N+1):
    row = list(map(int, input().split()))
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + row[0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + row[1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + row[2]
print(min(dp[N]))