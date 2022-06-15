import sys

input = lambda: sys.stdin.readline()
n = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 메모리 초과 방지
print(dp[n])

"""
1 -1
00 11 -2
100 001 111 -3
0011 0000 1001 1100 1111 -5
10000 00100 00001 00111 10011 11001 11100 11111 - 8

n-1 : 1을 하나씩 더하기
n-2 : 00을 하나씩 더하기
"""