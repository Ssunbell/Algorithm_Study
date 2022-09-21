n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
#print(w)

dp = [0]
dp.append(w[1])
#print(dp)

if n > 1:
    dp.append(w[1] + w[2])
    #print(dp,'ㅇㄹ')

for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i])) # 4번째 부터의 dp의 규칙성
    #print(dp)
print(dp[n])
