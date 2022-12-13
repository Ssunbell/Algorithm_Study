import sys
input = sys.stdin.readline
from itertools import combinations
from itertools import accumulate as acc
from collections import Counter

t = int(input().strip())
n = int(input().strip())
a = [0] + list(map(int, input().split()))
m = int(input().strip())
b = [0] + list(map(int, input().split()))

answer = 0

# 우선 a와 b 배열 각각의 누적합을 구한 후, 각 배열들의 부배열의 합이 될 수 있는 모든 경우의 수를 구한다 (1000C2 라서 가능함)
_perfix_a = [c_a[1] - c_a[0] for c_a in combinations(acc(a), 2)]
_perfix_b = [c_b[1] - c_b[0] for c_b in combinations(acc(b), 2)]

b_dic = Counter(_perfix_b)
b_dic_key = set(b_dic.keys())

for v in _perfix_a:
    if t - v in b_dic_key:
        answer += b_dic[t - v]

print(answer)