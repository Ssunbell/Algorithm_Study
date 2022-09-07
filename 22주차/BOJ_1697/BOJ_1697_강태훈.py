import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
# 이 후 코드를 실행할 필요 없이 답이 확정된 케이스
if N >= K:
    print(N - K)
    exit()

BOUNDARY = min(100000, max(N, K) * 2)
# 중복방문 체크 및 최단거리 저장 용도
distance = [0] * (BOUNDARY + 1)
# BFS
que = deque([N])
while que:
    curr = que.popleft()
    print(curr)
    if curr == K:
        print(distance[K])
        break
    for nx in (curr - 1, curr + 1, curr * 2):
        # 주어진 범위 내에 있는지, 중복방문을 하고 있는지 확인 후 큐에 삽입, 거리 저장
        if 0 <= nx <= BOUNDARY and distance[nx] == 0:
            que.append(nx)
            distance[nx] = distance[curr] + 1

'''
최단거리 문제의 경우 기준점과 가까운 위치부터 큐에 삽입해 확인할 수 있는 BFS방식이 적합함.

N이 K보다 클 경우 뒤로 한칸씩 가는 방법만 존재함. 이 경우 큐에 curr * 2가 연속해서 들어가게 되어 필요 이상으로 많은 연산이 필요함. 예를들어 입력이 100 1 인 경우 70000 이상의 수까지 체크하게 됨.
이를 해결하고자 조기종료 조건을 추가하고 BOUNDARY를 조정함.
'''
