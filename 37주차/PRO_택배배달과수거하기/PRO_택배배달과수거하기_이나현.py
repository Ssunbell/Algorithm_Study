#프로그래머스_택배 배달과 수거하기
#가장 먼 집부터 배달 및 수거
#멀리있는 집의 인덱스, 개수정보를 최대한 빠르게 알고싶다. -> heapq

from heapq import heappush, heappop

def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = []
    pickup = []
    for distance, value in enumerate(deliveries, start=1): #배달해야하는 위치와, 개수를 deliver이라는 힙에 넣기
        if value > 0:
            heappush(deliver, (-distance, value))
    for distance, value in enumerate(pickups, start=1): #수거해야하는 위치와, 개수를 pickup이라는 힙에 넣기
        if value > 0:
            heappush(pickup, (-distance, value))

    while deliver or pickup: #배달해야하거나 수거해야하는 것이 하나라도 남을 때까지
        d_n = 0              #트럭에 남은 배달 박스개수
        p_n = 0              #트럭에 할 수 있는 수거 박스개수
        d_distance = 0       #배달해야하는 집의 위치
        p_distance = 0       #수거해야하는 집의 위치
        if deliver: #배달해야하는 집이 있다면
            d_distance, d_value = heappop(deliver) #가장 먼 집의 위치와 개수를 꺼낸다.
            d_n = cap - d_value                    #트럭에 남은 박스 개수를 빼준다.
        if pickup:  #수거해야하는 집이 있다면
            p_distance, p_value = heappop(pickup)
            p_n = cap - p_value
        distance = max(-d_distance, -p_distance)   #배달, 수거해야하는 집 중 가장 먼 집의 거리
        answer += distance * 2                     #왕복이므로 *2
        if d_n < 0:                              #만약 해당 집에 배달해야하는 양보다 배달할 수 있는 박스개수가 적다 
            heappush(deliver, (d_distance, -d_n))#-> 부족한만큼 다시 정보를 heapq에 넣기
        if p_n < 0:
            heappush(pickup, (p_distance, -p_n))

        while d_n > 0 and deliver: #트럭에 배달할 수 있는 박스가 남고, 배달해야하는 집이 남아있을 때까지
            d_distance, d_value = heappop(deliver)
            d_n = d_n - d_value
            if d_n < 0:            #배달해야하는 개수보다 가능한 개수가 작다. -> 부족한만큼 그 정보를 heapq에 넣기
                heappush(deliver, (d_distance, -d_n))
        while p_n > 0 and pickup:
            p_distance, p_value = heappop(pickup)
            p_n = p_n - p_value
            if p_n < 0:
                heappush(pickup, (p_distance, -p_n))
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]), 16)
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 30)
print(solution(4, 5, [8, 0, 8, 0, 4], [0, 0, 0, 0, 20]), 50)
print(solution(2, 2, [0, 1], [0, 4]), 8)
print(solution(2, 2, [0, 0], [0, 6]), 12)
print(solution(2, 2, [0, 0], [4, 0]), 4)
print(solution(2, 2, [5, 0], [0, 3]), 10)
print(solution(5, 3, [5, 0, 5], [0, 1, 10]), 16)
print(solution(5, 3, [5, 1, 5], [0, 1, 10]), 16)
print(solution(2, 3, [0, 6, 13], [19, 0, 1]), 54)
print(solution(2, 3, [4, 2, 1], [0, 4, 1]), 16)
print(solution(4, 5, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 12)
print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]), (13 * 4 + 6 * 2 + 6) * 2)