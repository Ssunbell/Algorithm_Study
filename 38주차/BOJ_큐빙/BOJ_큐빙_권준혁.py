def rotate_u(cube:list, dir:str):
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
            cube[2][1][0][i]= cube[1][0][i][0]
        for i in range(3):
            cube[1][0][i][2] = a[2 - i]
            cube[1][2][i][2] = b[2 - i]
    return cube

def cubing(cube:list, q:str):
    loc, dir = q[0], q[1]
    if loc == 'U':
        cube = rotate_u(cube, dir)
    elif loc == 'D':
        cube = rotate_d(cube, dir)
    elif loc == 'F':
        cube = rotate_f(cube, dir)
    elif loc == 'B':
        cube = rotate_b(cube, dir)
    elif loc == 'L':
        cube = rotate_l(cube, dir)
    elif loc == 'R':
        cube = rotate_r(cube, dir)
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