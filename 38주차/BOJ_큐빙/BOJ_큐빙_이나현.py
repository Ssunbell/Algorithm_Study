#5373 큐빙
#디버깅 중 -> 0점
def init_cube():
    colors = ['w','y','r','o','g','b']
    planes = ['U','D','F','B','L','R']
    for i in range(6):
        cube[planes[i]] = {}
        for j in range(1,10):
            cube[planes[i]][j] = colors[i]


def turn_self_plane(plane, direction):
    if direction == '+':
        turn = {1:3, 2:6, 3:9, 4:2, 5:5, 6:8, 7:1, 8:4, 9:7}
    else:
        turn = {3:1, 6:2, 9:3, 2:4, 5:5, 8:6, 1:7, 4:8, 7:9}
    for i in range(1,10):
        cube[plane][i] = cube[plane][turn[i]]


def turn_neighbor_cube(plane, direction):
    if plane == 'U':
        neighbors = 'BRFL'
    elif plane == 'F':
        neighbors = 'RDLU'
    elif plane == 'R':
        neighbors = 'UFDB'
    elif plane == 'L':
        neighbors = 'DFUB'
    elif plane == 'B':
        neighbors = 'LURD'
    else:
        neighbors = 'FLBR'


    indexes = ['369','123','147','789']
    if direction == '+':
        for i in range(3):
            index = indexes[i]
            index2 = indexes[(i+1)%4]
            neighbor = neighbors[i]
            neighbor2 = neighbors[(i+1)%4]
            for j in range(3):
                cube[neighbor][int(index[j])] = cube[neighbor2][int(index2[j])]
    else:
        for i in range(3):
            index = indexes[i]
            index2 = indexes[(i-1)%4]
            neighbor = neighbors[i]
            neighbor2 = neighbors[(i-1)%4]
            for j in range(3):
                cube[neighbor][int(index[j])] = cube[neighbor2][int(index2[j])]


T = int(input())
for t in range(T):
    n = int(input())
    command = list(input().split())
    cube = {}
    init_cube()
    for c in command:
        plane, direction = c
        turn_self_plane(plane, direction)
        turn_neighbor_cube(plane, direction)
    string = ''
    for i in range(1, 10):
        string += cube['U'][i]
        if i % 3 == 0:
            print(string)
            string = ''