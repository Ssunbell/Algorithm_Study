def find_max_index(i, max_num, priorities):
    l = len(priorities)
    while True:
        if priorities[i] == max_num:
            return i
        i = (i + 1) % l

def solution(priorities, location):
    answer = 1
    i = 0
    while True:
        max_num = max(priorities)
        i = find_max_index(i, max_num, priorities)
        if i == location:
            return answer
        priorities[i] = 0
        answer += 1
    return answer
