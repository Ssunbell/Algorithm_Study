import sys

input = lambda: sys.stdin.readline().rstrip()

sign = list(input())

# () = 2
# [] = 3
# (x) * 2
# [x] * 3
# x, y = x + y

s_lst = []
answer = 0
s_calculation = 1

for i in range(len(sign)):

    print('s_calculation',sign[i], s_calculation, i)
    print('answer',sign[i],answer, i)
    if sign[i] == '(':
        s_lst.append(sign[i])
        s_calculation *= 2

    elif sign[i] == '[':
        s_lst.append(sign[i])
        s_calculation *= 3

    elif sign[i] == ')':
        if not s_lst or s_lst[-1] == '[':
            answer = 0 
            break
        if sign[i-1] == '(':
            answer += s_calculation
        s_lst.pop()
        s_calculation //= 2 # 다시 1로 만들어주기

    else: # ']'
        if not s_lst or s_lst[-1] == '(':
            answer = 0 
            break
        if sign[i-1] == '[':
            answer += s_calculation
        s_lst.pop()
        s_calculation //= 3 # 다시 1로 만들어주기

        
if s_lst:
    print(0)

else:
    print(answer)