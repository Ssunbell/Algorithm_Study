x = int(input())


dp = [0 for _ in range(x+1)]

for i in range(2,x+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[int(i/3)],dp[int(i/2)],dp[i-1]) + 1
    elif i % 3 == 0 and i % 2 != 0:
        dp[i] = min(dp[int(i/3)],dp[i-1]) + 1
    elif i % 3 != 0 and i % 2 == 0:
        dp[i] = min(dp[int(i/2)],dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[x])