n = int(input())

result = 0

dp = [0] * (n+1)

for i in range(1,n+1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 2
    else:
        dp[i] = (dp[i-1]%15746) + (dp[i-2]%15746)

print(dp[n]%15746)