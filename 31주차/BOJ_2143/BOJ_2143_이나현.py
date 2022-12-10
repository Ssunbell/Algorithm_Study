#[2143_두 배열의 합]
from itertools import combinations
from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
#구간합 counter
A_sum_dict = defaultdict(lambda:0)
for x1, x2 in combinations(range(n+1), 2):
    A_sum_dict[sum(A[x1:x2])] += 1
#가능한 경우 cnt
cnt = 0
for x1, x2 in combinations(range(m+1), 2):
    t = T - sum(B[x1:x2])
    cnt += A_sum_dict[t]
print(cnt)