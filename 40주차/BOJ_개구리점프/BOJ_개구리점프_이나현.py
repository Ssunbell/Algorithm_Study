#백준 17619 개구리점프
# pypy3 통과. python 50점
# 1.시작점을 기준으로 통나무를 정렬한다.
# 2.통나무의 오른쪽 끝점을 기준으로 그룹화하기 O(N)
#     그룹화하는 방법 : 지금까지의 가장 큰 오른쪽 끝점보다 현재 통나무의 왼쪽 끝점이 더 큰 위치 -> 서로 다른 그룹
# 3.질문에 답하기 위해 같은 그룹인지 확인하기 O(N log1e9)
#     그룹 확인 방법 : 그룹정보는 오른쪽 끝점만 기록되어있다.
#                   bisect_right를 이용하여 통나무의 왼쪽 끝점을 통해 이전그룹의 오른쪽 끝점을 확인하여 같은 그룹인지 확인

from bisect import bisect_right

N, Q = map(int, input().split())
log_info = {i : list(map(int, input().split()))[:2] for i in range(1, N+1)}
questions = [list(map(int, input().split())) for _ in range(Q)]
 
#통나무 그룹화
logs = sorted(log_info.values(), key=lambda x: x[0])
groups = []
group_max = 0
for log in logs:
    if group_max < log[0]:
        groups.append(group_max)
    group_max = max(group_max, log[1])
groups.append(group_max)

#질문을 통해 그룹 확인
for question in questions:
    log1, log2 = question
    s1 = log_info[log1][0]
    s2 = log_info[log2][0]

    이전그룹e1 = bisect_right(groups, s1)
    이전그룹e2 = bisect_right(groups, s2)
    if 이전그룹e1 == 이전그룹e2:
        print(1)
    else:
        print(0)