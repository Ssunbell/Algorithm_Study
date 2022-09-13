def solution(N, r, c, answer=0):
    if N == 0:
        return answer
    nextwidth = 2 ** (N - 1)
    part_idx = 2 * r // nextwidth + c // nextwidth
    return solution(N - 1, r % nextwidth, c % nextwidth, answer + (nextwidth ** 2) * part_idx)


N, r, c = map(int, input().split())
print(solution(N, r, c))

'''
비슷한 동작을 계속해서 반복해서 수행함을 통해 재귀호출을 떠올렸다.
N의 최댓값인 15는 재귀적으로 호출해도 15회면 답을 도출해 낼 수 있기에 재귀적 호출횟수가 늘어남으로 인해 발생하는 문제에서도 자유롭다.
따라서 N을 기준으로 어떤 연산을 수행할지 정하고, N값에 의해 loop가 종료될 수 있도록 했다.

영역을 사분할하고 방문 순서에 따라 값을 지정한 후 입력받은 좌표가 해당되는 영역을 찾는다. (part_idx)
ex)
01
23
영역을 분할할 수 없다면(N == 0이라면) answer을 반환한다. => 종료조건

part_idx에 분할된 영역의 넓이를 곱하여 answer에 더하면 사분할된 영역을 차기 영역으로 사용할 수 있다. 이에 따라 r과 c도 조정한다.
'''
