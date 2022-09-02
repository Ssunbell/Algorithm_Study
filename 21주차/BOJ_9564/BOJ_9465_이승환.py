import sys

input_s = lambda : sys.stdin.readline().strip()

t = int(input_s())

for _ in range(t):
    n = int(input_s())
    stickers = []
    stickers.append(list(map(int,input_s().split())))
    stickers.append(list(map(int,input_s().split())))
    
    dp = [[0]*(n+1),[0]*(n+1)]
    dp[0][1] = stickers[0][0]
    dp[1][1] = stickers[1][0]

    for i in range(2,n+1):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i-1]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i-1]

    print(max(max(dp[0]),max(dp[1])))