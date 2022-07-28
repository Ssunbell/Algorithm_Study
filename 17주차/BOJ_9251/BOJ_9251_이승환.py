si = input()
sj = input()

dp = [[0]*(len(sj)+1) for _ in range((len(si)+1))]

for i in range(1,len(si)+1):
    for j in range(1,len(sj)+1):
        if si[i-1] == sj[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(max(dp)))
