n = int(input())
position = [list(map(int, input().split())) for _ in range(n)]

x = [position[i][0] for i in range(n)]
y = [position[i][1] for i in range(n)]
outbox_length = [max(x)+10 - min(x), max(y)+10 - min(y)]
outbox = [ [0 for j in range(outbox_length[0])] for i in range(outbox_length[1])]

x_pos = [position[i][0] - min(x) for i in range(n)]
y_pos = [position[i][1] - min(y) for i in range(n)]

for xl, yl in zip(x_pos, y_pos):
    x_null = list(map(int, '0' * outbox_length[0]))
    for y in range(yl, yl+10):
        for x in range(xl, xl+10):
            x_null[x] = 1
        outbox[y] = [o + v for o, v in zip(outbox[y], x_null)]
        
num = 0
for i in range(outbox_length[1]):
    num += outbox[i].count(0)
print((outbox_length[0] * outbox_length[1] - num))