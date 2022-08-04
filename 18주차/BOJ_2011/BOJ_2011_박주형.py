import sys
input = lambda : sys.stdin.readline().rstrip()

n = list(map(int,input()))
l = len(n)
dp = [0 for _ in range(l+1)]
if (n[0] == 0) :
    print("0")
else :
    n = [0] + n
    dp[0]=dp[1]=1
    for i in range(2, l+1):
        print(n)
        if n[i] > 0:
            dp[i] += dp[i-1]
            print(dp)
        comb = n[i-1] * 10 + n[i]
        print(comb)
        if comb >= 10 and comb <= 26 :
            dp[i] += dp[i-2]
            print(dp)
    print(dp[l] % 1000000)

# [2] => 1개
# [2,5] => (2,5) (25) 2개
# [2,5,1] => (2,5,1) (25, 1) 2개
# [2,5,1,1] => (2,5,1,1) (2,5,11) (25,1,1) (25,11) 4개
# [2,5,1,1,4] => 6개