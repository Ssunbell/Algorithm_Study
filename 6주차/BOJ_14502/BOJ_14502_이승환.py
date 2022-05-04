import copy
import sys

input_s = lambda : sys.stdin.readline().strip()

n,m = map(int, input_s().split())
lab = [list(map(int, input_s().split())) for _ in range(n)]

def bfs(arr):
    visited = []
    q = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i,j))
    while q:
        curr = q.pop(0)
        if curr in visited:
            continue
        visited.append(curr)
        arr[curr[0]][curr[1]] = 2
        if curr[0] -1 >= 0 and (curr[0] -1,curr[1]) not in visited and arr[curr[0] -1][curr[1]] != 1 and (curr[0]-1,curr[1]) not in q:
            q.append((curr[0]-1,curr[1]))
        if curr[0] +1 < n and (curr[0] +1,curr[1]) not in visited and arr[curr[0] +1][curr[1]] != 1 and (curr[0]+1,curr[1]) not in q:
            q.append((curr[0]+1,curr[1]))
        if curr[1] -1 >= 0 and (curr[0],curr[1]-1) not in visited and arr[curr[0]][curr[1]-1] != 1 and (curr[0],curr[1]-1) not in q:
            q.append((curr[0],curr[1]-1))
        if curr[1] +1 < m and (curr[0],curr[1]+1) not in visited and arr[curr[0]][curr[1] +1] != 1 and (curr[0],curr[1]+1) not in q:
            q.append((curr[0],curr[1]+1))
    result = find_zero(arr)
    return result

def find_zero(arr):
    sum_zero = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                sum_zero += 1
    return sum_zero

def wall_maker(arr):
    result = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                result.append((i,j))
    return result

def find_max(arr):
    all_lab = []
    wall_index = wall_maker(arr)
    size = len(wall_index)
    for first in range(0, size - 2):
        for second in range(first + 1, size - 1):
            for third in range(second + 1, size):
                first_wall = wall_index[first]
                second_wall = wall_index[second]
                third_wall = wall_index[third]
                new_lab = copy.deepcopy(lab)
                new_lab[first_wall[0]][first_wall[1]] = 1
                new_lab[second_wall[0]][second_wall[1]] = 1
                new_lab[third_wall[0]][third_wall[1]] = 1
                all_lab.append(new_lab)
    return all_lab

k = find_max(lab)
all_result = []
for i in k:
    zero = bfs(i)
    all_result.append(zero)
print(max(all_result))