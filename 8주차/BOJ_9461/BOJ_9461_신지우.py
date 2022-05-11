t = int(input())

n = [int(input()) for i in range(t)]

p = [0] * 101

p[1] = 1
p[2] = 1
p[3] = 1

for i in n:
    for j in range(4, 101):
        p[j] = p[j-3] + p[j-2]
    print(p[i])