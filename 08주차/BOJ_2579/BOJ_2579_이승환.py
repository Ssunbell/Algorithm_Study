# dp[i]는 i번째 계단을 마지막으로 생각할 때 점수의 최대값
# dp[i]일때는 무조건 i번째 계단을 밟게됨
# i를 밟으려면 i-1 or i-2 둘 중 하나는 무조건 밟아야함
# i-1을 밟으면 i-2를 밟지 않고 무조건 i-3을 밟음
# i-2를 밟으면 무조건 i-1을 안밟음
# i-2를 무조건 밟으면 i-3을 밟는지 안밟는지는 i입장에서는 전혀 신경쓸 일이 아님
# i입장에서는 i-2를 밟는지 i-1을 밟는지만 신경쓰면 됨
# dp[i] = dp[i-3] + s[i-1] + s[i]
# dp[i] = dp[i-2] + s[i]

n = int(input())
s = [0]*(n+3)
for i in range(n):
    s[i+1] = int(input())

dp = [0 for _ in range(n+3)]

dp[1] = s[1]
dp[2] = s[1] + s[2]
dp[3] = max(s[1]+s[3], s[2]+s[3])

for i in range(3,n+1):
    dp[i] = max(dp[i-2], dp[i-3]+s[i-1]) + s[i]

print(dp[n])