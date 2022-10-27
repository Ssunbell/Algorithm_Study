#[프로그래머스_호텔방배정]
import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):

    def find_parent(x):
        if x not in parent:
            parent[x] = x+1
            return x
        parent[x] = find_parent(parent[x])
        return parent[x]

    parent = {}
    result = []
    for num in room_number:
        if num not in parent:       #배정받지않은 방
            parent[num] = num+1
            result.append(num)
        else:             
            x = find_parent(num)
            result.append(x)
    return result

print(solution(	10, [1, 3, 4, 1, 3, 1]))  #[1, 3, 4, 2, 5, 6]