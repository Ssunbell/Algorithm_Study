# dp[i]는 i번째 포도주까지 시식했을때 가장 많이 먹을 수 있는 양
# check는 포도주를 연속으로 먹은 횟수
# i-1일때 check < 2 라면 i에서는 무조건 포도주시식해야 가장 많은 양을 시식하는거임
# i-1일때 check == 2라면 3가지경우중 하나가 dp[i]값
# 1. dp[i-3]까지 먹고 i-2를 안먹고 i-1과 i를 먹을 때, 이때 check는 2
# 2. dp[i-2]까지 먹고 i를 먹을 때 이때 check는 1
# 3. dp[i-1]까지 먹고 i를 안먹을 때 이때 check는 0

n = int(input())

check = 0
dp = [0 for _ in range(n+1)] # i=3 일때 i-3을 참조하기위해 0번 인덱스에 더미데이터 0 추가
wine = [0 for _ in range(n+1)] # dp와 인덱스를 맞추기 위해 더미데이터 추가
for i in range(1,n+1):
    wine[i] = int(input())

for i in range(1,n+1): # dp와 인덱스를 맞추기 위해 1부터 반복문 시작
    if i < 3:  # i<3일때는 와인을 그냥 마시는 것이 이득
        dp[i] = sum(wine[:i+1]) # 0부터 i번째 와인의 합을 dp에 저장
        check += 1 # 와인을 마신 횟수 증가
    else:
        if check == 2: 
            dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-1], dp[i-2]+wine[i]) # 이중 가장 큰 값을 dp에 저장
            # 저장한 값에 따라서 check의 값이 달라짐.
            if dp[i] == dp[i-1]: # i번째 와인을 마시지 않았기 때문에 check = 0
                check = 0
            elif dp[i] == dp[i-2] + wine[i]: # i번째 와인을 마셨기 때문에 check = 1
                check = 1
            elif dp[i] == dp[i-3]+wine[i-1]+wine[i]: # i-1, i를 마셨기 때문에 check = 2
                check = 2
        else: # check < 2 일 경우 와인을 그냥 마시는 것이 이득
            dp[i] = dp[i-1] + wine[i]
            check += 1

# dp값중 가장 큰 값이 정답
print(max(dp))
