n = int(input())
l = list(map(int,input().split()))[::-1]
dp = [0] * (n)
order = 1

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if l[j] > l[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            order = max(order, dp[i])
print(order)
        
        
###############################
# 리스트     10 20  20  10  30  10
## order : 이전 숫자를 가지고 부분 수열을 만들 경우의 순서
# order     1   2   2   1   3   1 
# dp : 이전 숫자를 가지고 부분 수열을 만들 경우 가장 많은 부분 수열의 인덱스
# dp     0  0   1   1   0   2   0