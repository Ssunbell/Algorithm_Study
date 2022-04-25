# dp[n][i] 는 자릿수가 n개일때, i로 끝나는 계단수의 갯수
# dp[n][i] = dp[n-1][i-1] + dp[n-1][i+1]
# why : n=4, i=2라고하면,
# xxx2 라는 숫자가 되게 된다. xxx2 가 계단수가되려면 xx32 or xx12
# xx3 이 계단수가되려면 dp[n][i] = dp[n-1][i-1] + dp[n-1][i+1] 이 식을 똑같이 적용
# i가 0이면 dp[n][i] = dp[n-1][i+1], xx0의 계단수는 x10밖에없음
# i가 9면 dp[n][i] = dp[n-1][i-1], xx9의 계단수는 x89밖에 없음

n = int(input())
dp = [[0 for _ in range(11)] for _ in range(101)]

for i in range(1,10):
        dp[1][i] = 1

if n >= 2:
    for i in range(2,n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1] % 1000000000
            elif j == 9:
                dp[i][j] = dp[i-1][j-1] % 1000000000
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

print(sum(dp[n])% 1000000000)