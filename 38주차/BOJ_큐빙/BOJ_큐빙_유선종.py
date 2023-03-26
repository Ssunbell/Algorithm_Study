from typing import *

root_cube = {
    'U' : [['w'] * 3 for _ in range(3)], # U 윗 면
    'L' : [['g'] * 3 for _ in range(3)], # L 왼쪽 면
    'F' : [['r'] * 3 for _ in range(3)], # F 앞 면
    'R' : [['b'] * 3 for _ in range(3)], # R 오른쪽 면
    'B' : [['o'] * 3 for _ in range(3)], # B 뒷 면
    'D' : [['y'] * 3 for _ in range(3)], # D 아랫 면
}

def plane_around(plane:str) -> List[str]:
    # [위, 왼, 오, 아래]
    if plane == 'U':
        return ['B', 'L', 'R', 'F']
    elif plane == 'L':
        return ['U', 'B', 'F', 'D']
    elif plane == 'F':
        return ['U', 'L', 'R', 'D']
    elif plane == 'R':
        return ['U', 'F', 'B', 'D']
    elif plane == 'B':
        return ['U', 'R', 'L', 'D']
    elif plane == 'D':
        return ['B', 'L', 'R', 'F']
    
def storage_rotate(storage:List[str], rotate:str) -> List[str]:
    # [위, 왼, 오 아래]
    if rotate == '+':
        return  [storage[1], storage[3], storage[0], storage[2]]
    elif rotate == '-':
        return  [storage[2], storage[0], storage[3], storage[1]]
    
def plane_around_rotate(cube:dict, plane:str, rotate:str) -> dict:
    storage = []
    planes = plane_around(plane)
    if plane == 'U':
        storage = [cube[p][0] for p in planes]
    elif plane == 'L':
        for i, p in enumerate(planes):
            storage.append([row[0] for row in cube[p]])
    elif plane == 'F':
        for i, p in enumerate(planes):
            if i == 0 or i == 3:
                storage.append(cube[p][-1])
            elif i == 1:
                storage.append([row[-1] for row in cube[p]])
            elif i == 2:
                storage.append([row[0] for row in cube[p]])
    elif plane == 'R':
        for i, p in enumerate(planes):
            if i == 2:
                storage.append([row[0] for row in cube[p]])
            else:
                storage.append([row[-1] for row in cube[p]])
    elif plane == 'B':
        for i, p in enumerate(planes):
            if i == 0 or i == 3:
                storage.append(cube[p][0])
            elif i == 1:
                storage.append([row[-1] for row in cube[p]])
            elif i == 2:
                storage.append([row[0] for row in cube[p]])
    elif plane == 'D':
        storage = [cube[p][-1] for p in planes]
    
    storage = storage_rotate(storage, rotate)
    
    if plane == 'U':
        for i, p in enumerate(planes):
            cube[p][0] = storage[i]
    elif plane == 'L':
        for i, p in enumerate(planes):
            if i == 1:
                for j in range(3):
                    cube[p][j][-1] = storage[i][j]
            else:
                for j in range(3):
                    cube[p][j][0] = storage[i][j]
    elif plane == 'F':
        for i, p in enumerate(planes):
            if i == 0 or i == 3:
                cube[p][-1] = storage[i]
            else:
                for j in range(3):
                    if i == 1:
                        cube[p][j][-1] = storage[i][j]
                    elif i == 2:
                        cube[p][j][0] = storage[i][j]
    elif plane == 'R':
        for i, p in enumerate(planes):
            for j in range(3):
                if i == 2:
                    cube[p][j][0] = storage[i][j]
                else:
                    cube[p][j][-1] = storage[i][j]
    elif plane == 'B':
        for i, p in enumerate(planes):
            if i == 0 or i == 3:
                    cube[p][0] = storage[i]
            else:
                for j in range(3):
                    if i == 1:
                        cube[p][j][-1] = storage[i][j]
                    elif i == 2:
                        cube[p][j][0] = storage[i][j]
    elif plane == 'D':
        for i, p in enumerate(planes):
            cube[p][-1] = storage[i]
    return cube

n = int(input())
commands = []
for _ in range(n):
    _ = int(input())
    commands.append([tuple(com)  for com in input().split()])

for command in commands:
    cube = {p:c for p, c in root_cube.items()}
    for p, r in command:
        if r == '+':
            cube[p] = [list(row[::-1]) for row in zip(*cube[p])]
        elif r == '-':
            cube[p] = [list(row) for row in zip(*[r[::-1] for r in cube[p]])]
        # print(cube)
        cube = plane_around_rotate(cube, p, r)
    for row in cube['U']:
        print(''.join(row))
        # for key, value in cube.items():
        #     print(key)
        #     for row in value:
        #         print(row)
# print(commands)
    