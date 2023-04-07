from itertools import product

def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    arr = [[0.1,0.2,0.3,0.4] for _ in range(m)]
    cases = product(*arr)
    result = []
    for sale in cases:                        #각 이모티콘의 세일 케이스
        total_cost, total_register = 0, 0
        for user in users:                    #유저별로 계산
            cost = 0
            for i in range(m):                #모든 이모티콘 확인
                if sale[i] >= user[0]*0.01:
                    cost += emoticons[i] * (1-sale[i])
            if cost >= user[1]:
                total_register += 1
            else:
                total_cost += cost
        result.append([total_register, int(total_cost)])
    answer = sorted(result,reverse=True)[0]
    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))