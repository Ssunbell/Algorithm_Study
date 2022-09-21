import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())
case = [int(input()) for _ in range(t)]
for n in case:
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 0 + 1
    dp[3] = 0 + 1
    dp[4] = 1 + 1
    dp[5] = 0 + 2
    dp[6] = 1 + 2
    for i in range(7, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])

'''
1   2   3   4   5   6   7   8   9   10   11  12  13
1   1   1    2   2   3   4   5   7   9  12  16    21
1  0/1 0/1 1/1 0/2 1/2 1/3 1/4 2/5 2/7 3/9 4/12  5/16
'''