n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0, wine[0]]
if n > 1:
    dp = [0, wine[0], wine[0] + wine[1]]


for i in range(3, n + 1):
    case_1 = dp[i - 2] + wine[i - 1]
    case_2 = dp[i - 3] + wine[i - 1] + wine[i - 2]
    case_3 = dp[i - 1]
    max_value = max(case_1, case_2, case_3)
    
    dp.append(max_value)
print(dp[n])

# 1 : 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
# 2 : 이번 포도주를 먹고 이전 포도주도 먹은 경우
# 3 : 이번 포도주를 먹지 않아야 하는 경우