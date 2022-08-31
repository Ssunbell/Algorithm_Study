import sys
from math import ceil
input = sys.stdin.readline
N, L = map(int, input().split())
puddles = [list(map(int, input().split())) for _ in range(N)]

latest_board, answer = -1, 0
# latest_board는 가장 최근에 설치된 널빤지의 최 우측
for start, end in sorted(puddles):
  # 현재 널빤지가 start의 우측에 존재하면 시작점을 널빤지의 최 우측으로 조정
  latest_board = max(start, latest_board)
  temp = ceil((end - latest_board) / L)
  answer += temp
  latest_board += temp * L
print(answer)