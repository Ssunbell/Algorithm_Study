n = int(input())
wines = [int(input()) for i in range(n)]

dp = []
dp.append(wines[0])
if n > 1:
    dp.append(wines[0] + wines[1])
for i in range(2, n):
    if i == 2:
        dp.append(max(dp[i-1], dp[i-2] + wines[i],
                      wines[i-1] + wines[i]))
    else:
        dp.append(max(dp[i-1], dp[i-2] + wines[i],
                      dp[i-3] + wines[i-1] + wines[i]))
print(dp[n-1])
