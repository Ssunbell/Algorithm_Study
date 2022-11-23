"""
전략:
    dfs
    완전탐색
    현재 상태에서 발생할 수 있는 노드를 방문하면서
    방문 루트를 기준으로 dfs
"""

def solution(info, edges):
    def nextNodes(v):
        temp = list()
        for e in edges:
            # i는 부모노드, j는 자식노드
            i, j = e
            # 부모노드 번호 비교
            if v == i:
                temp.append(j)
        return temp

    # current: 현재 방문한 노드 확인
    def dfs(sheep, wolf, current, path):
        # 지금 노드 확인, 양 늑대 판별
        if info[current]:
            wolf += 1
        else:
            sheep += 1
        # 늑대가 다 잡아먹음, 무시
        if sheep <= wolf:
            return 0
        # 아니라면 임시 변수에 값 갱신
        maxSheep = sheep
        # 서칭 시작
        for p in path:
            for n in nextNodes(p):
                if n not in path:
                    path.append(n)
                    # 최대 양 판별
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n, path))
                    path.pop()
        return maxSheep

    answer = dfs(0, 0, 0, [0])
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info, edges))