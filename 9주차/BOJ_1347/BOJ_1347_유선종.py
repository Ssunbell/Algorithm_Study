n = int(input())
command = list(input())

map = [[0] * (n * 2) for _ in range(n*2)]

xn = n
yn = n
# 정중앙에서 시작
map[yn][xn] = '.'

# left(서) up(북) right(동) down(남)
dx = [-1, 0, 1, 0] # 좌우이동은 열의 이동을 의미하므로 [][dx]
dy = [0, -1, 0, 1] # 상하이동은 행의 이동을 의미하므로 [dy][]
direction = 3

for com in command:
    if com == 'L':
        direction = (direction - 1) % 4
    elif com == 'R':
        direction = (direction + 1) % 4
    elif com == 'F':
        xn = dx[direction] + xn
        yn = dy[direction] + yn
        map[yn][xn] = '.'

minmax = []
temp_row = []
temp_col = []
for i, row in enumerate(map):
    try:
        print('들어왔다')
        temp_col.append(row.index('.'))
        temp_col.append()
        temp_row.append(i)
    except:
        print('없당')
        continue
minmax.append(min(temp_row))
minmax.append(max(temp_row))
minmax.append(min(temp_col))
minmax.append(max(temp_col))

print(minmax)



print(map)