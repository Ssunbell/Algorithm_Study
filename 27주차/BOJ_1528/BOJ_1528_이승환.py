target = int(input())

# 모든 금민수를 구함
minsu = []
minsu.append('')
check = True
while check:
    for m in minsu:
        f = m+'4'
        s = m+'7'
        if len(f)>2 or len(s)>2:
            check = False
            break
        minsu.append(f)
        minsu.append(s)
minsu.pop(0)
minsu = list(map(int,minsu))

# 금민수를 메모이제이션
dp = [-1]*2000000
for m in minsu:
    dp[m] = [m]

for i in range(target):
    for m in minsu:
        if dp[i] != -1 and dp[i+m] == -1:
            dp[i+m] = dp[i] + dp[m]

try:
    for i in dp[target]:
        print(i,end=" ")
except:
    print(-1)