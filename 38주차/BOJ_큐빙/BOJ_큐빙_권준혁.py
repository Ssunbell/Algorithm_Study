def surface_rotate(cube:list, dir:str, mode:int):
    if mode == 1: # 회전 수행 전
        if dir == '+':
            cube[1][1] = [i[::-1] for i in zip(*cube[1][1])]
        elif dir == '-':
            cube[1][1] = [i for i in zip(*cube[1][1])][::-1]
    else: # 회전 수행한 것이면,
        if dir == '-':
            cube[1][1] = [i[::-1] for i in zip(*cube[1][1])]
        elif dir == '+':
            cube[1][1] = [i for i in zip(*cube[1][1])][::-1]
    return cube

def rotate(cube:list, dir:str):
    a = cube[0][1][2]
    b = cube[2][1][0]
    if dir == '+':
        for i in range(3):
            cube[0][1][2][i] = cube[1][0][2 - i][2]
            cube[2][1][0][i]= cube[1][2][2 - i][0]
        for i in range(3):
            cube[1][0][i][2] = b[i]
            cube[1][2][i][2] = a[i]
    elif dir == '-':
        for i in range(3):
            cube[0][1][2][i] = cube[1][2][i][2]
            cube[2][1][0][i] = cube[1][0][i][0]
        for i in range(3):
            cube[1][0][i][2] = a[2 - i]
            cube[1][2][i][2] = b[2 - i]
    return cube

def cubing(cube:list, q:str):
    loc, dir = q[0], q[1]
    if loc == 'U':
        cube = rotate(cube, dir)
    elif loc == 'D':
        cube[2][1], cube[3][1], cube[0][1], cube[1][1] = cube[0][1], cube[1][1], cube[2][1], cube[3][1]
        cube = rotate(cube, dir)
        cube[2][1], cube[3][1], cube[0][1], cube[1][1] = cube[0][1], cube[1][1], cube[2][1], cube[3][1]
    elif loc == 'F':
        cube[3][1], cube[0][1], cube[1][1], cube[2][1] = cube[0][1], cube[1][1], cube[2][1], cube[3][1]
        cube = rotate(cube, dir)
        cube[1][1], cube[2][1], cube[3][1], cube[0][1] = cube[0][1], cube[1][1], cube[2][1], cube[3][1]
    elif loc == 'B':
        cube[1][1], cube[2][1], cube[3][1], cube[0][1] = cube[0][1], cube[1][1], cube[2][1], cube[3][1]
        cube = rotate(cube, dir)
        cube[3][1], cube[0][1], cube[1][1], cube[2][1] = cube[0][1], cube[1][1], cube[2][1], cube[3][1]
    elif loc == 'L':
        # cube = rotate_l(cube, dir)
        pass
    elif loc == 'R':
        # cube = rotate_r(cube, dir)
        pass
    cube = rotate(cube, loc, dir) # 해당 면 회전
    return cube

if __name__ == '__main__':
    t = int(input())
    cube = \
        [
            [
                [['x', 'x', 'x'] for _ in range(3)],
                [['o', 'o', 'o'] for _ in range(3)],
                [['x', 'x', 'x'] for _ in range(3)],
            ],
            [
                [['g', 'g', 'g'] for _ in range(3)],
                [['w', 'w', 'w'] for _ in range(3)],
                [['b', 'b', 'b'] for _ in range(3)],
            ],
            [
                [['x', 'x', 'x'] for _ in range(3)],
                [['r', 'r', 'r'] for _ in range(3)],
                [['x', 'x', 'x'] for _ in range(3)],
            ],
            [
                [['x', 'x', 'x'] for _ in range(3)],
                [['y', 'y', 'y'] for _ in range(3)],
                [['x', 'x', 'x'] for _ in range(3)],
            ],
        ]
    for _ in range(t):
        n = int(input())
        query = input().split()
        for q in query:
            cube = cubing(cube, q)
        for a in cube[1][2]: # 윗면 출력
            print(''.join(a))

"""
X 앞 X
우 위 좌
X 뒤 X
X 아 X

X 위 X
우 뒤 좌
X 아 X
X 앞 X
"""