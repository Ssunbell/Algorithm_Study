import sys

input_s = lambda : sys.stdin.readline().strip()

n, m = map(int,input_s().split())
relation = [list(map(int,input_s().split())) for _ in range(m)]

dp = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]
bacon = []
nodes = [[] for _ in range(n+1)]

# 그래프 생성
for edge in relation:
    dp[edge[0]][edge[1]] = 1
    dp[edge[1]][edge[0]] = 1

# 플로이드 워셜
for k in range(1,n+1):  # 1을 중간점으로 할 때
    for i in range(1,n+1):
        for j in range(1,n+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

# 케빈베이컨 계산
for path in dp:
    sum_path = 0
    for i in path:
        if i != float("inf"):
            sum_path += i
    bacon.append(sum_path)
bacon[0] = float("inf")

# 가장 작은 케빈 베이컨 값을 가지는 사람 구하기(인덱스 구하기)
min_bacon = list(filter(lambda x: bacon[x] == min(bacon), range(len(bacon))))

# 케빈 베이컨이 가장 작은 사람.
print(min(min_bacon))