import sys

intput = lambda: sys.stdin.readline().rstrip()
exp = input().split('-')

num = []

for i in exp:
    if '+' in i:
        num_sum = 0
        s = i.split('+')
        for j in s:
            num_sum += int(j)
        num.append(num_sum)
    else:
        num.append(i)

num = list(map(int, num))

for z in range(1, len(num)):
    num[0] -= int(num[z])

print(num[0])