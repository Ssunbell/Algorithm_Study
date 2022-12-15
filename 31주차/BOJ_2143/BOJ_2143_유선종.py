import sys

input = lambda : sys.stdin.readline().rstrip()

T = int(input())
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_dict = dict()
for i in range(n):
    n_sum = 0
    for j in range(i, n):
        n_sum += n_list[j]
        if n_sum in n_dict:
            n_dict[n_sum] += 1
        else:
            n_dict[n_sum] = 1

cnt = 0
for i in range(m):
    m_sum = 0
    for j in range(i, m):
        m_sum += m_list[j]
        if T - m_sum in n_dict:
            cnt += n_dict[T - m_sum]

print(cnt)

# from typing import Iterator

# def cumulative_sum(arr:list) -> Iterator[int]:
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             yield sum(arr[i:j+1])

# T = int(input())
# n = int(input())
# n_list = list(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

# n_dict = dict()
# m_dict = dict()
# for i in cumulative_sum(n_list):
#     if i in n_dict:
#         n_dict[i] += 1
#     else:
#         n_dict[i] = 1

# for i in cumulative_sum(m_list):
#     if i in m_dict:
#         m_dict[i] += 1
#     else:
#         m_dict[i] = 1
# cnt = 0

# for key, value in n_dict.items():
#     if (T - key) in m_dict:
#         cnt += (value * m_dict[T-key])
# print(cnt)