import heapq
def solution(food_times, k):
    # 네트워크 지연 전에 이미 음식을 다 먹을 수 있는 경우
    if sum(food_times) <= k:
        return -1
    q = []
    # 결국 먹는 시간이 작은 음식을 기준으로 한번에 제거를 할 수 있으므로 heapq 사용
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    print(q)
    # 이전 음식 섭취까지 소요한 전체 시간
    sum_time = 0
    # 이전 음식의 섭취 시간
    previous_time = 0
    # 남은 음식 개수
    left = len(food_times)
    
    # q[0][0] - previous_time: 이 차이가 모든 음식들의 시간을 고려해서 한번에 제거할 수 있는 크기임
    # (q[0][0] - previous_time) * left: 남은 음식들만큼을 한번에 처리
    # sum_time + (q[0][0] - previous_time) * left: 총 소요 시간
    # sum_time + (q[0][0] - previous_time) * left <= k: k보다 클 경우가 네트워크 지연 이후임.
    while sum_time + (q[0][0] - previous_time) * left <= k:
        now_time = heapq.heappop(q)[0]
        # 현재 먹은 음식까지의 소요 시간 저장
        sum_time += (now_time - previous_time) * left
        left -= 1
        previous_time = now_time
    
    # 남은 음식들을 원래 순서로 재정렬
    res = sorted(q, key=lambda x:x[1])
    # (k - sum_time) % left: 이렇게 나머지값을 구하면 정답 음식의 위치를 알 수 있음
    return res[(k - sum_time) % left][1]