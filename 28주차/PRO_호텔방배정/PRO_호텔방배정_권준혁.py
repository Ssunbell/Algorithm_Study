import sys
sys.setrecursionlimit(10**4)

def find_parent(dic, r):
    if not dic.get(r):
        dic[r] = r + 1
        return r
    else:
        dic[r] = find_parent(dic, dic[r])
        return dic[r]

def solution(k, room_number):
    answer = []
    dic = dict()
    for room in room_number:
        answer.append(find_parent(dic, room))
    return answer