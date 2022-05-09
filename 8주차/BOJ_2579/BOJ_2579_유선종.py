import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)] + [0,0]

dp = [0] * (n + 3)
dp[1] = stairs[1]
dp[2] = dp[1] + stairs[2]
dp[3] = max(stairs[2] + stairs[3], stairs[1] + stairs[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i] + stairs[i-1])
print(dp[n])

'''
10 20 15 25 10 20
O  O  X  O  O  X
_  O  _  O  O  X
O  _  O  O  X  O
O  _  O  _  O  O
O  O  X  _  O  O
_  O  O  X  O  O
_  O  _  O  _  O

20 10 25 15 20 10
O  O  X  O  O  X  O
O  O  X  _  O  O  X
O  O  X  _  O  _  O
O  _  O  O  X  O  _
O  _  O  O  X  _  O
O  _  O  _  O  _  O
O  _  O  _  O  O  X
'''
