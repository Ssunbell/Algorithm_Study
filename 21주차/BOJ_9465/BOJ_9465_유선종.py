import sys

input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n,[0]*n]
    
    # 0번째
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    
    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1] + sticker[0][i], dp[1][i-2] + sticker[0][i])
        dp[1][i] = max(dp[0][i-1] + sticker[1][i], dp[0][i-2] + sticker[1][i])
    print(max(dp[0][n-1], dp[1][n-1]))
    
    


'''
A C E G
B D F H

E로 가는 경우의 수
1) A -> D -> E (n-1번째 아래)
2) B -> E (n-2번째 아래)

G로 가는 경우의 수
1) A -> D -> G (n-2번째 아래)
2) B -> C -> F -> G (n-1번째 아래)
'''

# for _ in range(t):
#     n = int(input())
#     sticker = [list(map(int, input().split())) for _ in range(k)]
#     answer = 0
    
#     while sum([sum(row) for row in sticker]) != 0:
#         tmp_sticker = sorted([(i, max(row)) for i, row in enumerate(sticker)], key=lambda x: (-x[1], -x[0]))
#         row_sticker, max_sticker = tmp_sticker[0][0], tmp_sticker[0][1]
#         col_sticker = sticker[row_sticker].index(max_sticker)
#         answer += max_sticker
        
#         dx = [0, 0, -1, 0, 1]
#         dy = [0, 1, 0, -1, 0]
#         for i in range(5):
#             try:
#                 sticker[row_sticker-dx[i]][col_sticker-dy[i]] = 0
#             except:
#                 pass
#     print(answer)