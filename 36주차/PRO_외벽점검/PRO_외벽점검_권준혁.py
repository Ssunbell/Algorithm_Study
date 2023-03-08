# 그리디하게 생각하면, dist가 큰 순서대로 하나씩 배치해서, 가능한 경우를 탐색한다.
# 직원을 둘 수 있는 경우의 수: len(weak) -> 모두 배치해보고,
# 아직 점검 못한 지점이 있으면 그 다음으로 큰 dist의 직원을 배치한다.
from bisect import bisect_right

def solution(n, weak, dist):
    answer = 10 ** 8
    dist.sort(reverse = True)
    weak += [w + n for w in weak]
    for idx, start in enumerate(weak[:len(weak) // 2]): # 시작점 찾기 (시작점은 weak의 위치로 두기)
        # idx ~ idx + len(weak) - 1: 여기 전체 구간임.
        # weak[:len(weak) // 2]: 시작점을 원래의 weak의 길이만큼만 설정하는 것이 맞음.
        cnt = 0
        now = start
        for d in dist:
            now += d # d만큼의 이동
            cnt += 1
            if True if now >= weak[idx + len(weak) // 2 - 1] else False:
                answer = min(answer, cnt)
                break
            else: # 다음 weak 찾기
                now = weak[bisect_right(weak, now)]
    return answer if answer != 10 ** 8 else -1

"""
레스토랑: 원형, 둘레: n미터
취약 지점 점검
- 점검 시간: 1시간
- 1시간 이동 거리: 각기 다름
- 최소 인원 할당
- 정북 방향: 0
- 취약 지점: 정북 방향으로부터 시계 방향으로 떨어진 거리로 나타냄.
- 각 인원들은 시계 혹은 반시계 방향 둘 다 가능
"""