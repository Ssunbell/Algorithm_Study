import sys
from collections import Counter

n = int(sys.stdin.readline())

num_lst = []

for i in range(n):
    num = int(input())
    num_lst.append(num)

# 산술평균
print(round(sum(num_lst) / n)) 

# 중앙값
num_lst.sort()
print(num_lst[len(num_lst) // 2])

# 최빈값
max_num = Counter(num_lst).most_common()
if len(max_num) > 1 and max_num[0][1] == max_num[1][1]: # 최빈값이 2개 이상일 때
    print(max_num[1][0])
else:
    print(max_num[0][0])

# 범위
print(max(num_lst) - min(num_lst))