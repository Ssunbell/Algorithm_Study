import sys

input_s = input_s = lambda : sys.stdin.readline().strip()

n = int(input_s())
m = int(input_s())
bus = [list(map(int,input_s().split())) for _ in range(m)]

dp = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]

# 그래프 생성
for edge in bus:
    dp[edge[0]][edge[1]] = min(dp[edge[0]][edge[1]], edge[2])
    # dp[edge[1]][edge[0]] = min(dp[edge[1]][edge[0]], edge[2])

# 자기자신 초기화
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            dp[i][j] = 0
            dp[j][i] = 0

# 플로이드 워셜
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dp[i][j] == float("inf"):
            dp[i][j] = 0
        print(dp[i][j],end=" ")
    print()