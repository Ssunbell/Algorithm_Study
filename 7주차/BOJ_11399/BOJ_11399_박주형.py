n = int(input())
line = list(map(int, input().split()))
line.sort()
dp = [0] * n
for i in range(len(line)):
    if i == 0:
        dp[i] = line[i]
    else:
        dp[i] = dp[i-1] + line[i]

print(sum(dp))
