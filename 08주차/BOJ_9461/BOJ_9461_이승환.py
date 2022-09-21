test_case = int(input())

for t in range(test_case):
    n = int(input())
    dp = [0 for i in range(n)]
    for i in range(n):
        if i == 0 or i == 1 or i == 2:
            dp[i] = 1
        elif i == 3 or i == 4:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-5]
    print(dp[n-1])