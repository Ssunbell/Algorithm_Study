#[스티커]
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr = [tmp for tmp in zip(arr1, arr2)]
    
    dp = [[0, 0] for _ in range(N)]
    dp[0] = (arr[0][0], arr[0][1])
    if N > 1:
        dp[1] = (arr[1][0]+arr[0][1], arr[1][1]+arr[0][0])
    for i in range(2, N):
        dp[i][0] = arr[i][0] + max(dp[i-1][1], max(dp[i-2]))
        dp[i][1] = arr[i][1] + max(dp[i-1][0], max(dp[i-2]))
    print(max(dp[N-1]))