import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
like_dict = defaultdict(list)
classroom = [[-1 for _ in range(n)]for _ in range(n)]

around = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_near(graph: list, location: tuple) -> list:
    x, y = location
    near = []
    for dx, dy in around:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            yield (nx, ny)


def count_near_likestudent(graph: list, location: tuple, like_list: list) -> int:
    cnt = 0
    x, y = location
    for nx, ny in get_near(graph, location):
        if graph[nx][ny] in like_list:
            cnt += 1
    return cnt


def count_near_emptyspace(graph: list, location: tuple) -> int:
    cnt = 0
    for nx, ny in get_near(graph, location):
        if graph[nx][ny] == -1:
            cnt += 1
    return cnt


for _ in range(n**2):
    student = list(map(lambda x: int(x) - 1, input().split()))
    like_dict[student[0]] = student[1:]

    set_location = [-1, []]
    for i in range(n):
        for j in range(n):
            if classroom[i][j] != -1:
                continue
            near_like_student = count_near_likestudent(
                graph=classroom, location=(i, j), like_list=like_dict[student[0]])
            if near_like_student < set_location[0]:
                continue
            elif near_like_student > set_location[0]:
                set_location = (near_like_student, [(i, j)])
            elif near_like_student == set_location[0]:
                set_location[1].append((i, j))

    fix_location = [-1, []]
    for x, y in set_location[1]:
        near_empty_region = count_near_emptyspace(
            classroom, (x, y))
        if near_empty_region < fix_location[0]:
            continue
        elif near_empty_region > fix_location[0]:
            fix_location = (near_empty_region, [(x, y)])
        elif near_empty_region == fix_location[0]:
            fix_location[1].append((x, y))

    x, y = sorted(fix_location[1])[0]
    classroom[x][y] = student[0]

answer = 0

for i in range(n):
    for j in range(n):
        cnt = -1
        fav_list = like_dict[classroom[i][j]]
        for nx, ny in get_near(graph=classroom, location=(i, j)):
            if classroom[nx][ny] in fav_list:
                cnt += 1
        answer += int(10**(cnt))

print(answer)

'''
구현
조건 1: 비어있는 킨 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
조건 2: 인접한 칸 중 비어있는 칸이 가장 많은 칸
조건 3: 행의 번호가 가장 작은 칸
조건 4: 열의 번호가 가장 작은 칸
'''
