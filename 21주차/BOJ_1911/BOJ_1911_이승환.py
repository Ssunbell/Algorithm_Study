from math import ceil
import sys

input_s = lambda : sys.stdin.readline().strip()

n,l = map(int,input_s().split())

puddles = []
for i in range(n):
    start, end = map(int,input_s().split())
    puddles.append((start,end))

puddles.sort()
num_board = 0
puddle_end = 0

for puddle in puddles:
    start,end = puddle
    # 널빤지의 마지막이 웅덩이의 시작 지점보다 작으면 웅덩이의 시작 지점을 널빤지의 마지막지점으로함
    # 널빤지의 마지막 지점부터 널빤지를 대기 시작함
    # 만약 널빤지의 마지막 지점이 웅덩이 시작 지점보다 크다면 pass
    if puddle_end <= start:
        puddle_end = start
    num_board += ceil((end - puddle_end)/l)
    # 널빤지의 마지막 지점계산
    puddle_end += ceil((end - puddle_end)/l)*l

print(num_board)
