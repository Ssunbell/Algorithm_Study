import sys
input = sys.stdin.readline
TestCase = int(input())

def getMaximumValue(n, arr):
  dp = [[j for j in i] + [0] for i in zip(*arr)]
  for i in range(1, n):
    dp[i][0] += max(dp[i-1][1], dp[i-1][2])
    dp[i][1] += max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = max(dp[i-1])
  return max(dp[n - 1])

for _ in range(TestCase):
  n = int(input())
  stickers = [list(map(int, input().split())) for _ in range(2)]
  print(getMaximumValue(n, stickers))