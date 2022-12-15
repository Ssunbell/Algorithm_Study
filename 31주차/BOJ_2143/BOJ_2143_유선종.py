'''
1
12
123
1234
12345
2
23
234
2345
3
34
345
4
45
5
'''

import sys
from typing import Iterator

input = lambda : sys.stdin.readline().rstrip()

def cumulative_sum(arr:list) -> Iterator[int]:
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            yield sum(arr[i:j+1])

T = int(input())
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_dict = dict()
m_dict = dict()
for i in cumulative_sum(n_list):
    if i in n_dict:
        n_dict[i] += 1
    else:
        n_dict[i] = 1

for i in cumulative_sum(m_list):
    if i in m_dict:
        m_dict[i] += 1
    else:
        m_dict[i] = 1
cnt = 0

for key, value in n_dict.items():
    if (T - key) in m_dict:
        cnt += (value * m_dict[T-key])
print(cnt)