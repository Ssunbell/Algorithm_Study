first = list(input())
second = list(input())

dp = [[0] * (len(second)+1) for _ in range(len(first)+1)] # [[열] 행]

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i - 1] == second[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])


# for i in range(len(first)): # 행
#     for j in range(len(second)): # 열
#         if first[i] == second[j]:
#             dp[i][j] = first[i]

# result = []
# for start in range(len(first)):
#     result1 = ''
#     cnt = 0
#     for i in range(start, len(first)):
#         for j in range(cnt, len(second)):
#             if dp[i][j] != 0:
#                 cnt = j 
#                 result1 += dp[i][j]
#                 break
#     result.append(len(result1))

# dp_rev = [col for col in zip(*dp)]
# for start in range(len(second)):
#     result2 = ''
#     cnt = 0
#     for i in range(start, len(second)):
#         for j in range(cnt, len(first)):
#             if dp_rev[i][j] != 0:
#                 cnt = j
#                 result2 += dp_rev[i][j]
#                 break
#     result.append(len(result2))

# print(max(result))