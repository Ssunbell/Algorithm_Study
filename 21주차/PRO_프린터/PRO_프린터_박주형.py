import sys
input = sys.stdin.readline


def solution(priorities, location):
    idx = [0] * len(priorities)
    idx[location] = 'j'
    answer = 0
    while True:
        if priorities[0] == max(priorities):
            answer += 1
            if idx[0] == 'j':
                return answer
                break
            else:
                priorities.pop(0)
                idx.pop(0)
        else:
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))
