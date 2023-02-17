def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = 0, 0
    for p in problems:
        max_alp = max(p[0], max_alp)
        max_cop = max(p[1], max_cop)
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp[alp][cop] = 0
    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            if a < max_alp:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)
            if c < max_cop:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    min_alp = min(a + alp_rwd, max_alp)
                    min_cop = min(c + cop_rwd, max_cop)
                    dp[min_alp][min_cop] = min(dp[min_alp][min_cop], dp[a][c] + cost)
    return dp[-1][-1]

"""
모든 문제를 푼다: 문제들의 최대 요구 사항 이상을 도달하기만 하면 됨.
"""