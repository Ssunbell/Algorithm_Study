import sys
input = sys.stdin.readline

n = int(input())

temp = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    min_value = min(temp)
    dp[i] = min_value * (n + 1 - i)
    temp.remove(min_value)
print(sum(dp))