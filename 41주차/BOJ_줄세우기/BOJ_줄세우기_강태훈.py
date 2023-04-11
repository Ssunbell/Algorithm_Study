import sys
input = sys.stdin.readline

def solve(n, i_graph, o_graph):
    answer = []
    stack = [i for i in range(1,n+1) if not i_graph[i]]
    while stack:
        cnode = stack.pop()
        answer.append(cnode)
        for node in o_graph[cnode]:
            i_graph[node] -= 1
            if not i_graph[node]:
                stack.append(node)
    return answer

if __name__ == "__main__":
    n, m = map(int, input().split())
    o_graph, i_graph = [[] for _ in range(n+1)], [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        i_graph[b] += 1
        o_graph[a].append(b)
    print(*solve(n, i_graph, o_graph), end=" ")

"""
간선의 개수가 n-1보다 크다 -> 트리로 해결 불가능한 문제 -> 그래프 문제
    이 때 n의 조건이 32000 -> 인접행렬 사용 시 10억에 가까운 메모리 공간이 필요하다.
        따라서 인접 리스트로 접근해야 한다.
A > B > C > A 인 경우는 해결 불가능한 case로 볼 수 있다 -> 사이클 존재 X -> DAG(방향성 비순환 그래프) -> 위상정렬
"""