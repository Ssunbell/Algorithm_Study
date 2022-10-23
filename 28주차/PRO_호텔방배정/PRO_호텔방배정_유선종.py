import sys
sys.setrecursionlimit(10**8)
def find_parent(room,n):
    try:
        # 기존의 key: 방 번호, value : 최소 방 번호로 업데이트
        room[n] = find_parent(room,room[n])

        return room[n]
    except:
        # key : 방 번호, value : 그 다음 방 번호
        room[n] = n + 1

        return n

def solution(k, room_number):
    result = []
    room = dict()
    for n in room_number:
        result.append(find_parent(room,n))
    return result