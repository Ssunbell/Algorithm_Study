import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
list_std = list(input().split())
rev = {'1' : '3', '2' : '4', '3' : '1', '4' : '2'}
reverse_std = list(map(lambda x: rev[x], list_std))[::-1]
m = int(input())
list_case = [list(input().split()) for _ in range(m)]

result = []
for case in list_case:
    for i in range(n):
        if case[i:] + case[:i] == list_std or case[i:] + case[:i] == reverse_std:
            result.append(case)
            break
print(len(result))
for case in result:
    print(*case)
    