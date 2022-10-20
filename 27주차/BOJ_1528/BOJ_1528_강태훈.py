from math import log10
from collections import deque
import heapq
n = int(input())


def get_kms(num):
    kms = []
    for size in range(1, 1+int(log10(num))):
        for i in range(2**size):
            val = format(i, "b").zfill(size).replace(
                "0", "4").replace("1", "7")
            n = int(val)
            if n > num:
                return kms[::-1]
            kms.append(n)
    return kms[::-1]


kms_vals = get_kms(n)


q = deque()
answer = [-1]
memory = [[] for _ in range(n+1)]
q.append([0, []])

while q:
    curr_sum, curr_list = q.popleft()
    if curr_sum == n:
        answer = curr_list
        break

    for val in kms_vals:
        if val + curr_sum > n:
            continue
        if memory[val+curr_sum]:
            continue
        memory[val+curr_sum] = curr_list+[val]
        q.append([val+curr_sum, curr_list+[val]])

print(*sorted(answer))
