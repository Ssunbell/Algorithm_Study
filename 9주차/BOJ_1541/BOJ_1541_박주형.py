# - 기준으로 스플릿해서 괄호 넣고 전체 빼기 -> 55 - (50+40)
# ex 55-50+40 -> ['55', '50+40'] -> ['55', ['50', '40']]
# - 만 있는 경우, 첫번째만 + 나머지는 -로
# 55 + 50 - 40은? ['55+50', '40']
# 10+20+30+40 -> ['10+20+30+40']
# 인덱스 0은 무조건 +


import sys
def input(): return sys.stdin.readline().strip()


exp = input().split('-')
ans = 0
for i in range(len(exp)):
    if i == 0:
        dp = exp[i].split('+')
        for j in range(len(dp)):
            ans += int(dp[j])
    else:
        dp = exp[i].split('+')
        for j in range(len(dp)):
            ans -= int(dp[j])

print(ans)


'''import sys
def input(): return sys.stdin.readline().strip()


exp = input().split('-')
ans = 0
for i in range(len(exp)):
    if '+' in exp[i]:
        exp[i] = exp[i].split('+')
        if len(exp) == 1:
            for j in range(len(exp[i])):
                ans += int(exp[i][j])
        else:
            for j in range(len(exp[i])):
                ans -= int(exp[i][j])
    elif '+' not in exp[0]:
        ans += int(exp[0])
        ans -= int(exp[i])

print(ans)'''