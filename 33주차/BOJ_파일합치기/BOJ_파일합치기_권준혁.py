import sys
input = sys.stdin.readline
from itertools import accumulate

t = int(input())
for _ in range(t):
    l = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * l for _ in range(l)]
    acc = [0] + list(accumulate(arr))
    for k in range(1, l):
        for i in range(l - k):
            dp[i][i + k] = min(dp[i][j] + dp[j + 1][i + k] for j in range(i, i + k)) + acc[i + k + 1] - acc[i]
    print(dp[0][l - 1])