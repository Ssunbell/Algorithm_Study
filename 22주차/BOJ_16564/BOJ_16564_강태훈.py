import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
N, K = map(int, input().split())
Level = [int(input()) for _ in range(N)]
heapify(Level)

targetLv = Level[0]
cnt = 0

while len(Level) >= 2:
    minLv = heappop(Level)
    cnt += 1
    need = (Level[0] - minLv) * cnt
    if K >= need:
        K -= need
        targetLv = Level[0]
    else:
        targetLv += K // cnt
        K = 0
        break
targetLv += K // N
print(targetLv)

'''
N의 경우 1000000으로 그리 큰 숫자가 아니지만, K와 X는 꽤 큰 수이다. 따라서 기준을 N으로 설정한다.
Level을 Minheap으로 만든 후 하나씩 뽑아가며 이전에 처리된 모든 수를 그 값에 맞춘다.
그 과정에서 K보다 큰 수가 필요로 하면 K를 적절히 분배한 후 loop를 break한다.
Level의 모든 원소에 대해 위 과정이 끝나면, 남은 K를 적절히 분배한다.
'''
