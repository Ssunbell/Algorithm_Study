import sys

input_s = lambda : sys.stdin.readline().strip()

t = int(input_s())

for i in range(t):
    turtle_move = input_s()
    # 북 동 남 서, r일경우 +1, l일경우 -1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    t_curr = [0,0]
    t_dir = 0
    t_area = [[0],[0]]

    def change_direction(d,r):
        if r == "R":
            d += 1
        else:
            d -= 1
        curr_d = d % 4
        return curr_d

    for s in turtle_move:
        if s == "R" or s == "L":
            t_dir = change_direction(t_dir,s)
        elif s == "F":
            t_curr = [t_curr[0] + dx[t_dir], t_curr[1] + dy[t_dir]]
            t_area[0].append(t_curr[0])
            t_area[1].append(t_curr[1])
        elif s == "B":
            t_curr = [t_curr[0] - dx[t_dir], t_curr[1] - dy[t_dir]]
            t_area[0].append(t_curr[0])
            t_area[1].append(t_curr[1])

    max_x = max(t_area[0])
    min_x = min(t_area[0])
    max_y = max(t_area[1])
    min_y = min(t_area[1])

    lect = (max_x - min_x) * (max_y - min_y)

    print(lect)

