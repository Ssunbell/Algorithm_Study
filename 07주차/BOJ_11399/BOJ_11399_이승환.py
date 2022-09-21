import sys

n = int(input())
atm = list(map(int,sys.stdin.readline().split()))

dp = [0 for _ in range(n)]

atm_sorted = sorted(atm)
for i in range(n):
    cust = atm_sorted[i]
    if i < 1:
        dp[i] = cust
    else:
        dp[i] = dp[i-1] + cust

print(sum(dp))
