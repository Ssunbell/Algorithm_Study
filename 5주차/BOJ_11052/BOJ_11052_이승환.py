n = int(input())
p = list(map(int,input().split()))

p = [0] + p

dp = [0 for i in range(len(p))]

dp[1] = p[1]
for i in range(2,len(p)):
    set_n = []
    for j in range(1,i+1):
        set_n.append(dp[i-j]+dp[j])
    dp[i] = max(max(set_n),p[i])

print(max(dp))