n = int(input())

a = list(map(int,input().split()))
a.append(0)

dp = [0] * (n+1)

for i in range(n-1,-1,-1):
    k = []
    for j in range(n,i,-1):
        if a[i] > a[j]:
            k.append(dp[j])
    dp[i] = max(k) + 1

print(max(dp))