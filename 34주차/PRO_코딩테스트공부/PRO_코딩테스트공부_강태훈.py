def solution(alp, cop, problems):
    problem_T = list(zip(*problems))
    max_alp, max_cop = max(problem_T[0]), max(problem_T[1])
    min_alp, min_cop = min(max_alp, alp), min(max_cop, cop)
    # 가능한 모든 비용에 대한 메모이제이션
    dp = [[(max_alp+max_cop)*100+1]*(max_cop+1) for _ in range(max_alp+1)]
    dp[min_alp][min_cop] = 0
    
    # 모든 알고리즘력과 코딩력에 대해 순회
    for c_alp in range(min_alp, max_alp+1):
        for c_cop in range(min_cop, max_cop+1):
            # 알고리즘력과 코딩력 단일로 키울 경우
            if c_alp + 1 <= max_alp:
                dp[c_alp + 1][c_cop] = min(dp[c_alp + 1][c_cop], dp[c_alp][c_cop] + 1)
            if c_cop + 1 <= max_cop:
                dp[c_alp][c_cop + 1] = min(dp[c_alp][c_cop + 1], dp[c_alp][c_cop] + 1)
            # 문제풀이의 경우
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= c_alp and cop_req <= c_cop:
                    n_alp = min(max_alp, c_alp+alp_rwd)
                    n_cop = min(max_cop, c_cop+cop_rwd)
                    dp[n_alp][n_cop] = min(dp[n_alp][n_cop], dp[c_alp][c_cop] + cost)

    return dp[-1][-1]