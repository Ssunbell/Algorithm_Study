import sys
from collections import deque

input_s = lambda : sys.stdin.readline().strip()

n,m = map(int,input_s().split())
r, c, d = map(int,input_s().split())
places = [list(map(int,input_s().split())) for _ in range(n)]

root = [r,c]

def clean(root, d, places):
    cleaned = deque()
    cp = 0
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    curr = root
    clean_on = True
    turn_left = 0
    while clean_on:
        if curr not in cleaned:
            cleaned.append(curr)
            turn_left = 0
        # 현재 방향에서 왼쪽방향
        dir_left = (d-1) % 4 
        # 현재 위치에서 왼쪽 위치
        curr_left = [curr[0]+di[dir_left],curr[1]+dj[dir_left]]
        # a 단계
        if curr_left not in cleaned and places[curr_left[0]][curr_left[1]] == 0:
            d = dir_left # 왼쪽으로 회전
            curr = curr_left  # 전진
        else:
            d = dir_left
            turn_left += 1
        if turn_left == 4:
            dir_back = (d+2) % 4
            curr_back = [curr[0]+di[dir_back],curr[1]+dj[dir_back]]
            if places[curr_back[0]][curr_back[1]] == 1:
                clean_on = False
            else:
                curr = curr_back
                turn_left = 0

    cp = len(cleaned)
    return cp

print(clean(root,d,places))


