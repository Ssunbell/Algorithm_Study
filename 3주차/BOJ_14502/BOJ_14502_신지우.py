# DP 문제
n = int(input()) 

day_list = []
pay_list = []
dp = []

for i in range(n): 
    day, pay = map(int, input().split()) 
    day_list.append(day) 
    pay_list.append(pay)
    dp.append(pay) 
    print(dp)
dp.append(0) 

for i in range(n-1, -1, -1): 
    if day_list[i] + i > n: 
        dp[i] = dp[i+1] 
    else: 
        print(dp[i+1]) 
        print(day_list[i],'ㅓㅈ에') 
        print(dp[i+day_list[i]],'wad') 
        print(pay_list[i]+dp[i+day_list[i]],'ws')
        dp[i] = max(dp[i+1], pay_list[i]+dp[i+day_list[i]]) 

print(dp[0])