def solution(k, room_number):
    answer = []
    room = dict()
    for r in room_number:
        room_list = []
        while True:
            try:
                p = room[r]
                room_list.append(r)
                r = p
            except:
                room[r] = r+1
                answer.append(r)
                for i in room_list:
                    room[i] = r+1
                break
    return answer

'''
어려워서 해설봄
배정할 방이 빈방이면 즉시배정, 부모노드를 저장(+1칸이 부모노드)
빈방이 아닐 경우 부모노드로 간다, 이때 방문했던 방을 저장
부모노드도 빈방이 아니면 빈방이 나올때까지 반복
빈방이 나오면 배정, 이때까지 방문했던 모든 방을 배정한 방의 부모노드로 최신화해준다.
'''
r = [1,3,1,1]

print(solution(10,r))