#프로그래머스_코딩테스트공부
#다이나믹 프로그래밍으로 풀이
#해당 실력까지 도달하기위해 만든 table을 만든 후 table 갱신
def solution(alp, cop, problems):
    # 문제들 중 가장 큰 알고력과 코딩력을 구한다.
    max_alp, max_cop = 0, 0
    for al, co, _, _, _ in problems:
        max_alp = max(max_alp, al)
        max_cop = max(max_cop, co)
    # 초기값이 문제의 max값보다 큰 경우 예외처리
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    # 해당 실력을 갖기까지 필요한 최소 시간 테이블. 일단 아무 문제 안풀었다고 가정한 테이블
    table = [[float('inf')]*(max_cop+1) for _ in range(max_alp+1)]
    table[alp][cop] = 0
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i < max_alp:
                table[i+1][j] = min(table[i+1][j], table[i][j]+1)
            if j < max_cop:
                table[i][j+1] = min(table[i][j+1], table[i][j]+1)
            # 각 문제를 하나하나 돌면서 해당 실력에서 문제를 풀었을 때 드는 시간 갱신
            for al_req, co_req, al_rwd, co_rwd, cost in problems:
                if i >= al_req and j >= co_req:
                    ni = min(max_alp, i+al_rwd)
                    nj = min(max_cop, j+co_rwd)
                    if table[ni][nj] > table[i][j] + cost:
                        table[ni][nj] = table[i][j] + cost
    return table[max_alp][max_cop]




#85점 코드 : 교환법칙이 성립한다고 가정하고 풀이..
#문제 안풀고 1시간씩 시간 들였다고 가정한 table 초기화 후
#한문제씩 table 갱신
def solution(alp, cop, problems):
    # 문제들 중 가장 큰 알고력과 코딩력을 구한다.
    max_alp, max_cop = 0, 0
    for al, co, _, _, _ in problems:
        max_alp = max(max_alp, al)
        max_cop = max(max_cop, co)
    # 초기값이 문제의 max값보다 큰 경우 예외처리
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    # 해당 실력을 갖기까지 필요한 최소 시간 테이블. 일단 아무 문제 안풀었다고 가정한 테이블
    table = [[float('inf')]*(max_cop+1) for _ in range(max_alp+1)]
    table[alp][cop] = 0
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i < max_alp:
                table[i+1][j] = min(table[i+1][j], table[i][j]+1)
            if j < max_cop:
                table[i][j+1] = min(table[i][j+1], table[i][j]+1)
    # 각 문제를 하나하나 돌면서 해당 실력에서 문제를 풀었을 때 드는 시간 갱신
    for al_req, co_req, al_rwd, co_rwd, cost in problems:
        for i in range(al_req,max_alp+1):
            for j in range(co_req, max_cop+1):
                ni = min(max_alp, i+al_rwd)
                nj = min(max_cop, j+co_rwd)
                if table[ni][nj] > table[i][j] + cost:
                    table[ni][nj] = table[i][j] + cost
    return table[max_alp][max_cop]

# print(solution(	10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))