#[금민수의 합]
def recur(num):
    min_dp = 100
    if num in gold:
        result.append(num)
        return
    if dp[num] >= 100:
        result.append(-1)
        return
    for g in gold:
        if num - g < 0:
            break
        if min_dp > dp[num-g]:
            min_dp = dp[num - g]
            tmp = g
    result.append(tmp)
    recur(num - tmp)

target = int(input())
length = len(str(target))
#연산에 쓰이는 금민수 리스트 : target의 자리수까지의 금민수들만 구한다.
gold_str = ['4', '7']
for l in range(2, length+1):
    for i in range(len(gold_str)):
        gold_str.append(gold_str[i]+'4')
        gold_str.append(gold_str[i]+'7')
gold = list(map(int, list(set(gold_str))))
gold.sort()
#인덱스의 해당 숫자까지 오기까지 필요한 금민수의 수 계산 (bottom-up)
dp=[0]
for i in range(1,target+1):
    m=100
    for g in gold:
        if g>i:
            break
        if dp[i-g]<m:
            m=dp[i-g]
    dp.append(m+1)

result = []
recur(target)
if -1 in result:
    print(-1)
else:
    result.sort()
    print(*result, sep=' ')

'''
#틀린 dp 구하기
dp = [250000] * (target+1)
dp[4], dp[7] = 1, 1
for i in range(8, target+1):
    for g in gold:
        if i - g > 0:
            dp[i] = min(dp[i], dp[i-g] + 1)
'''