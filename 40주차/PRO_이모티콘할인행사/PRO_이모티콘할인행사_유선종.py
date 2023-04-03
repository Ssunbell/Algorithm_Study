from typing import *

cases:List[List[int]] = []
def dfs(n:int, case:List[int]=[]):
    if len(case) == n:
        cases.append([10 * (r+1) for r in case])
        return
    
    for i in range(4):
        dfs(n, case + [i])

def solution(users, emoticons):
    n = len(emoticons)
    answer = [0,0]
    dfs(n)
    for case in cases:
        sub_answer = [0,0]
        for ratio, marginal_price in users:
            total_price = 0
            for i in range(n):
                if ratio <= case[i]:
                    total_price += emoticons[i] * (100 - case[i]) * 0.01
                    marginal_price -= emoticons[i] * (100 - case[i]) * 0.01
            if marginal_price <= 0:
                sub_answer[0] += 1
            else:
                sub_answer[1] += total_price

        if sub_answer[0] > answer[0]:
            answer = sub_answer[:]
        elif sub_answer[0] == answer[0]:
            if max(answer[1], sub_answer[1]) > answer[1]:
                answer = sub_answer[:]

    return answer