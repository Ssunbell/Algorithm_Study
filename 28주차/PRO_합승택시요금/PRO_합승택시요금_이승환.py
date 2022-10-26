def solution(n, s, a, b, fares):
    answer = 0
    max_val = float("inf") 
    # graph[i][j] 는 i+1 에서 j+1 로 가는 비용
    graph = [[max_val] * n for _ in range(n)]
    
    # 그래프 생성
    for i,j,w in fares:
        graph[i-1][j-1] = w
        graph[j-1][i-1] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    graph[i][j] = 0
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    
    answer = [graph[s-1][i] + graph[i][a-1] + graph[i][b-1] for i in range(n)]

    return min(answer)

'''
s에서 출발해서 특정지점 k까지 같이가고 그 다음 a,b로 각자 알아서 가는경우
그 값이 가장 작은게 정답.
그렇다면 모든 지점에서 모든 지점까지의 최단거리를 전부 구하고
모든 k 에 대해서 (s->k + k->a + k->b) 인 값중 최소값을 구하면 정답.
--> 플로이드 워셜 알고리즘으로 풀면 됨
'''

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(	6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
