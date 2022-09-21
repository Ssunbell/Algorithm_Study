cd = [[0]*100 for i in range(100)]

for n in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            cd[i][j] = 1

print(sum(sum(i) for i in cd))