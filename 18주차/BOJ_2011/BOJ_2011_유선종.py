p = input()

dp = [0] * (len(p) + 1)
dp[0], dp[1] = 1, 1

if p[0] == '0':
    print(0)
else:
    for i in range(2, len(p)+1):
        if p[i-1] != '0':
            dp[i] += dp[i - 1]
        if p[i-2] == '1':
            dp[i] += dp[i - 2]
        elif p[i-2] == '2' and int(p[i-1]) <= 6:
            dp[i] += dp[i - 2]
    print(dp[-1] % 1000000)
'''
dp[3] 2,5,1/ 25, 1
dp[4] 2,5,1,1 / 25,1,1 / 2,5,11 / 25,11
dp[4] 2,5,1,1 / 25,1,1 / 2,5,11 / 25,11 + (4) 2,5,1/ 25, 1 + (4)
'''