import sys

input = lambda : sys.stdin.readline().strip()

M, n = map(int, input().split())
list_command = [list(input().split()) for _ in range(n)]

def robot_move(M, list_command):
    #   x축  y축 x축 y축
    #   동   북  서   남
    list_loc = [0,0]
    xy = [1, 1, -1, -1]
    dir = 0

    for command in list_command:
        com, num = command[0], command[1]

        if com == 'MOVE':
            if dir == 0 or dir == 2:
                list_loc[0] += (int(num) * xy[dir])
                if list_loc[0] > M or list_loc[1] < 0:
                    return None
            elif dir == 1 or dir == 3:
                list_loc[1] += (int(num) * xy[dir])
                if list_loc[1] > M or list_loc[1] < 0:
                    return None
        elif com == 'TURN':
            if num == '0':
                dir = (dir + 1) % 4
            elif num == '1':
                dir = (dir - 1) % 4

    return list_loc
location = robot_move(M, list_command)
if location:
    print(*location)
else:
    print(-1)
    
