from heapq import heappush, heappop

def solution(food_times, k):
    hq = []
    for i, food in enumerate(food_times):
        heappush(hq, (food, i+1))
    
    answer = -1
    yamyam = 0
    while hq:
        eat_loop = (hq[0][0] - yamyam) * len(hq)
        if eat_loop <= k:
            k -= (hq[0][0] - yamyam) * len(hq)
            yamyam, _ = heappop(hq)
        else:
            idx = k % len(hq)
            hq.sort(key = lambda x: x[1])
            answer = hq[idx][1]
            break
    
    return answer