import sys
sys.setrecursionlimit(10**5)
def dfs(s, profit):
    global answer, graph
    tmp = profit // 10
    if graph[s] == -1 or profit // 10 < 1:
        if profit // 10 < 1:
            answer[s] += profit
        else:
            answer[s] += (profit - tmp)
        return
    earn = profit - tmp
    answer[s] += earn
    dfs(graph[s], tmp)
    
def solution(enroll, referral, seller, amount):
    global answer, graph
    answer = [0] * len(enroll)
    # s는 enroll 상에서의 직원들의 index인데, dfs에서 index로 접근하기 때문에
    # 민호의 경우에 대해서 처리해주기 위해 referral이 "-"인 경우에는 -1로 초기화
    # 그래서 접근하는 직원이 민호인 경우 즉, s == -1인 경우의 예외 처리를 하기 위함
    graph = [-1] * len(enroll)
    # 각 직원별로 index부여
    enroll2idx = {e:i for i, e in enumerate(enroll)}
    # i번째 직원의 parent의 index를 graph list에 담기
    for i, r in enumerate(referral):
        if r != "-":
            graph[i] = enroll2idx[r]
    for s, a in zip(seller, amount):
        dfs(enroll2idx[s], a * 100)
    return answer