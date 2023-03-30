from typing import *

N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]

def move_block(
    array:List[List[int]],
    q:List[Tuple[int, int]]
) -> List[List[int]]:
    row, col = len(array), len(array[0])
    k = 0
    pos = [n for n in q]
    for x, y in pos:
        if row > col: # green_array
            nx, ny = x+1, y
        elif row < col: # blue_array
            nx, ny = x, y+1
        if nx==row or ny==col or array[nx][ny] > 0:
            break
        else:
            pos.append((nx, ny))
            k += (1 / len(q))

    for x, y in q:
        if row > col: # green_array
            array[x+int(k)][y] += 1
        elif row < col: # blue_array
            array[x][y+int(k)] += 1
        
    return array

def check_delete_blocks(
    array:List[List[int]],
    result:int
) -> List[List[int]]:
    row, col = len(array), len(array[0])
    if row > col: # green_array
        r = row-1
        while r != -1:
            if all(array[r]):
                result += 1
                for k in range(r, 0, -1):
                    array[k] = array[k-1]
                array[0] = [0] * col
            else:
                r -= 1
    elif row < col: # blue_array
        c = col-1
        while c != -1:
            if all([row[c] for row in array]):
                result += 1
                for r in range(row):
                    for k in range(c, 0, -1):
                        array[r][k] = array[r][k-1]
                    array[r][0] = 0
            else:
                c -= 1
    
    return array, result

def check_sub_array(array:List[List[int]]) -> List[List[int]]:
    row, col = len(array), len(array[0])
    
    if row > col: # green_array
        while any(array[1]):
            for r in range(row-1, 0, -1):
                array[r] = array[r-1]
            array[0] = [0] * col
    elif row < col: # blue_array
        while any([row[1] for row in array]):
            for r in range(row):
                for c in range(col-1, 0, -1):
                    array[r][c] = array[r][c-1]
                array[r][0] = 0
    return array

green_result = 0
blue_result = 0
blue_array = [[0]*6 for _ in range(4)]
green_array = [[0]*4 for _ in range(6)]
for t, x, y in blocks:
    if t == 1:
        blue_q = [(x, 0)]
        green_q = [(0, y)]
    elif t == 2:
        blue_q = [(x, 1), (x, 0)]
        green_q = [(0, y+1), (0, y)]
    elif t == 3:
        blue_q = [(x+1, 0), (x, 0)]
        green_q = [(1, y), (0, y)]
        
    blue_array = move_block(blue_array, blue_q)
    blue_array, blue_result = check_delete_blocks(blue_array, blue_result)
    blue_array = check_sub_array(blue_array)
    
    green_array = move_block(green_array, green_q)
    green_array, green_result = check_delete_blocks(green_array, green_result)
    green_array = check_sub_array(green_array)
print(blue_result + green_result)
print(sum(map(sum, blue_array)) + sum(map(sum, green_array)))

