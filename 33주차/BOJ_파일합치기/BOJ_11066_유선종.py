import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    k = int(input())
    pages = list(map(int, input().split()))
    dp = [[0 for _ in range(k)] for _ in range(k)]
    for x in range(1,k):
        # x는 보고싶은 파일의 길이 (예 : 3개 -> [1, 21, 3])
        for i in range(k-x):
            dp[i][i+x] = 99999999999
            
            ## 파일의 길이만큼 누적합
            cumul = sum(pages[i:i+x+1])
            for k in range(i,i+x):
                dp[i][i+x] = min(dp[i][i+x],dp[i][k]+dp[k+1][i+x]+cumul)
    print(dp[0][k-1])
'''
1
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

# dp[i][k] + dp[k+1][i+x] + tmp의 해석
비교할 대상은 3개의 원소 양 끝
[1, 21, 3] -> [22, 3, 4]
            -> [1, 24, 4]
x == 1,
[0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 103, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 119, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49]

x == 2,
[0, 22, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 24, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 7, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 9, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 40, 85, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 40, 53, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 9, 19, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 7, 19, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 114, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 103, 227, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 119, 168, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49]

x == 3,
[0, 22, 47, 58, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 24, 35, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 7, 19, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 9, 53, 98, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 40, 85, 98, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 40, 53, 66, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 9, 19, 34, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 7, 19, 129, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 114, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 103, 227, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 119, 168, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49]
'''
# t = int(input())
# for _ in range(t):
#     k = int(input())
#     arr = list(map(int, input().split()))
#     p = arr.index(min(arr))
#     answer = 0
#     while True:
#         try:
#             if p > 0 and arr[p-1] < arr[p+1]:
#                 tmp = arr.pop(p-1)
#                 p -= 1
#                 arr[p] += tmp
#                 answer += arr[p]
#             elif arr[p] < arr[p+1] + arr[p+2]:
#                 arr[p] += arr.pop(p+1)
#                 answer += arr[p]
#             elif len(arr) == 3:
#                 arr = sorted(arr)
#                 answer += sum(arr[:2]) * 2 + arr[-1]
#                 break
#             else:
#                 p = arr.index(min(arr))
#             print(arr)
#         except:
#             p = 0
#             continue
#     print(answer)