# turn 0 : 왼쪽 90도 turn 1 : 오른쪽 90도
#

import sys


def input(): return sys.stdin.readline().strip()


m, n = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


for _ in range(n):
    order = [list(map(str, input().split()))]
    direction = 2
    x, y = 0, 0


for i in order:
    if i[0] == "TURN":
        if i[1] == "0":
            direction += 1
        else:
            direction -= 1
    elif i[0] == "MOVE":
        x += dx[direction] * int(i[1])
        y += dy[direction] * int(i[1])

if 0 < x <= m and 0 < y <= m:
    print(x, y, sep=" ")
else:
    print(-1)
