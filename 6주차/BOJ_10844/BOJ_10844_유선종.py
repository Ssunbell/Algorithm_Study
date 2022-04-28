n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)


'''
자리수: 1   2   3
      0   0   0
      1   1   1
      2   2   2
      3   3   3
      4   4   4
      5   5   5
      6   6   6
      7   7   7
      8   8   8
      9   9   9
'''